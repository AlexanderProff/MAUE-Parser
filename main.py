import xml.parsers.expat
import pandas as pd

daten = {}
aktuelleTabelle = None
aktuelleHeader = []
aktuelleRow = []

#Parser-Funktion für gefundene Start-Tags
def start_element(name, attrs):
  #definiere alle Variablen als Global statt Funktions-Lokal
  global daten
  global aktuelleTabelle
  global aktuelleHeader
  global aktuelleRow

  #Table-Tag gefunden
  if name == 'Table' and attrs['name'] != None:
    #noch kein vorheriges öffnedes Table-Tag gefunden, neue Tabelle
    if aktuelleTabelle == None:
      aktuelleTabelle = attrs['name']
    #bereits vorher ein öffnendes Tabel-Tag gefunden (nested Table)
    else:
      daten[aktuelleTabelle] = pd.DataFrame(columns=aktuelleHeader)
      #noch Daten einer nicht abgeschlossenen Row wegzuschreiben
      if len(aktuelleRow) > 0:
        #Daten ans Ende der Tabelle schreiben
        daten[aktuelleTabelle].loc[len(daten[aktuelleTabelle])] = aktuelleRow
        aktuelleRow = []
      aktuelleHeader = []
      aktuelleTabelle = attrs['name']
  
  #Data-Tag gefunden
  elif name == 'Data' and attrs['header'] != None:
    aktuelleHeader.append(attrs['header'])
  
  #Column-Tag gefunden
  elif name == 'Column' and attrs['value'] != None:
    aktuelleRow.append(attrs['value'])
     
#Parser-Funktion für gefundene End-Tags     
def end_element(name):
  #definiere alle Variablen als Global statt Funktions-Lokal
  global daten
  global aktuelleTabelle
  global aktuelleHeader
  global aktuelleRow

  #schließendes Table-Tag gefunden
  if name == 'Table' and aktuelleTabelle != None:
    aktuelleHeader = []
    aktuelleTabelle = None

  #schließendes Row-Tag gefunden
  elif name == 'Row':
    #die bisher gefundenen Columns enthielten Werte
    if len(aktuelleRow) > 0:
      #erforderliche Tabelle existiert noch nicht
      if not aktuelleTabelle in daten:
        daten[aktuelleTabelle] = pd.DataFrame(columns=aktuelleHeader)
        aktuelleHeader = []
      #Daten ans Ende der Tabelle schreiben
      daten[aktuelleTabelle].loc[len(daten[aktuelleTabelle])] = aktuelleRow
      aktuelleRow = []

#Parser und Parser-Funktionen festlegen
p = xml.parsers.expat.ParserCreate(encoding='UTF-8')
p.StartElementHandler = start_element
p.EndElementHandler = end_element

#Lese Daten von test.xml und parse
with open('test.xml') as f:
  read_data = f.read()
  p.Parse(read_data)

#Iteriere über alle gefundenen Tabellen und gebe in separate CSVs aus
for bezeichnung, werte in daten.items():
  werte.to_csv(bezeichnung + '.csv', index=False)