# MAUE-Parser
Parser für die Maschinenlesbare unidirektionale automatische Übergabe von Einsatzdaten "MAÜ" des Ministeriums des 
Inneren und für Sport des Landes Rheinland-Pfalz auf Basis der Datenformatbeschreibung MAÜ1.1 mit Stand Dezember 2020.

# Verwendung
Das Python-Skript erwartet eine Datei mit dem Namen "test.xml" im gleichen Verzeichnis, wie das Skript. Diese Datei wird geparst und jede gefundene Tabelle in eine 
separate CSV-Datei geschrieben im gleichen Verzeichnis geschrieben.

# Warnung
Existierende CSV-Dateien werden überschrieben, bestehende jedoch vorher nicht gelöscht. Daher kann nicht davon ausgegangen werden, 
dass die im Verzeichnis existierenden CSV-Dateien zwingend den aktuellen Stand wiedergeben - sie könnten von einem vorherigen Lauf stammen.

Weiterhin findet im Skript aktuell KEINE Fehlerbehandlung statt. 
