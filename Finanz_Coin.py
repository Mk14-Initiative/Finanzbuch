
# Importiert das tkinter-Modul für die GUI-Entwicklung
import tkinter as tk

# Importiert die ttk (Themed Tkinter) für verbesserte Widgets
from tkinter import ttk

# Importiert alle Klassen und Funktionen aus tkinter
from tkinter import *

# Importiert die messagebox für die Anzeige von Dialogfeldern
from tkinter import messagebox

# Importiert die PhotoImage-Klasse für die Verwendung von Bildern
from tkinter import PhotoImage

# Importiert das datetime-Modul für die Arbeit mit Datum und Uhrzeit
import datetime

# Importiert ein benutzerdefiniertes Modul namens chip
import chip

# Importiert ein benutzerdefiniertes Modul namens month_view
import month_view

# Erstellt eine Liste von Monatsnamen
month_list = [
	"January",	# Januar
	"February",   # Februar
	"March",	  # März
	"April",	  # April
	"Mai",		# Mai
	"June",	   # Juni
	"July",	   # Juli
	"August",	 # August
	"September",  # September
	"October",	# Oktober
	"November",   # November
	"December"	# Dezember
]
# Definiert eine Funktion, die überprüft, ob ein Wert in eine Fließkommazahl umgewandelt werden kann
def check_of_float(value):

	# Beginnt einen Try-Block, um potenzielle Fehler zu behandeln
	try:
		
		# Überprüft, ob der Wert ein Komma enthält (deutsche Schreibweise)
		if "," in value:
		
			# Ersetzt das Komma durch einen Punkt, um die Umwandlung in float zu ermöglichen
			value = value.replace(",", ".")

		# Wandelt den bearbeiteten Wert in eine Fließkommazahl um
		value = float(value)

		# Gibt den umgewandelten Wert zurück
		return value

	# Behandelt den Fall, dass die Umwandlung in float fehlschlägt (z.B. wenn der Wert keine gültige Zahl ist)
	except ValueError:
		
		# Gibt None zurück, um anzuzeigen, dass die Umwandlung nicht erfolgreich war
		return None

	# Diese Zeile ist überflüssig, da die Rückgabe bereits im try-Block behandelt wird
	return
# Funktion, um die Jahre aus einer Tabelle zu formatieren
def table_yearformat():

	# Liest die Tabellen und speichert sie in der Variablen tabellist
	tabellist = chip.read_tables()

	# Überprüft alle Tabellen und aktualisiert tabellist
	tabellist = chip.check_alltabels(tabellist)

	# Initialisiert eine temporäre Liste, um die Teile der Tabellen zu speichern
	temp_list = []

	# Durchläuft die Liste der Tabellen
	for i in range(len(tabellist)):
		
		# Teilt jede Tabelle bei "_" und fügt das Ergebnis der temp_list hinzu
		temp_list.append(tabellist[i].split("_"))

	# (Die folgende Zeile wurde auskommentiert, könnte aber verwendet werden, um die erste Zeile zu löschen)
	# del temp_list[0]

	# Initialisiert eine Liste, um die Jahre zu speichern
	year_list = []

	# Durchläuft die temporäre Liste
	for i in range(len(temp_list)):
		
		# Fügt das Jahr (zweites Element) jeder Tabelle zur year_list hinzu
		year_list.append(temp_list[i][1])

	# Entfernt Duplikate aus der Liste der Jahre, um nur eindeutige Jahre zu behalten
	year_list = list(set(year_list))

	# Sortiert die Liste der Jahre in aufsteigender Reihenfolge
	year_list.sort()

	# Gibt die formatierte Liste der Jahre zurück
	return(year_list)

# Funktion, um die Tabellen für einen bestimmten Monat abzurufen
def tabel_month(value):
	# Liste der korrekten Monatsnamen in englischer Sprache
	correct_month = ["January", "February", "March", "April", "Mai", "June", "July", "August", "September", "October", "November", "December"]

	# Liest die Tabellen und speichert sie in der Variablen tabellist
	tabellist = chip.read_tables()

	# Überprüft alle Tabellen und aktualisiert tabellist
	tabellist = chip.check_alltabels(tabellist)

	# Initialisiert eine Liste, um die Monate zu speichern, die mit dem gegebenen Wert übereinstimmen
	month_list = []

	# Initialisiert eine temporäre Liste, um die Teile der Tabellen zu speichern
	temp_list = []

	# Durchläuft die Liste der Tabellen
	for i in range(len(tabellist)):

		# Teilt jede Tabelle bei "_" und fügt das Ergebnis der temp_list hinzu
		temp_list.append(tabellist[i].split("_"))

	# Durchläuft die temporäre Liste
	for i in range(len(temp_list)):

		# Überprüft, ob der zweite Teil der Tabelle dem gegebenen Monat (value) entspricht
		if temp_list[i][1] == value:

			# Wenn ja, wird der erste Teil (Monat) zur month_list hinzugefügt
			month_list.append(temp_list[i][0])

	# Erstellt ein Dictionary zur Zuordnung von Monatsnamen zu ihren Indizes
	order_dict = {month: index for index, month in enumerate(correct_month)}

	# Sortiert die month_list basierend auf der Reihenfolge der Monate im order_dict
	month_list = sorted(month_list, key=lambda month: order_dict[month])

	# Gibt die sortierte Liste der Monate zurück
	return month_list

