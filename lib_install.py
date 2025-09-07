
# Importiert das 'os'-Modul, das Funktionen für Betriebssystem-Interaktionen bietet (wird hier aber nicht verwendet)
import os

# Importiert das 'subprocess'-Modul, um Unterprozesse zu erstellen und mit ihnen zu interagieren (z. B. Befehle ausführen)
import subprocess

# Importiert das 'sys'-Modul, um auf System-spezifische Parameter und Funktionen zuzugreifen (hier wird der Python-Interpreter verwendet)
import sys

# Definiert die Funktion 'install_package', die ein Python-Paket installiert
def install_package(package):

	# Führt den Befehl 'pip install package' aus, um das angegebene Paket zu installieren
	# sys.executable verweist auf den Pfad des laufenden Python-Interpreters
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Definiert die Funktion 'install_pip', um sicherzustellen, dass 'pip' installiert ist
def install_pip():

	try:

		# Versucht, 'ensurepip' zu verwenden, um die Standard-Pip-Version zu installieren, falls sie nicht bereits vorhanden ist
		subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])

	except subprocess.CalledProcessError:

		# Falls 'ensurepip' fehlschlägt, wird versucht, 'python3-pip' über das Paketmanagementsystem 'apt' zu installieren (Linux-spezifisch)
		subprocess.check_call(["sudo", "apt", "install", "-y", "python3-pip"])

# Definiert die Funktion 'install_tkinter', die versucht, das 'tkinter'-Modul zu installieren (eine GUI-Bibliothek für Python)
def install_tkinter():
	
	try:
		# Führt den Befehl aus, um 'python3-tk' über das Paketmanagementsystem 'apt' zu installieren (Linux-spezifisch)
		subprocess.check_call(["sudo", "apt", "install", "-y", "python3-tk"])
	
	except subprocess.CalledProcessError as e:
	
		# Gibt eine Fehlermeldung aus, falls die Installation fehlschlägt, und zeigt den Fehler an
		print(f"Error installing tkinter: {e}")

# Definiert die Funktion 'install_requirements', die dafür sorgt, dass alle erforderlichen Pakete installiert werden
def install_requirements():
	
	try:
		# Installiert 'pip', falls es noch nicht installiert ist
		install_pip()
		
		# Installiert notwendige Python-Pakete mit 'pip'
		install_package("matplotlib")  # Installiert das 'matplotlib'-Paket (wird häufig für Datenvisualisierung verwendet)
	
		install_package("numpy")	   # Installiert das 'numpy'-Paket (wird für numerische Berechnungen und wissenschaftliches Rechnen verwendet)
	
	except subprocess.CalledProcessError as e:
	
		# Gibt eine Fehlermeldung aus, falls bei der Installation eines Pakets ein Fehler auftritt, und zeigt den Fehler an
		print(f"Error installing a package: {e}")

# Definiert die Funktion 'run_with_sudo', die das Skript mit 'sudo' neu startet, wenn es nicht bereits als Root ausgeführt wird
def run_with_sudo():
	
	""" Restart the script with sudo if it's not already running as root. """
	# Überprüft, ob das Skript mit Root-Rechten ausgeführt wird (EUID = 0 bedeutet Root)
	if os.geteuid() != 0:
	
		# Wenn das Skript nicht mit Root-Rechten ausgeführt wird, wird eine Warnmeldung ausgegeben
		print("This script needs to be run with sudo.")
		
		# Informiert den Benutzer, dass das Skript mit 'sudo' neu gestartet wird
		print("Restarting with sudo...")
		
		# Führt das Skript erneut mit 'sudo' aus, indem der aktuelle Python-Interpreter und die Argumente übergeben werden
		subprocess.check_call(['sudo', sys.executable] + sys.argv)
		
		# Beendet das aktuelle Skript, nachdem der Neustart initiiert wurde
		sys.exit()

# Überprüft, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
	
	# Ruft die Funktion 'run_with_sudo' auf, um sicherzustellen, dass das Skript mit den erforderlichen Rechten läuft
	run_with_sudo()
	
	# Führt die Funktion 'install_tkinter' aus, um das tkinter-Paket zu installieren
	install_tkinter()
	
	# Führt die Funktion 'install_requirements' aus, um die benötigten Python-Pakete zu installieren
	install_requirements()