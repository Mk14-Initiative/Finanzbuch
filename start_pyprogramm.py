
#!/usr/bin/env python3
# Shebang-Zeile, die angibt, dass das Skript mit Python 3 ausgeführt werden soll

# Importiert das Modul 'finanz_start', das wahrscheinlich die Hauptfunktionen für die Finanzanwendung enthält
import finanz_start

# Definiert die Hauptfunktion des Skripts
def main():

	# Ruft die Funktion 'start' aus dem Modul 'finanz_start' auf, um die Anwendung zu starten
	finanz_start.start()

# Überprüft, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":

	# Ruft die Hauptfunktion auf, um das Programm zu starten
	main()