# Funktion zum Erstellen einer neuen Tabelle
def new_table(parent_window):

	# Überprüft, ob ein übergeordnetes Fenster vorhanden ist
	if parent_window:
		# Wenn ja, wird das übergeordnete Fenster geschlossen
		parent_window.destroy()

	# Erstellt ein neues Fenster (nt) für die neue Monatstabelle
	nt = tk.Tk()
	
	# Setzt den Titel des Fensters
	nt.title("New Month Table")

	# Konfiguriert das Fenster mit Hintergrundfarbe, Cursor und Reliefstil aus den Einstellungen
	nt.config(bg=chip.read_row("settings", "bg")[0], 
			  cursor=chip.read_row("settings", "cursor")[0], 
			  relief=chip.read_row("settings", "relief")[0])

	# Konfiguriert die Spalten des Fensters
	nt.columnconfigure(0, weight=1, minsize=150)  # Erste Spalte

	nt.columnconfigure(1, weight=1, minsize=150)  # Zweite Spalte

	nt.columnconfigure(2, weight=1, minsize=150)  # Dritte Spalte

	# Konfiguriert die Zeilen des Fensters
	nt.rowconfigure(1, weight=1)  # Erste Zeile

	nt.rowconfigure(2, weight=1)  # Zweite Zeile

	nt.rowconfigure(3, weight=1)  # Dritte Zeile

	nt.rowconfigure(4, weight=1)  # Vierte Zeile

	# Funktion zur Konfiguration des benutzerdefinierten Stils für Treeview-Widgets
	def custom_treeview_style():

		# Erstellt ein Style-Objekt für das ttk-Modul
		style = ttk.Style()

		# Konfiguriert den Hintergrund, die Schriftfarbe und den Font des Treeview
		style.configure("Custom.Treeview", 
						bg=chip.read_row("settings", "bg")[0], 
						fg=chip.read_row("settings", "fg")[0], 
						font=(chip.read_row("settings", "font")[0], 
							  int(chip.read_row("settings", "font_size")[0])), 
						fieldbackground=chip.read_row("settings", "bg")[0])

		# Konfiguriert den Stil des Combobox-Widgets
		style.configure("CustomCombobox.TCombobox", 
						bg=chip.read_row("settings", "bg")[0], 
						fg=chip.read_row("settings", "fg")[0], 
						font=(chip.read_row("settings", "font")[0], 
							  int(chip.read_row("settings", "font_size")[0])), 
						fieldbackground=chip.read_row("settings", "bg")[0])

		# Konfiguriert die Kopfzeilen des Treeview
		style.configure("Custom.Treeview.Heading", 
						background=chip.read_row("settings", "bg")[0], 
						foreground=chip.read_row("settings", "fg")[0], 
						font=(chip.read_row("settings", "font")[0], 
							  int(chip.read_row("settings", "font_size")[0])))

		# Mappt die Hintergrundfarbe für ausgewählte Zeilen
		style.map("Custom.Treeview.", 
				  background=[("selected", chip.read_row("settings", "activeforeground")[0])])

		# Mappt die Hintergrundfarbe der Kopfzeilen, wenn sie aktiv sind
		style.map("Custom.Treeview.Heading", 
				  background=[("active", chip.read_row("settings", "activebackground")[0])])

		return style

	# Ruft die Funktion zur Anpassung des Treeview-Stils auf
	custom_treeview_style()
	
	# Aktuellen Zeitpunkt abrufen
	hundred_value = datetime.datetime.now()

	# Jahr im Jahrhundertformat (z. B. 20 für 2020) im String-Format speichern
	hundred_value = hundred_value.strftime("%C")

	# Aktuellen Zeitpunkt erneut abrufen
	tenth_value = datetime.datetime.now()

	# Jahr im zweistelligen Format (z. B. 20 für 2020) im String-Format speichern
	tenth_value = tenth_value.strftime("%y")

	# StringVar für das Jahrhundertjahr erstellen und initialisieren
	hundred_var = tk.StringVar(value=hundred_value)

	# StringVar für das zweistellige Jahr erstellen und initialisieren
	tenth_var = tk.StringVar(value=tenth_value)

	# Aktuellen Monat abrufen
	month_name = datetime.datetime.now()
	
	# Monat im vollständigen Namen (z. B. "October") im String-Format speichern
	month_name = month_name.strftime("%B")

	# Spinbox für das Jahrhundertjahr (19 oder 20) erstellen
	hundred = tk.Spinbox(nt, from_=19, to=21, textvariable=hundred_var, wrap=True, 
					 font=(chip.read_row("settings", "font")[0], 
						   int(chip.read_row("settings", "font_size")[0])), 
					 fg=chip.read_row("settings", "fg")[0], 
					 bg=chip.read_row("settings", "bg")[0])

	# Konfiguration der Spinbox für das Jahrhundertjahr
	hundred.config(bd=int(chip.read_row("settings", "borderwidth")[0]), 
				cursor=chip.read_row("settings", "cursor")[0])

	# Spinbox für das zweistellige Jahr (0 bis 99) erstellen
	tenth = tk.Spinbox(nt, from_=0, to=99, textvariable=tenth_var, wrap=True, 
				   font=(chip.read_row("settings", "font")[0], 
						 int(chip.read_row("settings", "font_size")[0])), 
				   fg=chip.read_row("settings", "fg")[0], 
				   bg=chip.read_row("settings", "bg")[0])

	# Konfiguration der Spinbox für das zweistellige Jahr
	tenth.config(bd=int(chip.read_row("settings", "borderwidth")[0]), 
			   cursor=chip.read_row("settings", "cursor")[0])

	# StringVar für den Monat erstellen
	month = tk.StringVar()

	# Kombinationsfeld (Combobox) für die Monate erstellen
	month_box = ttk.Combobox(nt, textvariable=month, style="CustomCombobox.TCombobox")

	# Liste der Monate in die Combobox einfügen
	month_box["values"] = month_list

	# Setzt den aktuellen Monat in die Combobox
	month_box.set(month_name)
	
	def new_month_table():
	
		# Abrufen der Werte aus den Eingabefeldern
		hundredvalue = hundred.get()  # Jahrhundert (19 oder 20)
	
		tenthvalue = tenth.get()	  # Zweistelliges Jahr (0 bis 99)
		
		monthnow = month.get()		# Aktueller Monat aus der Combobox

		# Erstellen des Tabellennamens im Format "Monat_JahrHundert_Jahr"
		tablename = monthnow + "_" + hundredvalue + tenthvalue

		# Abrufen des Wertes aus dem Eingabefeld für "lohn"
		lohn_value = input_entry.get()

		# Überprüfen, ob das Eingabefeld leer ist
		if not lohn_value:
			
			# Fehlermeldung anzeigen, wenn kein Wert eingegeben wurde
			tk.messagebox.showerror('error', "No Input value")
			
			return  # Funktion beenden

		# Überprüfen, ob der eingegebene Wert eine gültige Zahl ist
		lohn_value = check_of_float(lohn_value)
		
		if not lohn_value:
		
			# Fehlermeldung anzeigen, wenn der Wert ungültig ist
			tk.messagebox.showerror("error", "Wrong Input")
			
			input_entry.delete(0, "end")  # Eingabefeld zurücksetzen
			
			return  # Funktion beenden

		# Überprüfen, ob eine Tabelle mit dem gegebenen Namen bereits existiert
		result = chip.pre_autotest(tablename, lohn_value)
		
		# print(result)  # (Kommentierte Zeile, um das Ergebnis zu debuggen)

		if result is None:
		
			# Fehlermeldung anzeigen, wenn eine falsche oder existierende Tabelle gefunden wurde
			tk.messagebox.showerror('error', "Wrong Date Table exist")
		
			input_entry.delete(0, "end")  # Eingabefeld zurücksetzen
			
			return  # Funktion beenden

		# Eingabefeld zurücksetzen, wenn alle Überprüfungen erfolgreich waren
		input_entry.delete(0, "end")
	
		return  # Funktion beenden
	
	# Erstellen eines Buttons für die Funktion "Neue Monatstabelle"
	new_month_table = tk.Button(nt, text="New Month Table", command=new_month_table)

	# Konfigurieren des Buttons mit Hintergrundfarbe, Schriftfarbe, Schriftart und anderen Eigenschaften
	new_month_table.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), 
	borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	relief=chip.read_row("settings", "relief")[0], 
	activebackground=chip.read_row("settings", "activebackground")[0], 
	cursor=chip.read_row("settings", "cursor")[0],
	highlightthickness=chip.read_row("settings", "highlightthickness")[0], 
	highlightbackground=chip.read_row("settings", "highlightbackground")[0], 
	activeforeground=chip.read_row("settings", "activeforeground")[0]
	)

	# Erstellen eines Eingabefelds für die Geldsumme
	input_entry = tk.Entry(nt)

	# Konfigurieren des Eingabefelds mit Hintergrundfarbe, Schriftfarbe, Schriftart und anderen Eigenschaften
	input_entry.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0])), 
	bd=int(chip.read_row("settings", "borderwidth")[0]), 
	relief=chip.read_row("settings", "relief")[0]
	)

	# Erstellen eines "Zurück"-Buttons, der zur Startansicht zurückführt
	back_button = tk.Button(nt, text="back", command=lambda: start_window(nt))

	# Konfigurieren des "Zurück"-Buttons mit den gleichen Einstellungen wie zuvor
	back_button.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), 
	borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	relief=chip.read_row("settings", "relief")[0], 
	activebackground=chip.read_row("settings", "activebackground")[0], 
	cursor=chip.read_row("settings", "cursor")[0],
	highlightthickness=chip.read_row("settings", "highlightthickness")[0], 
	highlightbackground=chip.read_row("settings", "highlightbackground")[0], 
	activeforeground=chip.read_row("settings", "activeforeground")[0]
	)

	# Erstellen eines "Schließen"-Buttons, der das Fenster schließt
	close_button = tk.Button(nt, text="close", command=nt.destroy)

	# Konfigurieren des "Schließen"-Buttons mit den gleichen Einstellungen wie zuvor
	close_button.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), 
	borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	relief=chip.read_row("settings", "relief")[0], 
	activebackground=chip.read_row("settings", "activebackground")[0], 
	cursor=chip.read_row("settings", "cursor")[0],
	highlightthickness=chip.read_row("settings", "highlightthickness")[0], 
	highlightbackground=chip.read_row("settings", "highlightbackground")[0], 
	activeforeground=chip.read_row("settings", "activeforeground")[0]
	)

	# Erstellen eines Labels für die Jahrhundertangabe
	hundred_label = tk.Label(nt, text="Hundred")

	# Konfigurieren des Labels mit den gleichen Einstellungen wie zuvor
	hundred_label.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), 
	borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	relief=chip.read_row("settings", "relief")[0], 
	activebackground=chip.read_row("settings", "activebackground")[0], 
	cursor=chip.read_row("settings", "cursor")[0],
	highlightthickness=chip.read_row("settings", "highlightthickness")[0], 
	highlightbackground=chip.read_row("settings", "highlightbackground")[0]
	)

	# Erstellen eines Labels für die Zehnerangabe
	tenth_label = tk.Label(nt, text="Tenth")

	# Konfigurieren des Labels mit den gleichen Einstellungen wie zuvor
	tenth_label.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), 
	borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	relief=chip.read_row("settings", "relief")[0], 
	activebackground=chip.read_row("settings", "activebackground")[0], 
	cursor=chip.read_row("settings", "cursor")[0],
	highlightthickness=chip.read_row("settings", "highlightthickness")[0], 
	highlightbackground=chip.read_row("settings", "highlightbackground")[0]
	)

	# Erstellen eines Labels für die Geldsumme
	input_label = tk.Label(nt, text="Money Input")

	# Konfigurieren des Labels mit den gleichen Einstellungen wie zuvor
	input_label.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), 
	borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	relief=chip.read_row("settings", "relief")[0], 
	activebackground=chip.read_row("settings", "activebackground")[0], 
	cursor=chip.read_row("settings", "cursor")[0],
	highlightthickness=chip.read_row("settings", "highlightthickness")[0], 
	highlightbackground=chip.read_row("settings", "highlightbackground")[0]
	)

	# Erstellen eines Labels für den Monat
	month_label = tk.Label(nt, text="Month")

	# Konfigurieren des Labels mit den gleichen Einstellungen wie zuvor
	month_label.config(
	bg=chip.read_row("settings", "bg")[0], 
	fg=chip.read_row("settings", "fg")[0], 
	font=(chip.read_row("settings", "font")[0], int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), 
	borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
	relief=chip.read_row("settings", "relief")[0], 
	activebackground=chip.read_row("settings", "activebackground")[0], 
	cursor=chip.read_row("settings", "cursor")[0],
	highlightthickness=chip.read_row("settings", "highlightthickness")[0], 
	highlightbackground=chip.read_row("settings", "highlightbackground")[0]
	)
	
	# Platzieren des "Hundert"-Labels in der ersten Zeile (0) und erster Spalte (0)
	# Die Optionen 'sticky', 'padx' und 'pady' sorgen für eine Anpassung der Größe und Abstände
	hundred_label.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

	# Platzieren des "Zehner"-Labels in der ersten Zeile (0) und zweiter Spalte (1)
	tenth_label.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

	# Platzieren des "Monat"-Labels in der ersten Zeile (0) und dritter Spalte (2)
	month_label.grid(column=2, row=0, sticky="nsew", padx=5, pady=5)

	# Platzieren des Widgets für "Hundert" in der zweiten Zeile (1) und erster Spalte (0)
	hundred.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

	# Platzieren des Widgets für "Zehner" in der zweiten Zeile (1) und zweiter Spalte (1)
	tenth.grid(column=1, row=1, sticky="nsew", padx=5, pady=5)

	# Platzieren des Monats-Auswahlfelds in der zweiten Zeile (1) und dritter Spalte (2)
	month_box.grid(column=2, row=1, sticky="nsew", padx=5, pady=5)

	# Platzieren des Labels für die Geldsumme in der dritten Zeile (2) und erster Spalte (0)
	input_label.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)

	# Platzieren des Eingabefelds für die Geldsumme in der vierten Zeile (3) und erster Spalte (0)
	input_entry.grid(column=0, row=3, sticky="nesw", padx=5, pady=5)

	# Platzieren des Buttons für die neue Monatstabelle in der vierten Zeile (3) und zweiter Spalte (1)
	new_month_table.grid(column=1, row=3, sticky="nsew", padx=5, pady=5)

	# Platzieren des "Zurück"-Buttons in der fünften Zeile (4) und erster Spalte (0)
	back_button.grid(column=0, row=4, sticky="nsew", padx=5, pady=5)

	# Platzieren des "Schließen"-Buttons in der fünften Zeile (4) und zweiter Spalte (1)
	close_button.grid(column=1, row=4, sticky="nsew", padx=5, pady=5)

	# Starten der Tkinter-Ereignisschleife, um das Fenster anzuzeigen und Interaktionen zu ermöglichen
	nt.mainloop()

	# Rückgabe, um die Funktion zu beenden (optional, je nach Kontext)
	return

# Funktion zum Starten eines neuen Fensters
def start_window(parent_window):

	# Überprüfen, ob ein übergeordnetes Fenster existiert
	if parent_window:

		# Wenn ja, das übergeordnete Fenster schließen
		parent_window.destroy()

	# Erstellen der Datenbanktabellen durch einen Aufruf an die chip-Instanz
	chip.make_db_tabels()

	# Erstellen eines neuen Tkinter-Fensters
	fc = tk.Tk()

	try:
		# Versuchen, ein Icon für das Fenster zu setzen
		icon = PhotoImage(file="Unbenannt.png")  # Laden des Icons aus einer Datei

		fc.iconphoto(True, icon)  # Setzen des Icons für das Fenster

	except Exception as e:

		# Fehlerbehandlung, wenn das Laden des Icons fehlschlägt (z.B. wenn die Datei nicht gefunden wird)
		pass

	# Setzen des Titels für das Fenster
	fc.title("Money Coin")

	# Konfigurieren des Fensters mit den aus der chip-Instanz gelesenen Einstellungen
	fc.config(bg=chip.read_row("settings", "bg")[0],  # Hintergrundfarbe
			  cursor=chip.read_row("settings", "cursor")[0],  # Cursorstil
			  relief=chip.read_row("settings", "relief")[0])  # Rahmenstil

	# Konfigurieren der Spalten und Zeilen im Tkinter-Fenster 'fc'

	# Spalte 0 konfigurieren: 
	# Gewicht 1 bedeutet, dass die Spalte bei Bedarf wachsen kann, 
	# und die minimale Größe der Spalte wird auf 150 Pixel gesetzt.
	fc.columnconfigure(0, weight=1, minsize=150)

	# Konfigurieren der Zeilen 1 bis 9:
	# Jede Zeile erhält ein Gewicht von 1, was bedeutet, 
	# dass sie proportional zum verfügbaren Platz wachsen kann.
	fc.rowconfigure(1, weight=1)  # Zeile 1 konfigurieren
	
	fc.rowconfigure(2, weight=1)  # Zeile 2 konfigurieren
	
	fc.rowconfigure(3, weight=1)  # Zeile 3 konfigurieren
	
	fc.rowconfigure(4, weight=1)  # Zeile 4 konfigurieren
	
	fc.rowconfigure(5, weight=1)  # Zeile 5 konfigurieren
	
	fc.rowconfigure(6, weight=1)  # Zeile 6 konfigurieren
	
	fc.rowconfigure(7, weight=1)  # Zeile 7 konfigurieren
	
	fc.rowconfigure(8, weight=1)  # Zeile 8 konfigurieren
	
	fc.rowconfigure(9, weight=1)  # Zeile 9 konfigurieren
	
	# Erstellen einer Schaltfläche "Monatsauswahl und Übersicht"
	overview = tk.Button(fc, text="Monatsauswahl und übersicht", command=lambda: month_view.month_overview(fc))

	# Konfigurieren der Schaltfläche mit Hintergrundfarbe, Schriftfarbe, Schriftart und weiteren Eigenschaften
	overview.config(bg=chip.read_row("settings", "bg")[0],   # Hintergrundfarbe
				fg=chip.read_row("settings", "fg")[0],   # Schriftfarbe
				font=(chip.read_row("settings", "font")[0],  # Schriftart
					  int(chip.read_row("settings", "font_size")[0]),  # Schriftgröße
					  chip.read_row("settings", "font_style")[0]),  # Schriftstil
				borderwidth=int(chip.read_row("settings", "borderwidth")[0]),  # Breite des Rahmens
				relief=chip.read_row("settings", "relief")[0],  # Reliefstil
				activebackground=chip.read_row("settings", "activebackground")[0],  # Hintergrundfarbe im aktiven Zustand
				cursor=chip.read_row("settings", "cursor")[0],  # Mauszeigerstil
				highlightthickness=chip.read_row("settings", "highlightthickness")[0],  # Dicke des Hervorhebungsrahmens
				highlightbackground=chip.read_row("settings", "highlightbackground")[0],  # Hintergrundfarbe des Hervorhebungsrahmens
				activeforeground=chip.read_row("settings", "activeforeground")[0])  # Schriftfarbe im aktiven Zustand

	# Erstellen einer Schaltfläche "New Month Table"
	new_month = tk.Button(fc, text="New Month Table", command=lambda: new_table(fc))

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften wie zuvor
	new_month.config(bg=chip.read_row("settings", "bg")[0],
				 fg=chip.read_row("settings", "fg")[0],
				 font=(chip.read_row("settings", "font")[0],
					   int(chip.read_row("settings", "font_size")[0]),
					   chip.read_row("settings", "font_style")[0]),
				 borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
				 relief=chip.read_row("settings", "relief")[0],
				 activebackground=chip.read_row("settings", "activebackground")[0],
				 cursor=chip.read_row("settings", "cursor")[0],
				 highlightthickness=chip.read_row("settings", "highlightthickness")[0],
				 highlightbackground=chip.read_row("settings", "highlightbackground")[0],
				 activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Money Time"
	money_time = tk.Button(fc, text="Money Time", command=lambda: month_view.money_timetable(fc))

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	money_time.config(bg=chip.read_row("settings", "bg")[0],
				  fg=chip.read_row("settings", "fg")[0],
				  font=(chip.read_row("settings", "font")[0],
						int(chip.read_row("settings", "font_size")[0]),
						chip.read_row("settings", "font_style")[0]),
				  borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
				  relief=chip.read_row("settings", "relief")[0],
				  activebackground=chip.read_row("settings", "activebackground")[0],
				  cursor=chip.read_row("settings", "cursor")[0],
				  highlightthickness=chip.read_row("settings", "highlightthickness")[0],
				  highlightbackground=chip.read_row("settings", "highlightbackground")[0],
				  activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Reserve money View"
	reserve_bar = tk.Button(fc, text="Reserve money View", command=lambda: month_view.reserve_window(fc))

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	reserve_bar.config(bg=chip.read_row("settings", "bg")[0],
				   fg=chip.read_row("settings", "fg")[0],
				   font=(chip.read_row("settings", "font")[0],
						 int(chip.read_row("settings", "font_size")[0]),
						 chip.read_row("settings", "font_style")[0]),
				   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
				   relief=chip.read_row("settings", "relief")[0],
				   activebackground=chip.read_row("settings", "activebackground")[0],
				   cursor=chip.read_row("settings", "cursor")[0],
				   highlightthickness=chip.read_row("settings", "highlightthickness")[0],
				   highlightbackground=chip.read_row("settings", "highlightbackground")[0],
				   activeforeground=chip.read_row("settings", "activeforeground")[0])
	
	# Erstellen einer Schaltfläche "New Reserve Table"
	new_reserve = tk.Button(fc, text="New Reserve Table", command=lambda: month_view.reserve_newtable(fc))
	
	# Konfigurieren der Schaltfläche mit Hintergrundfarbe, Schriftfarbe, Schriftart und weiteren Eigenschaften
	new_reserve.config(bg=chip.read_row("settings", "bg")[0],   # Hintergrundfarbe
				   fg=chip.read_row("settings", "fg")[0],   # Schriftfarbe
				   font=(chip.read_row("settings", "font")[0],  # Schriftart
						 int(chip.read_row("settings", "font_size")[0]),  # Schriftgröße
						 chip.read_row("settings", "font_style")[0]),  # Schriftstil
				   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),  # Breite des Rahmens
				   relief=chip.read_row("settings", "relief")[0],  # Reliefstil
				   activebackground=chip.read_row("settings", "activebackground")[0],  # Hintergrundfarbe im aktiven Zustand
				   cursor=chip.read_row("settings", "cursor")[0],  # Mauszeigerstil
				   highlightthickness=chip.read_row("settings", "highlightthickness")[0],  # Dicke des Hervorhebungsrahmens
				   highlightbackground=chip.read_row("settings", "highlightbackground")[0],  # Hintergrundfarbe des Hervorhebungsrahmens
				   activeforeground=chip.read_row("settings", "activeforeground")[0])  # Schriftfarbe im aktiven Zustand

	# Erstellen einer Schaltfläche "Statistic"
	statistics = tk.Button(fc, text="Statistic", command=lambda: month_view.plot_overview(fc))
	
	# Konfigurieren der Schaltfläche mit denselben Eigenschaften wie zuvor
	statistics.config(bg=chip.read_row("settings", "bg")[0],
				  fg=chip.read_row("settings", "fg")[0],
				  font=(chip.read_row("settings", "font")[0],
						int(chip.read_row("settings", "font_size")[0]),
						chip.read_row("settings", "font_style")[0]),
				  borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
				  relief=chip.read_row("settings", "relief")[0],
				  activebackground=chip.read_row("settings", "activebackground")[0],
				  cursor=chip.read_row("settings", "cursor")[0],
				  highlightthickness=chip.read_row("settings", "highlightthickness")[0],
				  highlightbackground=chip.read_row("settings", "highlightbackground")[0],
				  activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Settings"
	settings_button = tk.Button(fc, text="Settings", command=lambda: month_view.settings(fc))
	
	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	settings_button.config(bg=chip.read_row("settings", "bg")[0],
					   fg=chip.read_row("settings", "fg")[0],
					   font=(chip.read_row("settings", "font")[0],
							 int(chip.read_row("settings", "font_size")[0]),
							 chip.read_row("settings", "font_style")[0]),
					   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
					   relief=chip.read_row("settings", "relief")[0],
					   activebackground=chip.read_row("settings", "activebackground")[0],
					   cursor=chip.read_row("settings", "cursor")[0],
					   highlightthickness=chip.read_row("settings", "highlightthickness")[0],
					   highlightbackground=chip.read_row("settings", "highlightbackground")[0],
					   activeforeground=chip.read_row("settings", "activeforeground")[0])
	
	# Erstellen einer Schaltfläche "Delete Table"
	delte_table = tk.Button(fc, text="Delete Table", command=lambda: month_view.delete_window(fc))
	
	# Konfigurieren der Schaltfläche mit Hintergrundfarbe, Schriftfarbe, Schriftart und weiteren Eigenschaften
	delte_table.config(bg=chip.read_row("settings", "bg")[0],   # Hintergrundfarbe
				   fg=chip.read_row("settings", "fg")[0],   # Schriftfarbe
				   font=(chip.read_row("settings", "font")[0],  # Schriftart
						 int(chip.read_row("settings", "font_size")[0]),  # Schriftgröße
						 chip.read_row("settings", "font_style")[0]),  # Schriftstil
				   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),  # Breite des Rahmens
				   relief=chip.read_row("settings", "relief")[0],  # Reliefstil
				   activebackground=chip.read_row("settings", "activebackground")[0],  # Hintergrundfarbe im aktiven Zustand
				   cursor=chip.read_row("settings", "cursor")[0],  # Mauszeigerstil
				   highlightthickness=chip.read_row("settings", "highlightthickness")[0],  # Dicke des Hervorhebungsrahmens
				   highlightbackground=chip.read_row("settings", "highlightbackground")[0],  # Hintergrundfarbe des Hervorhebungsrahmens
				   activeforeground=chip.read_row("settings", "activeforeground")[0])  # Schriftfarbe im aktiven Zustand

	# Erstellen einer Schaltfläche "Help"
	help_button = tk.Button(fc, text="Help", command=lambda: month_view.help_window(fc))

	# Konfigurieren der Schaltfläche mit denselben Eigenschaften wie zuvor
	help_button.config(bg=chip.read_row("settings", "bg")[0],
				   fg=chip.read_row("settings", "fg")[0],
				   font=(chip.read_row("settings", "font")[0],
						 int(chip.read_row("settings", "font_size")[0]),
						 chip.read_row("settings", "font_style")[0]),
				   borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
				   relief=chip.read_row("settings", "relief")[0],
				   activebackground=chip.read_row("settings", "activebackground")[0],
				   cursor=chip.read_row("settings", "cursor")[0],
				   highlightthickness=chip.read_row("settings", "highlightthickness")[0],
				   highlightbackground=chip.read_row("settings", "highlightbackground")[0],
				   activeforeground=chip.read_row("settings", "activeforeground")[0])

	# Erstellen einer Schaltfläche "Close"
	close_button = tk.Button(fc, text="close", command=fc.destroy)
	
	# Konfigurieren der Schaltfläche mit denselben Eigenschaften
	close_button.config(bg=chip.read_row("settings", "bg")[0],
					fg=chip.read_row("settings", "fg")[0],
					font=(chip.read_row("settings", "font")[0],
						  int(chip.read_row("settings", "font_size")[0]),
						  chip.read_row("settings", "font_style")[0]),
					borderwidth=int(chip.read_row("settings", "borderwidth")[0]),
					relief=chip.read_row("settings", "relief")[0],
					activebackground=chip.read_row("settings", "activebackground")[0],
					cursor=chip.read_row("settings", "cursor")[0],
					highlightthickness=chip.read_row("settings", "highlightthickness")[0],
					highlightbackground=chip.read_row("settings", "highlightbackground")[0],
					activeforeground=chip.read_row("settings", "activeforeground")[0])
	
	# Platzieren der Schaltfläche "Monatsauswahl und Übersicht" im Grid
	overview.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)  # Bei (0,0) positioniert, mit Padding

	# Platzieren der Schaltfläche "New Month Table" im Grid
	new_month.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)  # Bei (0,1) positioniert, mit Padding

	# Platzieren der Schaltfläche "Money Time" im Grid
	money_time.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)  # Bei (0,2) positioniert, mit Padding

	# Platzieren der Schaltfläche "Reserve money View" im Grid
	reserve_bar.grid(column=0, row=3, sticky="nsew", padx=5, pady=5)  # Bei (0,3) positioniert, mit Padding

	# Platzieren der Schaltfläche "New Reserve Table" im Grid
	new_reserve.grid(column=0, row=4, sticky="nsew", padx=5, pady=5)  # Bei (0,4) positioniert, mit Padding

	# Platzieren der Schaltfläche "Statistic" im Grid
	statistics.grid(column=0, row=5, sticky="nsew", padx=5, pady=5)  # Bei (0,5) positioniert, mit Padding

	# Platzieren der Schaltfläche "Delete Table" im Grid
	delte_table.grid(column=0, row=6, sticky="nsew", padx=5, pady=5)  # Bei (0,6) positioniert, mit Padding

	# Platzieren der Schaltfläche "Settings" im Grid
	settings_button.grid(column=0, row=7, sticky="nsew", padx=5, pady=5)  # Bei (0,7) positioniert, mit Padding

	# Platzieren der Schaltfläche "Help" im Grid
	help_button.grid(column=0, row=8, sticky="nsew", padx=5, pady=5)  # Bei (0,8) positioniert, mit Padding

	# Platzieren der Schaltfläche "Close" im Grid
	close_button.grid(column=0, row=9, sticky="nsew", padx=5, pady=5)  # Bei (0,9) positioniert, mit Padding

	# Starten der Hauptanwendungsschleife von Tkinter
	fc.mainloop()

	# Rückgabe von der Funktion (da es keine Rückgabewerte gibt, ist dies optional)
	return







