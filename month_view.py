import tkinter as tk

from tkinter import ttk

from tkinter import *

from tkinter import colorchooser

import datetime

# import Pillow

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

import Finanz_Coin

import chip

month_list = ["January", "February", "March", "April", "Mai", "June", "July", "August", "September", "October", "November", "December"]

# format year from table
def table_yearformat():

	tabellist = chip.read_tables()

	tabellist = chip.check_alltabels(tabellist)

	temp_list = []

	for i in range(len(tabellist)):

		temp_list.append(tabellist[i].split("_"))

	year_list = []

	for i in range(len(temp_list)):

		year_list.append(temp_list[i][1])

	year_list = list(set(year_list))

	year_list.sort()

	return year_list

def check_of_float(value):

	try:

		if "," in value:

			value = value.replace(",", ".")

		value = float(value)

		return value

	except ValueError:

		return None

	return

# month table
def month_overview(parent_window):

	if parent_window:

		parent_window.destroy()

	mo = tk.Tk()

	mo.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	mo.title("Month Overview")

	mo.columnconfigure(0, weight = 1, minsize = 150)

	mo.columnconfigure(1, weight = 1, minsize = 150)

	mo.rowconfigure(1, weight = 1)

	mo.rowconfigure(2, weight = 2) # tree

	mo.rowconfigure(3, weight = 1)

	mo.rowconfigure(4, weight = 1)

	mo.rowconfigure(5, weight = 1)

	mo.rowconfigure(6, weight = 1)

	mo.rowconfigure(7, weight = 1)

	def custom_treeview_style():

		style = ttk.Style()

		style.configure("Custom.Treeview", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("CustomCombobox.TCombobox", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("Custom.Treeview.Heading", background = chip.read_row("settings", "bg")[0], foreground = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])))

		style.map("Custom.Treeview.", background = [("selected", chip.read_row("settings", "activeforeground")[0])] )

		style.map("Custom.Treeview.Heading", background = [("active", chip.read_row("settings", "activebackground")[0])])

		return style

	custom_treeview_style()

	back_button = tk.Button(mo, text = "back", command = lambda: Finanz_Coin.start_window(mo))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(mo, text = "close", command = mo.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	# update table tree
	def update_money_tree(table):

		for item in table_tree.get_children():

			table_tree.delete(item)

		#work

		money_tabletime = chip.read_dbtable(table)

		for y in range(len(money_tabletime)):

			table_tree.insert("", tk.END, values=[ money_tabletime[y][0], money_tabletime[y][1], money_tabletime[y][2]])

		return

	year_list = tk.StringVar()

	def select_month(event):

		for item in table_tree.get_children():

			table_tree.delete(item)

		month = month_box.get()

		year = year_box.get()

		get_table = chip.read_dbtable(month + "_" + year)

		for y in range(len(get_table)):

			table_tree.insert("", tk.END, values=[get_table[y][0], get_table[y][1], get_table[y][2]])

		return

	def select_year(event):

		actual_tables = Finanz_Coin.tabel_month(year_box.get())

		month_box.configure(values=actual_tables)

		month_box.set(actual_tables[0])

		select_month(None)

		return

	outgo_text = tk.Entry(mo)

	outgo_text.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), bd = int(chip.read_row("settings", "borderwidth")[0]), relief = chip.read_row("settings", "relief")[0])

	sume_entry = tk.Entry(mo)

	sume_entry.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), bd = int(chip.read_row("settings", "borderwidth")[0]), relief = chip.read_row("settings", "relief")[0])

	def clear_entry():

		outgo_text.delete(0, "end")

		sume_entry.delete(0, "end")

		return

	def item_selection(event=None):

		try:

			clear_entry()

			item = table_tree.item(table_tree.selection())

			item = item["values"]

			outgo_text.insert(0, item[1])

			sume_entry.insert(0, item[2])

		except:

			return

		return

	

	year_box = ttk.Combobox(mo, style = "CustomCombobox.TCombobox")

	year_box.bind("<<ComboboxSelected>>", select_year)

	year_box["values"] = Finanz_Coin.table_yearformat()

	month_name = datetime.datetime.now()

	month_name = month_name.strftime("%B")

	current_month = tk.StringVar()

	month_box = ttk.Combobox(mo, textvariable = current_month, style = "CustomCombobox.TCombobox")

	month_box.bind("<<ComboboxSelected>>", select_month)

	table_tree = ttk.Treeview(mo, columns = ("id", "outgo", "sume"), show = "headings", style = "Custom.Treeview")

	table_tree.bind("<<TreeviewSelect>>", item_selection)

	table_tree.heading("id", text = "ID")

	table_tree.heading("outgo", text = "Outgo")

	table_tree.heading("sume", text = "Sume")

	table_tree.column("id", width = 0, minwidth = 0, stretch = False)

	def add_line():

		month = month_box.get()

		year = year_box.get()

		if not month or not year:

			tk.messagebox.showerror("error", "No Selection")

			clear_entry()

			return
			
		if month > "0" and year != "0":

			outgo_line = outgo_text.get()

			sume_line = sume_entry.get()

			if not outgo_line:

				tk.messagebox.showerror("error", "No Outgo Text")

				clear_entry()

				return

			if not sume_line:

				tk.messagebox.showerror("error", "No Outgo Value")

				clear_entry()

				return

			result = check_of_float(sume_line)

			#print("result ", result)

			if not result:

				tk.messagebox.showerror("error", "Wrong Sume Value")

				clear_entry()

				return

			table_name = month + "_" + year

		chip.add_newtableline_resttill_end(table_name, [outgo_line, result])



		update_money_tree(f"{month}_{year}")

		clear_entry()

		return

	add_button = tk.Button(mo, text="Add", command=add_line)

	add_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	# delete db line
	def delete_line():

		month = month_box.get()

		year = year_box.get()

		item = table_tree.item(table_tree.selection())

		if not item["values"] or len(item["values"]) == 0:

			tk.messagebox.showerror("error", "No Selection")

			return

		else:

			line = item["values"][0]

		# print(line)

		table_name = month + "_" + year

		chip.delete_monthline_rest_tillfutur(table_name, line)

		update_money_tree(table_name)

		clear_entry()

		return

	delete_button = tk.Button(mo, text="Delete", command=delete_line)

	delete_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	def refresh_value():

		month = month_box.get()

		year = year_box.get()

		table_name = month + "_" + year

		item = table_tree.item(table_tree.selection())

		item = item["values"]

		outgo_line = outgo_text.get()

		sume_line = sume_entry.get()

		if not outgo_line:

			tk.messagebox.showerror("error", "No Outgo Text")

			clear_entry()

			return

		if not sume_line:

			tk.messagebox.showerror("error", "No Sume Value")

			clear_entry()

			return

		result = check_of_float(sume_line)

		chip.change_monthline_rest_tillfutur(table_name, [item[0], outgo_line, result])

		update_money_tree(table_name)

		clear_entry()

		return

	refresh_button = tk.Button(mo, text="Change", command=refresh_value)

	refresh_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	outgo_label = tk.Label(mo, text = "Outgo Text")

	outgo_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	sume_label = tk.Label(mo, text = "Sume Value")

	sume_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	year_label = tk.Label(mo, text = "Year")

	year_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	month_label = tk.Label(mo, text = "Month")

	month_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	year_label.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	month_label.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

	month_box.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

	year_box.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	table_tree.grid(column = 0, row = 2, columnspan = 2, sticky = "nsew", padx = 5, pady = 5)

	outgo_label.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	sume_label.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	outgo_text.grid(column = 0, row = 4, sticky = "nsew", padx = 5, pady = 5)

	sume_entry.grid(column = 1, row = 4, sticky = "nsew", padx = 5, pady = 5)

	add_button.grid(column = 0, row = 5, sticky = "nsew", padx = 5, pady = 5)

	delete_button.grid(column = 1, row = 6, sticky = "nsew", padx = 5, pady = 5)

	refresh_button.grid(column = 0, row = 6, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 7, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 1, row = 7, sticky = "nsew", padx = 5, pady = 5)

	mo.mainloop()

	return

	

#month_overview(None)
#########################################################################################
#
#
#
# primary table with date an cyclon ####################################################
def money_timetable(parent_window):
	#work
	#terz
	if parent_window:

		parent_window.destroy()

	mt = tk.Tk()

	mt.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	mt.title("Money Time")

	mt.columnconfigure(0, weight = 1, minsize = 150)

	mt.columnconfigure(1, weight = 1, minsize = 150)

	mt.columnconfigure(2, weight = 1, minsize = 150)

	mt.rowconfigure(1, weight = 3) # tree

	mt.rowconfigure(2, weight = 1)

	mt.rowconfigure(3, weight = 1)

	mt.rowconfigure(4, weight = 1)

	mt.rowconfigure(5, weight = 1)

	mt.rowconfigure(6, weight = 1)

	mt.rowconfigure(7, weight = 1)

	times = ["Month", "Quart", "Terz", "Year"]

	length = chip.read_moneytimetable()

	length = len(length)

	def custom_treeview_style():

		style = ttk.Style()

		style.configure("Custom.Treeview", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("CustomCombobox.TCombobox", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("Custom.Treeview.Heading", background = chip.read_row("settings", "bg")[0], foreground = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])))

		style.map("Custom.Treeview.", background = [("selected", chip.read_row("settings", "activeforeground")[0])] )

		style.map("Custom.Treeview.Heading", background = [("active", chip.read_row("settings", "activebackground")[0])])

		return style


	custom_treeview_style()

	money_tree = ttk.Treeview(mt, columns=("id", "outgo", "sume", "time", "end"), show="headings", style = "Custom.Treeview")#, height = length)

	money_tree.heading("id", text="ID")

	money_tree.heading("outgo", text="Outgo")

	money_tree.heading("sume", text="Sume")

	money_tree.heading("time", text="Time")

	money_tree.heading("end", text="end time")

	money_tree.column("id", width = 0, minwidth = 0, stretch = False)

	year_box = tk.Spinbox(mt, from_ = 1900, to = 2300, wrap = True, font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fg = chip.read_row("settings", "fg")[0], bg = chip.read_row("settings", "bg")[0])

	year_box.config(bd = int(chip.read_row("settings", "borderwidth")[0]), cursor = chip.read_row("settings", "cursor")[0])	

	year_box.delete(0, "end")

	year_box.insert(0, datetime.datetime.now().strftime("%Y"))

	month_box = tk.Spinbox(mt, from_ = 1, to = 12, wrap = True, font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fg = chip.read_row("settings", "fg")[0], bg = chip.read_row("settings", "bg")[0])

	month_box.config(bd = int(chip.read_row("settings", "borderwidth")[0]), cursor = chip.read_row("settings", "cursor")[0])

	month_box.delete(0, "end")

	month_box.insert(0, datetime.datetime.now().strftime("%m"))

	quart_box = tk.Spinbox(mt, from_ = 1, to = 3, wrap = True, font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fg = chip.read_row("settings", "fg")[0], bg = chip.read_row("settings", "bg")[0])

	quart_box.delete(0, "end")

	quart_box.config(bd = int(chip.read_row("settings", "borderwidth")[0]), cursor = chip.read_row("settings", "cursor")[0])

	quart_box.insert(0, 1)

	terz_box = tk.Spinbox(mt, from_ = 1, to = 3, wrap = True, font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fg = chip.read_row("settings", "fg")[0], bg = chip.read_row("settings", "bg")[0])

	terz_box.delete(0, "end")

	terz_box.config(bd = int(chip.read_row("settings", "borderwidth")[0]), cursor = chip.read_row("settings", "cursor")[0])

	terz_box.insert(0, 1)

	def check_endtime():

		if end_time_var.get() == True:

			quart_box.config(state = "disabled")

			month_box.config(state = "normal")

			year_box.config(state = "normal")

		if end_time_var.get() == False:

			quart_box.config(state = "normal")

		return

	end_time_var = tk.IntVar()

	check_yearend = tk.Checkbutton(mt, text = "End Time", variable = end_time_var, command = check_endtime)

	check_yearend.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	def make_time():

		if time_box.get().lower() == "month" and end_time_var.get() == False:

			time_list = [time_box.get().lower(), "none"]

		elif time_box.get().lower() == "month" and end_time_var.get() == True:

			time_list = [time_box.get().lower(), str(year_box.get() + "." + str(month_box.get()))]

		elif time_box.get().lower() == "quart":

			if str(quart_box.get()) == "1":

				time_list = [time_box.get().lower(), "none"]

			else:

				time_list = [time_box.get().lower() + "." + str(quart_box.get()), "none"]

		elif time_box.get().lower() == "year":

			time_list = [time_box.get().lower() + "." + str(int(month_box.get())), "none"]

		elif time_box.get().lower() == "terz":

			time_list = [time_box.get().lower() + "." + str(terz_box.get()), "none"]

		return time_list

	def update_money_tree():

		for item in money_tree.get_children():

			money_tree.delete(item)

		money_tabletime = chip.read_moneytimetable()

		for y in range(len(money_tabletime)):

			money_tree.insert("", tk.END, values=[ money_tabletime[y][0], money_tabletime[y][1], money_tabletime[y][2], money_tabletime[y][3], money_tabletime[y][4]])

		return

	def delete_entrys():

		outgo_entry.delete(0, "end")

		sume_entry.delete(0, "end")

		return

	update_money_tree()

	outgo_entry = tk.Entry(mt, width = 20)

	outgo_entry.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), bd = int(chip.read_row("settings", "borderwidth")[0]), relief = chip.read_row("settings", "relief")[0])

	sume_entry = tk.Entry(mt, width = 20)

	sume_entry.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), bd = int(chip.read_row("settings", "borderwidth")[0]), relief = chip.read_row("settings", "relief")[0])

	def time_selected(event):

		if time_box.get().lower() == "month":

			year_box.config(state = "disabled")

			month_box.config(state = "disabled")

			quart_box.config(state = "disabled")

			terz_box.config(state = "disabled")

		elif time_box.get().lower() == "quart":

			year_box.config(state = "disabled")

			month_box.config(state = "disabled")

			quart_box.config(state = "normal")

			terz_box.config(state = "disabled")

		elif time_box.get().lower() == "year":

			year_box.config(state = "normal")

			month_box.config(state = "normal")

			quart_box.config(state = "disabled")

			terz_box.config(state = "disabled")

		elif time_box.get().lower() == "terz":

			year_box.config(state = "disabled")

			month_box.config(state = "disabled")

			quart_box.config(state = "disabled")

			terz_box.config(state = "normal")

		return

	time_box = ttk.Combobox(mt, value = times, style = "CustomCombobox.TCombobox")

	time_box.set(times[0])

	time_box.bind("<<ComboboxSelected>>", time_selected)

	end_time_var.set(False)

	year_label = tk.Label(mt, text = "Year")

	year_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	month_label = tk.Label(mt, text = "Month")

	month_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	quart_label = tk.Label(mt, text = "Quart Selection")

	quart_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	terz_label = tk.Label(mt, text = "Terz Selection")

	terz_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	# add entry to table
	def add_moneytime():

		select_values = make_time()

		outgo = outgo_entry.get()

		sume = sume_entry.get()

		sume = check_of_float(sume)

		# print(sume)

		if not outgo:

			tk.messagebox.showerror("error", "No Outgo Text")

			delete_entrys()

			return

		if not sume:

			tk.messagebox.showerror("error", "No Sume Value")

			delete_entrys()

			return

		chip.add_moneytimerowchangetable([outgo, sume, select_values[0], select_values[1]])

		delete_entrys()

		update_money_tree()

		return

	add_button = tk.Button(mt, text = "Add", command = add_moneytime)

	add_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	# get selected item
	def item_selection(event):

		delete_entrys()

		try:

			item = money_tree.item(money_tree.selection())

			item = item["values"]

			#print(item)

			outgo_entry.insert(0, item[1])

			sume_entry.insert(0, item[2])

			#time_entry.insert(0, item[3])

			if "." in item[3]:

				#print(".")

				if "quart" in item[3]:

					time_box.set(item[3].split(".")[0])

					quart_box.delete(0, "end")

					quart_box.insert(0, item[3].split(".")[1])

				else:

					#print(item[3])

					time_box.delete(0, "end")

					time_box.set(item[3].split(".")[0])

					month_box.delete(0, "end")

					month_box.insert(0, item[3].split(".")[1])

			if "." in item[4]:

				var = item[4].split(".")

				time_box.set(item[3])

				year_box.delete(0, "end")

				year_box.insert(0, var[0])

				month_box.delete(0, "end")

				month_box.insert(0, var[1])

			if not "." in item[4] and not "." in item[3]:

				month_box.delete(0, "end")

				year_box.delete(0, "end")

				time_box.set(item[3])

			endtime_enty.insert(0, item[4])

		except:

			pass

		return

	# change line in db
	def change_line():

		item = money_tree.item(money_tree.selection())

		item = item["values"]

		item_id = item[0]

		outgo = outgo_entry.get()

		sume = sume_entry.get()

		sume = check_of_float(sume)

		select_values = make_time()

		if not outgo:

			tk.messagebox.showerror("error", "No Outgo Text")

			delete_entrys()

			return

		if not sume:

			tk.messagebox.showerror("error", "No Sume Value")

			delete_entrys()

			return

		chip.change_moneytime_tableyear([item_id, outgo, sume, select_values[0], select_values[1]])

		update_money_tree()

		year_box.delete(0, "end")

		year_box.insert(0, datetime.datetime.now().strftime("%Y"))

		month_box.delete(0, "end")

		month_box.insert(0, datetime.datetime.now().strftime("%m"))

		delete_entrys()

		return

	change_button = tk.Button(mt, text="Change", command=change_line)

	change_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	money_tree.bind("<<TreeviewSelect>>", item_selection)

	# delete line in table
	def delete_moneyfrequency():

		item = money_tree.item(money_tree.selection())

		# print(item)

		if not item["values"] or len(item["values"]) == 0:

			tk.messagebox.showerror("error", "No Selection")

			return

		else:

			line = item["values"]

		# print(line)

		chip.money_timedeleteline("money_time", line)

		update_money_tree()

		return

	outgo_label = tk.Label(mt, text = "Outgo Text")

	outgo_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	sume_label = tk.Label(mt, text = "Sume Value")

	sume_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	time_label = tk.Label(mt, text = "How often repeat")

	time_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	endtime_label = tk.Label(mt, text = "Time ends repeat")

	endtime_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	delete_button = tk.Button(mt, text="Delete", command=delete_moneyfrequency)

	delete_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])


	back_button = tk.Button(mt, text="back", command=lambda: Finanz_Coin.start_window(mt))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])


	close_button = tk.Button(mt, text="close", command = mt.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])


	money_tree.grid(column = 0, row = 0, columnspan = 4, sticky = "nsew", padx = 10, pady = 10)

	outgo_label.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	sume_label.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

	time_label.grid(column = 2, row = 1, sticky = "nsew", padx = 5, pady = 5)

	endtime_label.grid(column = 3, row = 1, sticky = "nsew", padx = 5, pady = 5)

	outgo_entry.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady = 5)

	sume_entry.grid(column = 1, row = 2, sticky = "nsew", padx = 5, pady = 5)

	add_button.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	change_button.grid(column = 0, row = 4, sticky="nsew", padx = 5, pady = 5)

	time_box.grid(column = 2, row = 2, sticky = "nsew", padx = 5, pady = 5)

	check_yearend.grid(column = 3, row = 2, sticky = "nsew", padx = 5, pady = 5)

	year_label.grid(column = 2, row = 3, sticky = "nsew", padx = 5, pady = 5)

	year_box.grid(column = 2, row = 4, sticky = "nsew", padx = 5, pady = 5)

	month_label.grid(column = 3, row = 3, sticky = "nsew", padx = 5, pady = 5)

	month_box.grid(column = 3, row = 4, sticky = "nsew", padx = 5, pady = 5)

	quart_label.grid(column = 2, row = 5, sticky = "nsew", padx = 5, pady = 5)

	terz_label.grid(column = 3, row = 5, sticky = "nsew", padx = 5, pady = 5)

	quart_box.grid(column = 2, row = 6, sticky = "nsew", padx = 5, pady = 5)

	terz_box.grid(column = 3, row = 6, sticky = "nsew", padx = 5, pady = 5)

	delete_button.grid(column = 0, row = 5, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 7, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 2, row = 7, sticky = "nsew", padx = 5, pady = 5)

	mt.mainloop()

	return
#money_timetable(None)
# delete window to delete tabels
def delete_window(parent_window):

	if parent_window:

		parent_window.destroy()

	dt = tk.Tk()

	dt.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	dt.title("Delete Table")

	dt.columnconfigure(0, weight = 1, minsize = 150)

	dt.columnconfigure(1, weight = 1, minsize = 150)

	dt.rowconfigure(1, weight = 1)

	dt.rowconfigure(2, weight = 1)

	dt.rowconfigure(3, weight = 1)

	def custom_treeview_style():

		style = ttk.Style()

		style.configure("Custom.Treeview", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("CustomCombobox.TCombobox", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("Custom.Treeview.Heading", background = chip.read_row("settings", "bg")[0], foreground = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])))

		style.map("Custom.Treeview.", background = [("selected", chip.read_row("settings", "activeforeground")[0])] )

		style.map("Custom.Treeview.Heading", background = [("active", chip.read_row("settings", "activebackground")[0])])

		return style

	custom_treeview_style()

	def update_year():

		year_box["values"] = Finanz_Coin.table_yearformat()

		return

	def select_month(event):

		month = month_box.get()

		year = year_box.get()

		return

	def select_year(event):

		actual_tables = Finanz_Coin.tabel_month(year_box.get())

		month_box.configure(values=actual_tables)

		month_box.set(actual_tables[0])

		select_month(None)

		return

	def delte_table():
		
		month = month_box.get()

		year = year_box.get()

		if year:

			delete_value = str(month) + "_" + str(year)

			chip.delete_table(delete_value)

			# print(delete_value)

			chip.delete_yearsume(delete_value)

			month_box.set("")

			year_box.set("")

			update_year()

		else:

			tk.messagebox.showerror("error", "No Selection")

			month_box.set("")

			year_box.set("")

			return

		return

	year_box = ttk.Combobox(dt, style = "CustomCombobox.TCombobox")

	year_box.bind("<<ComboboxSelected>>", select_year)

	year_box["values"] = Finanz_Coin.table_yearformat()

	month_name = datetime.datetime.now()

	month_name = month_name.strftime("%B")

	current_month = tk.StringVar()

	month_box = ttk.Combobox(dt, textvariable=current_month, style = "CustomCombobox.TCombobox")

	month_box.bind("<<ComboboxSelected>>", select_month)

	delete_button = tk.Button(dt, text="Delete Table", command=delte_table)

	delete_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	back_button = tk.Button(dt, text="back", command=lambda: Finanz_Coin.start_window(dt))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(dt, text="close", command = dt.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	year_label = tk.Label(dt, text = "Year")

	year_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	month_label = tk.Label(dt, text = "Month")

	month_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	year_label.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	month_label.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

	year_box.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	month_box.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

	delete_button.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	dt.mainloop()

	return

def reserve_window(parent_window):

	if parent_window:

		parent_window.destroy()

	rw = tk.Tk()

	rw.title("Reserve Money")

	rw.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	rw.columnconfigure(0, weight = 1, minsize = 150)

	rw.columnconfigure(1, weight = 1, minsize = 150)

	rw.columnconfigure(2, weight = 1, minsize = 150)

	rw.rowconfigure(1, weight = 1)

	rw.rowconfigure(2, weight = 1)

	rw.rowconfigure(3, weight = 1)

	rw.rowconfigure(4, weight = 1)

	rw.rowconfigure(5, weight = 1)

	rw.rowconfigure(6, weight = 1)

	def custom_treeview_style():

		style = ttk.Style()

		style.configure("Custom.Treeview", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("CustomCombobox.TCombobox", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("Custom.Treeview.Heading", background = chip.read_row("settings", "bg")[0], foreground = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])))

		style.map("Custom.Treeview.", background = [("selected", chip.read_row("settings", "activeforeground")[0])] )

		style.map("Custom.Treeview.Heading", background = [("active", chip.read_row("settings", "activebackground")[0])])

		return style


	custom_treeview_style()

	reserve_tree = ttk.Treeview(rw, columns = ("id", "outgo", "sume"), show = "headings", style = "Custom.Treeview")

	reserve_tree.heading("id", text = "ID")

	reserve_tree.heading("outgo", text = "Outgo")

	reserve_tree.heading("sume", text = "Sume")

	reserve_tree.column("id", width = 0, minwidth = 0, stretch = False)

	def delete_entrys():

		outgo_entry.delete(0, "end")

		sume_entry.delete(0, "end")

		return

	def deselect_item():

		reserve_tree.selection_remove(reserve_tree.selection())

		return

	# update table tree
	def update_money_tree(table):

		delete_entrys()

		deselect_item()

		for item in reserve_tree.get_children():

			reserve_tree.delete(item)

		chip.get_reservevalues(table)

		money_tabletime = chip.read_dbtable(table)

		for y in range(len(money_tabletime)):

			reserve_tree.insert("", tk.END, values = [ money_tabletime[y][0], money_tabletime[y][1], money_tabletime[y][2]])

		return

	def select_year(event):

		delete_entrys()

		deselect_item()

		actual_tables = year_box.get()

		update_money_tree(actual_tables)

		return

	def add_value():

		if not year_box.get():

			tk.messagebox.showerror("error", "No Year Selection")

			delete_entrys()

			return

		if not outgo_entry.get() or not sume_entry.get():

			tk.messagebox.showerror("error", "No Entry")

			delete_entrys()

			return

		actual_tables = year_box.get()

		chip.check_dblastline(actual_tables)

		sume_line = check_of_float(sume_line)

		if not sume_line:

			tk.messagebox.showerror("error", "No Entry")

			delete_entrys()

			return

		chip.update_dbrowline(actual_tables, [outgo_entry.get(), sume_line])

		chip.make_reserve_sume(actual_tables)

		update_money_tree(actual_tables)

		return

	def change_line():

		item = reserve_tree.item(reserve_tree.selection())

		if not year_box.get():

			tk.messagebox.showerror("error", "No Year Selection")

			delete_entrys()

			return

		if not item["values"] or len(item["values"]) == 0:

			tk.messagebox.showerror("error", "No Entry Selection")

			delete_entrys()

			return

		reverse_dict = chip.reverse_dic()

		table_list = chip.check_reservetable_change(year_box.get())

		item = item["values"]

		# print(item)

		for i in table_list:

			if item[1] in i or item[1] == "rest":

				tk.messagebox.showerror("error", "Wrong Selection")

				delete_entrys()

				deselect_item()

				return

		sume_line = check_entry()

		chip.update_dbline(year_box.get(), [item[0], outgo_entry.get(), sume_line])

		chip.make_reserve_sume(year_box.get())

		update_money_tree(year_box.get())

		return

	def delete_line():

		if not year_box.get():

			tk.messagebox.showerror("error", "No Year Selection")

			delete_entrys()

		item = reserve_tree.item(reserve_tree.selection())

		if not item["values"] or len(item["values"]) == 0:

			tk.messagebox.showerror("error", "No Entry Selection")

			delete_entrys()

		reverse_dict = chip.reverse_dic()

		table_list = chip.check_reservetable_change(year_box.get())

		item = item["values"]

		for i in table_list:

			if item[1] in i or item[1] == "rest":

				tk.messagebox.showerror("error", "Wrong Selection")

				delete_entrys()

				deselect_item()

				return

		chip.delete_dbline(year_box.get(), item[0])

		chip.make_reserve_sume(year_box.get())

		update_money_tree(year_box.get())

		return

	def item_selection(event):

		delete_entrys()

		try:

			item = reserve_tree.item(reserve_tree.selection())

			item = item["values"]

			outgo_entry.insert(0, item[1])

			sume_entry.insert(0, item[2])

		except:

			return

		return

	year_box = ttk.Combobox(rw, style = "CustomCombobox.TCombobox")

	year_box.bind("<<ComboboxSelected>>", select_year)

	year_box["values"] = chip.read_reservetables()

	add_button = tk.Button(rw, text = "Add Value", command = add_value)

	add_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	change_button = tk.Button(rw, text = "Change", command = change_line)

	change_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	delete_button = tk.Button(rw, text = "Delete", command = delete_line)

	delete_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	outgo_entry = tk.Entry(rw)

	outgo_entry.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), bd = int(chip.read_row("settings", "borderwidth")[0]), relief = chip.read_row("settings", "relief")[0])

	sume_entry = tk.Entry(rw)

	sume_entry.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), bd = int(chip.read_row("settings", "borderwidth")[0]), relief = chip.read_row("settings", "relief")[0])

	reserve_tree.bind("<<TreeviewSelect>>", item_selection)

	back_button = tk.Button(rw, text = "Back", command = lambda: Finanz_Coin.start_window(rw))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(rw, text = "Close", command = rw.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	year_label = tk.Label(rw, text = "Year")

	year_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	outgo_text = tk.Label(rw, text = "Outgo Name")

	outgo_text.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	value_label = tk.Label(rw, text = "Outgo Value")

	value_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	year_label.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	year_box.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	reserve_tree.grid(column = 0, row = 2, columnspan = 5, sticky = "nsew", padx = 5, pady = 5)

	outgo_text.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	value_label.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	outgo_entry.grid(column = 0, row = 4, sticky = "nsew",padx = 5, pady = 5)

	sume_entry.grid(column = 1, row = 4, sticky = "nsew", padx = 5, pady = 5)

	add_button.grid(column = 0, row = 5, sticky = "nsew", padx = 5, pady = 5)

	change_button.grid(column = 1, row = 5, sticky = "nsew", padx = 5, pady = 5)

	delete_button.grid(column = 2, row = 5, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 6, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 1, row = 6, sticky = "nsew", padx = 5, pady = 5)

	rw.mainloop()

	return

#reserve_window(None)

def reserve_newtable(parent_window):

	if parent_window:

		parent_window.destroy()

	nr = tk.Tk()

	nr.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	nr.title("New Reserve Table")

	nr.columnconfigure(0, weight = 1, minsize = 150)

	nr.columnconfigure(1, weight = 1, minsize = 150)

	nr.rowconfigure(1, weight = 1)

	nr.rowconfigure(2, weight = 1)

	nr.rowconfigure(3, weight = 1)

	nr.rowconfigure(4, weight = 1)

	nr.rowconfigure(5, weight = 1)

	hundred_value = datetime.datetime.now()

	hundred_value = hundred_value.strftime("%C")

	tenth_value = datetime.datetime.now()

	tenth_value = tenth_value.strftime("%y")

	hundred_var = tk.StringVar(value = hundred_value)

	tenth_var = tk.StringVar(value = tenth_value)

	hundred = tk.Spinbox(nr, from_= 19, to = 21, textvariable = hundred_var, wrap = True, font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fg = chip.read_row("settings", "fg")[0], bg = chip.read_row("settings", "bg")[0])

	hundred.config(bd = int(chip.read_row("settings", "borderwidth")[0]), cursor = chip.read_row("settings", "cursor")[0])	

	tenth = tk.Spinbox(nr, from_ = 0, to = 99, textvariable = tenth_var, wrap = True, font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fg = chip.read_row("settings", "fg")[0], bg = chip.read_row("settings", "bg")[0])

	tenth.config(bd = int(chip.read_row("settings", "borderwidth")[0]), cursor = chip.read_row("settings", "cursor")[0])	

	def reserve_table():

		hundredvalue = hundred.get()

		tenthvalue = tenth.get()

		tablename = "Reserve" + "_" + hundredvalue + tenthvalue

		if chip.table_exist(tablename) != None:

			tk.messagebox.showerror("error", "Wrong Year")

			tenth.delete(0, "end")

			tenth.insert(0, tenth_value)

			hundred.delete(0, "end")

			hundred.insert(0, hundred_value)

		else:

			chip.new_monthtable(tablename)

		return

	new_month_table = tk.Button(nr, text = "New Reserve Table", command = reserve_table)

	new_month_table.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	back_button = tk.Button(nr, text = "back", command = lambda: Finanz_Coin.start_window(nr))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(nr, text = "close", command = nr.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	hundred_label = tk.Label(nr, text = "Hundred")

	hundred_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	tenth_label = tk.Label(nr, text = "Tenth")

	tenth_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	hundred_label.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	tenth_label.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

	hundred.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady = 5)

	tenth.grid(column = 1, row = 2, sticky = "nsew", padx = 5, pady = 5)

	new_month_table.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 4, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 1, row = 4, sticky = "nsew", padx = 5, pady = 5)

	nr.mainloop()

	return


plot_marker = {
	"Circle": "o",
	"Star": "*",
	"Point": ".",
	"X": "x",
	"X filled": "X",
	"Plus": "+",
	"Plus filled": "P",
	"Square": "s",
	"Diamond": "D",
	"Diamond thin": "d",
	"Pentagon": "p",
	"Hexagon": "H",
	"Triangel down": "v",
	"Triangel up": "^",
	"Triangel left": "<",
	"Triangel right": ">",
	"Tri down": "1",
	"Tri up": "2",
	"Tri left": "3",
	"Tri right": "4",
	"Vline": "|",
	"Hline": "_",
}

plot_linestyle = {"Solid": "-", "Dotted": ":", "Dashed": "--", "Dash Dot": "-."}

plot_linecolor = {
	"AliceBlue": "#F0F8FF",
	"AntiqueWhite": "#FAEBD7",
	"Aqua": "#00FFFF",
	"Aquamarine": "#7FFFD4",
	"Azure": "#F0FFFF",
	"Beige": "#F5F5DC",
	"Bisque": "#FFE4C4",
	"Black": "#000000",
	"BlanchedAlmond": "#FFEBCD",
	"Blue": "#0000FF",
	"BlueViolet": "#8A2BE2",
	"Brown": "#A52A2A",
	"BurlyWood": "#DEB887",
	"CadetBlue": "#5F9EA0",
	"Chartreuse": "#7FFF00",
	"Chocolate": "#D2691E",
	"Coral": "#FF7F50",
	"CornflowerBlue": "#6495ED",
	"Cornsilk": "#FFF8DC",
	"Crimson": "#DC143C",
	"Cyan": "#00FFFF",
	"DarkBlue": "#00008B",
	"DarkCyan": "#008B8B",
	"DarkGoldenRod": "#B8860B",
	"DarkGray": "#A9A9A9",
	"DarkGrey": "#A9A9A9",
	"DarkGreen": "#006400",
	"DarkKhaki": "#BDB76B",
	"DarkMagenta": "#8B008B",
	"DarkOliveGreen": "#556B2F",
	"DarkOrange": "#FF8C00",
	"DarkOrchid": "#9932CC",
	"DarkRed": "#8B0000",
	"DarkSalmon": "#E9967A",
	"DarkSeaGreen": "#8FBC8F",
	"DarkSlateBlue": "#483D8B",
	"DarkSlateGray": "#2F4F4F",
	"DarkSlateGrey": "#2F4F4F",
	"DarkTurquoise": "#00CED1",
	"DarkViolet": "#9400D3",
	"DeepPink": "#FF1493",
	"DeepSkyBlue": "#00BFFF",
	"DimGray": "#696969",
	"DimGrey": "#696969",
	"DodgerBlue": "#1E90FF",
	"FireBrick": "#B22222",
	"FloralWhite": "#FFFAF0",
	"ForestGreen": "#228B22",
	"Fuchsia": "#FF00FF",
	"Gainsboro": "#DCDCDC",
	"GhostWhite": "#F8F8FF",
	"Gold": "#FFD700",
	"GoldenRod": "#DAA520",
	"Gray": "#808080",
	"Grey": "#808080",
	"Green": "#008000",
	"GreenYellow": "#ADFF2F",
	"HoneyDew": "#F0FFF0",
	"HotPink": "#FF69B4",
	"IndianRed": "#CD5C5C",
	"Indigo": "#4B0082",
	"Ivory": "#FFFFF0",
	"Khaki": "#F0E68C",
	"Lavender": "#E6E6FA",
	"LavenderBlush": "#FFF0F5",
	"LawnGreen": "#7CFC00",
	"LemonChiffon": "#FFFACD",
	"LightBlue": "#ADD8E6",
	"LightCoral": "#F08080",
	"LightCyan": "#E0FFFF",
	"LightGoldenRodYellow": "#FAFAD2",
	"LightGray": "#D3D3D3",
	"LightGrey": "#D3D3D3",
	"LightGreen": "#90EE90",
	"LightPink": "#FFB6C1",
	"LightSalmon": "#FFA07A",
	"LightSeaGreen": "#20B2AA",
	"LightSkyBlue": "#87CEFA",
	"LightSlateGray": "#778899",
	"LightSlateGrey": "#778899",
	"LightSteelBlue": "#B0C4DE",
	"LightYellow": "#FFFFE0",
	"Lime": "#00FF00",
	"LimeGreen": "#32CD32",
	"Linen": "#FAF0E6",
	"Magenta": "#FF00FF",
	"Maroon": "#800000",
	"MediumAquaMarine": "#66CDAA",
	"MediumBlue": "#0000CD",
	"MediumOrchid": "#BA55D3",
	"MediumPurple": "#9370DB",
	"MediumSeaGreen": "#3CB371",
	"MediumSlateBlue": "#7B68EE",
	"MediumSpringGreen": "#00FA9A",
	"MediumTurquoise": "#48D1CC",
	"MediumVioletRed": "#C71585",
	"MidnightBlue": "#191970",
	"MintCream": "#F5FFFA",
	"MistyRose": "#FFE4E1",
	"Moccasin": "#FFE4B5",
	"NavajoWhite": "#FFDEAD",
	"Navy": "#000080",
	"OldLace": "#FDF5E6",
	"Olive": "#808000",
	"OliveDrab": "#6B8E23",
	"Orange": "#FFA500",
	"OrangeRed": "#FF4500",
	"Orchid": "#DA70D6",
	"PaleGoldenRod": "#EEE8AA",
	"PaleGreen": "#98FB98",
	"PaleTurquoise": "#AFEEEE",
	"PaleVioletRed": "#DB7093",
	"PapayaWhip": "#FFEFD5",
	"PeachPuff": "#FFDAB9",
	"Peru": "#CD853F",
	"Pink": "#FFC0CB",
	"Plum": "#DDA0DD",
	"PowderBlue": "#B0E0E6",
	"Purple": "#800080",
	"RebeccaPurple": "#663399",
	"Red": "#FF0000",
	"RosyBrown": "#BC8F8F",
	"RoyalBlue": "#4169E1",
	"SaddleBrown": "#8B4513",
	"Salmon": "#FA8072",
	"SandyBrown": "#F4A460",
	"SeaGreen": "#2E8B57",
	"SeaShell": "#FFF5EE",
	"Sienna": "#A0522D",
	"Silver": "#C0C0C0",
	"SkyBlue": "#87CEEB",
	"SlateBlue": "#6A5ACD",
	"SlateGray": "#708090",
	"SlateGrey": "#708090",
	"Snow": "#FFFAFA",
	"SpringGreen": "#00FF7F",
	"SteelBlue": "#4682B4",
	"Tan": "#D2B48C",
	"Teal": "#008080",
	"Thistle": "#D8BFD8",
	"Tomato": "#FF6347",
	"Turquoise": "#40E0D0",
	"Violet": "#EE82EE",
	"Wheat": "#F5DEB3",
	"White": "#FFFFFF",
	"WhiteSmoke": "#F5F5F5",
	"Yellow": "#FFFF00",
	"YellowGreen": "#9ACD32",
}

def plot_overview(parent_window):

	if parent_window:

		parent_window.destroy()

	po = tk.Tk()

	po.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	po.title("Plot Overview")

	po.columnconfigure(0, weight = 1, minsize = 150)

	po.rowconfigure(1, weight = 1)

	po.rowconfigure(2, weight = 1)

	po.rowconfigure(3, weight = 1)

	po.rowconfigure(4, weight = 1)

	year_button = tk.Button(po, text = "Year Plot", command = lambda: year_plot(po))

	year_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	month_button = tk.Button(po, text = "Month Plot", command = lambda: month_plot(po))

	month_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	reserve_button = tk.Button(po, text = "Reserve Plot", command = lambda: reserve_plot(po))

	reserve_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	back_button = tk.Button(po, text = "back", command = lambda: Finanz_Coin.start_window(po))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(po, text = "close", command = po.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	month_button.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)

	year_button.grid(row = 1,column = 0, sticky = "nsew", padx = 5, pady = 5)

	reserve_button.grid(row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(row = 3,column = 0, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(row = 4,column = 0, sticky = "nsew", padx = 5, pady = 5)

	po.mainloop()

	return

def month_plot(parent_window):

	if parent_window:

		parent_window.destroy()

	mp = tk.Tk()

	mp.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	mp.title("Month Statistic")

	mp.columnconfigure(0, weight = 1, minsize = 150)

	mp.columnconfigure(1, weight = 1, minsize = 150)

	mp.columnconfigure(3, weight = 1, minsize = 150)

	mp.columnconfigure(4, weight = 1, minsize = 150)

	mp.rowconfigure(0, weight = 1)

	mp.rowconfigure(1, weight = 1)

	mp.rowconfigure(2, weight = 1)#, minsize = 350)

	mp.rowconfigure(3, weight = 1)

	mp.rowconfigure(4, weight = 1)

	def custom_treeview_style():

		style = ttk.Style()

		style.configure("Custom.Treeview", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("CustomCombobox.TCombobox", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("Custom.Treeview.Heading", background = chip.read_row("settings", "bg")[0], foreground = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])))

		style.map("Custom.Treeview.", background = [("selected", chip.read_row("settings", "activeforeground")[0])] )

		style.map("Custom.Treeview.Heading", background = [("active", chip.read_row("settings", "activebackground")[0])])

		return style

	custom_treeview_style()

	frame = tk.Frame(mp)

	back_button = tk.Button(mp, text = "back", command = lambda: plot_overview(mp))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(mp, text = "close", command = mp.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	main_window = tk.Button(mp, text = "Main Window", command = lambda: Finanz_Coin.start_window(mp))

	main_window.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	def dic_tolist(dic):

		new_list = []

		for i in dic.keys():

			new_list.append(i)

		return new_list

	def make_xvalues(value):

		new_list = []

		for i in value:

			new_list.append(i[1])

		return new_list

	def make_yvalues(value):

		new_list = []

		for i in value:

			new_list.append(i[2])

		return new_list

	def update_plot():

		actual_tables = table_box.get()

		if not actual_tables:

			return

		plot_values = chip.read_dbtable(actual_tables)

		plot_values = chip.make_list(plot_values)

		x_value = make_xvalues(plot_values)

		y_value = make_yvalues(plot_values)

		fig, ax = plt.subplots(figsize = (10,6))

		if line_var.get():

			ax.plot(x_value, y_value, marker = plot_marker[marker_box.get()], linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label = "Einamen, Ausgaben")

			ax.grid(grid_var.get())

			plt.legend()

			plt.xticks(rotation = 45, ha = "right")

			plt.subplots_adjust(bottom = 0.3)

		elif pie_var.get():

			total = sum(y_value)

			percentages = [value / total * 100 for value in y_value]

			legend_labels = [f"{label}: {pct:.1f}%" for label, pct in zip(x_value, percentages)]

			wedges, autotexts = ax.pie(y_value, labels = None, startangle = 90)

			ax.legend(wedges, legend_labels, title = "Categories", loc = "center right", bbox_to_anchor = (0, 0, 0, 1))

		elif bar_var.get():

			ax.bar( x_value, y_value, linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label = "Einamen, Ausgaben")

			ax.grid(grid_var.get())

			plt.xticks(rotation = 45, ha = "right")

			plt.legend()

			plt.subplots_adjust(bottom = 0.3)

		canvas = FigureCanvasTkAgg(fig, master=frame)

		canvas.draw()

		canvas.get_tk_widget().grid(column = 0, row = 2, columnspan = 4, sticky = "nsew")

		plt.close(fig)

		return

	def select_year(event):

		update_plot()

		return

	def pie_check():

		bar_var.set(False)

		line_var.set(False)

		linestyle_box.config(state = "disabled")

		marker_box.config(state = "disabled")

		linecolor_box.config(state = "disabled")

		grid_box.config(state = "disabled")

		update_plot()

		return

	def line_check():

		bar_var.set(False)

		pie_var.set(False)

		linestyle_box.config(state = "normal")

		marker_box.config(state = "normal")

		linecolor_box.config(state = "normal")

		grid_box.config(state = "normal")

		update_plot()

		return

	def bar_check():

		line_var.set(False)

		pie_var.set(False)

		marker_box.config(state = "disabled")

		linestyle_box.config(state = "disabled")

		linecolor_box.config(state = "normal")

		grid_box.config(state = "normal")

		update_plot()

		return

	def select_linestyle(event):

		update_plot()

		return

	def marker_style(event):

		update_plot()

		return

	def line_style(event):

		update_plot()

		return

	def grid_style():

		update_plot()

		return

	table_box = ttk.Combobox(mp, style = "CustomCombobox.TCombobox")

	table_box.bind("<<ComboboxSelected>>", select_year)

	new_list = chip.read_tables()

	table_box["values"] = chip.check_alltabels(new_list)

	linestyle_box = ttk.Combobox(mp, style = "CustomCombobox.TCombobox")

	marker_box = ttk.Combobox(mp, style = "CustomCombobox.TCombobox")

	linecolor_box = ttk.Combobox(mp, style = "CustomCombobox.TCombobox")

	marker_box.bind("<<ComboboxSelected>>", marker_style)

	linestyle_box["values"] = dic_tolist(plot_linestyle)

	linestyle_box.bind("<<ComboboxSelected>>", select_linestyle)

	linestyle_box.set(dic_tolist(plot_linestyle)[0])

	marker_box["values"] = dic_tolist(plot_marker)

	marker_box.set(dic_tolist(plot_marker)[0])

	linecolor_box["values"] = dic_tolist(plot_linecolor)

	linecolor_box.set(dic_tolist(plot_linecolor)[7])

	linecolor_box.bind("<<ComboboxSelected>>", line_style)

	grid_var = tk.IntVar()

	grid_box = tk.Checkbutton(mp, text = "Grid", variable = grid_var, command = grid_style)

	grid_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	grid_var.set(True)

	line_var = tk.IntVar()

	line_box = tk.Checkbutton(mp, text = "Line", variable = line_var, command = line_check)

	line_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	bar_var = tk.IntVar()

	bar_box = tk.Checkbutton(mp, text = "Bar", variable = bar_var, command = bar_check)

	bar_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	pie_var = tk.IntVar()

	pie_box = tk.Checkbutton(mp, text = "Pie", variable = pie_var, command = pie_check)

	pie_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	line_var.set(True)

	bar_var.set(False)

	pie_var.set(False)

	plottable_label = tk.Label(mp, text = "Year")

	plottable_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	linestyle_label = tk.Label(mp, text = "Linestyle")

	linestyle_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	marker_label = tk.Label(mp, text = "Marker Style")

	marker_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	linecolor_label = tk.Label(mp, text = "Line Color")

	linecolor_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	plottable_label.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	table_box.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	linestyle_label.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

	linestyle_box.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

	marker_label.grid(column = 2, row = 0, sticky = "nsew", padx = 5, pady = 5)

	marker_box.grid(column = 2, row = 1, sticky = "nsew", padx = 5, pady = 5)

	linecolor_label.grid(column = 3, row = 0, sticky = "nsew", padx = 5, pady = 5)

	linecolor_box.grid(column = 3, row = 1, sticky = "nsew", padx = 5, pady = 5)

	frame.grid(column = 0, row = 2, columnspan = 4)#, sticky = "nsew", padx = 5, pady = 5)

	line_box.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	bar_box.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	pie_box.grid(column = 2, row = 3, sticky = "nsew", padx = 5, pady = 5)

	grid_box.grid(column = 3, row = 3, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 4, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 1, row = 4, sticky = "nsew", padx = 5, pady = 5)

	main_window.grid(column = 2, row = 4, sticky = "nsew", padx = 5, pady = 5)

	mp.mainloop()

	return

def year_plot(parent_window):

	if parent_window:

		parent_window.destroy()

	yp = tk.Tk()

	yp.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	yp.title("Year Statistic")

	yp.columnconfigure(0, weight = 1, minsize = 150)

	yp.columnconfigure(1, weight = 1, minsize = 150)

	yp.columnconfigure(3, weight = 1, minsize = 150)

	yp.columnconfigure(4, weight = 1, minsize = 150)

	yp.rowconfigure(0, weight = 1)

	yp.rowconfigure(1, weight = 1)

	yp.rowconfigure(2, weight = 1)#, minsize = 350)

	yp.rowconfigure(3, weight = 1)

	yp.rowconfigure(4, weight = 1)

	def custom_treeview_style():

		style = ttk.Style()

		style.configure("Custom.Treeview", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("CustomCombobox.TCombobox", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("Custom.Treeview.Heading", background = chip.read_row("settings", "bg")[0], foreground = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])))

		style.map("Custom.Treeview.", background = [("selected", chip.read_row("settings", "activeforeground")[0])] )

		style.map("Custom.Treeview.Heading", background = [("active", chip.read_row("settings", "activebackground")[0])])

		return style

	custom_treeview_style()

	frame = tk.Frame(yp)

	back_button = tk.Button(yp, text = "back", command = lambda: plot_overview(yp))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(yp, text = "close", command = yp.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	main_window = tk.Button(yp, text = "Main Window", command = lambda: Finanz_Coin.start_window(yp))

	main_window.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	def dic_tolist(dic):

		new_list = []

		for i in dic.keys():

			new_list.append(i)

		return new_list

	def make_xvalues(value):

		new_list = []

		for i in value:

			temp = [float(i[1][2]), float(i[2][2])]

			new_list.append(temp)

			# new_list.append(temp)

		# print(new_list)

		return new_list

	def make_yvalues(value):

		new_list = []

		for i in value:

			new_list.append(i[0])

		# print(new_list)

		return new_list

	def update_plot():

		actual_tables = table_box.get()

		if not actual_tables:

			return

		plot_values = chip.make_yearplot(actual_tables)

		# plot_values = chip.make_list(plot_values)

		x_value = make_xvalues(plot_values)

		# print("x", x_value)

		y_value = make_yvalues(plot_values)

		# print("y", y_value)

		fig, ax = plt.subplots()

		fig, ax = plt.subplots(figsize = (10,6))

		if line_var.get():
			# ax.plot(y_value, [v[0] for v in x_value], marker = plot_marker[marker_box.get()], linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get())

			ax.plot(y_value, [v[0] for v in x_value], marker = plot_marker[marker_box.get()], linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label="Einnahmen")

			ax.plot(y_value, [v[1] for v in x_value], marker = plot_marker[marker_box.get()], linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label="Rest")

			ax.grid(grid_var.get())

			plt.legend()

			plt.xticks(rotation = 45, ha = "right")

			plt.subplots_adjust(bottom = 0.3)

			#ax.legend()

		elif pie_var.get():

			total_income = sum([v[0] for v in x_value])

			total_expense = sum([v[1] for v in x_value])

			ax.pie( [total_income, total_expense], autopct = "%1.1f%%", labels = ["Einnahmen", "Ausgaben"])  # color = plot_linecolor[linecolor_box.get()])

			plt.legend()

		elif bar_var.get():

			months = np.arange(len(y_value))

			width = 0.35

			ax.bar( months - width / 2, [v[0] for v in x_value], width, linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label = "Einnahmen")

			ax.bar( months + width / 2, [v[1] for v in x_value], width, linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label = "Rest")

			ax.set_xticks(months)

			ax.set_xticklabels(y_value)

			plt.subplots_adjust(bottom = 0.3)

			plt.legend()

			ax.grid(grid_var.get())

			#ax.legend()

			plt.xticks(rotation = 45, ha = "right")

		canvas = FigureCanvasTkAgg(fig, master = frame)

		canvas.draw()

		canvas.get_tk_widget().grid(column = 0, row = 2, columnspan = 4, sticky = "nsew")

		plt.close(fig)

		return

	def select_year(event):

		update_plot()

		return

	def pie_check():

		bar_var.set(False)

		line_var.set(False)

		linestyle_box.config(state = "disabled")

		marker_box.config(state = "disabled")

		linecolor_box.config(state = "disabled")

		grid_box.config(state = "disabled")

		update_plot()

		return

	def line_check():

		bar_var.set(False)

		pie_var.set(False)

		linestyle_box.config(state = "normal")

		marker_box.config(state = "normal")

		linecolor_box.config(state = "normal")

		grid_box.config(state = "normal")

		update_plot()

		return

	def bar_check():

		line_var.set(False)

		pie_var.set(False)

		marker_box.config(state = "disabled")

		linestyle_box.config(state = "disabled")

		linecolor_box.config(state = "normal")

		grid_box.config(state = "normal")

		update_plot()

		return

	def select_linestyle(event):

		update_plot()

		return

	def marker_style(event):

		update_plot()

		return

	def line_style(event):

		update_plot()

		return

	def grid_style():

		update_plot()

		return

	table_box = ttk.Combobox(yp, style = "CustomCombobox.TCombobox")

	table_box.bind("<<ComboboxSelected>>", select_year)

	table_box["values"] = table_yearformat()

	linestyle_box = ttk.Combobox(yp, style = "CustomCombobox.TCombobox")

	marker_box = ttk.Combobox(yp, style = "CustomCombobox.TCombobox")

	linecolor_box = ttk.Combobox(yp, style = "CustomCombobox.TCombobox")

	marker_box.bind("<<ComboboxSelected>>", marker_style)

	linestyle_box["values"] = dic_tolist(plot_linestyle)

	linestyle_box.bind("<<ComboboxSelected>>", select_linestyle)

	linestyle_box.set(dic_tolist(plot_linestyle)[0])

	marker_box["values"] = dic_tolist(plot_marker)

	marker_box.set(dic_tolist(plot_marker)[0])

	linecolor_box["values"] = dic_tolist(plot_linecolor)

	linecolor_box.set(dic_tolist(plot_linecolor)[7])

	linecolor_box.bind("<<ComboboxSelected>>", line_style)

	grid_var = tk.IntVar()

	grid_box = tk.Checkbutton(yp, text = "Grid", variable = grid_var, command = grid_style)

	grid_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	grid_var.set(True)

	line_var = tk.IntVar()

	line_box = tk.Checkbutton(yp, text = "Line", variable = line_var, command = line_check)

	line_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	bar_var = tk.IntVar()

	bar_box = tk.Checkbutton(yp, text = "Bar", variable = bar_var, command = bar_check)

	bar_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	pie_var = tk.IntVar()

	pie_box = tk.Checkbutton(yp, text = "Pie", variable = pie_var, command = pie_check)

	pie_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	line_var.set(True)

	bar_var.set(False)

	pie_var.set(False)

	plottable_label = tk.Label(yp, text = "Year")

	plottable_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	linestyle_label = tk.Label(yp, text = "Linestyle")

	linestyle_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	marker_label = tk.Label(yp, text = "Marker Style")

	marker_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	linecolor_label = tk.Label(yp, text = "Line Color")

	linecolor_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	plottable_label.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	table_box.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	linestyle_label.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

	linestyle_box.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

	marker_label.grid(column = 2, row = 0, sticky = "nsew", padx = 5, pady = 5)
	
	marker_box.grid(column = 2, row = 1, sticky = "nsew", padx = 5, pady = 5)

	linecolor_label.grid(column = 3, row = 0, sticky = "nsew", padx = 5, pady = 5)

	linecolor_box.grid(column = 3, row = 1, sticky = "nsew", padx = 5, pady = 5)
	
	frame.grid(column = 0, row = 2, columnspan = 4)# sticky = "nsew")

	line_box.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	bar_box.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	pie_box.grid(column = 2, row = 3, sticky = "nsew", padx = 5, pady = 5)

	grid_box.grid(column = 3, row = 3, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 4, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 1, row = 4, sticky = "nsew", padx = 5, pady = 5)

	main_window.grid(column = 2, row = 4, sticky = "nsew", padx = 5, pady = 5)

	yp.mainloop()

	return

#year_plot(None)

# plot_overview(None)

def reserve_plot(parent_window):

	if parent_window:

		parent_window.destroy()

	rp = tk.Tk()

	rp.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	rp.title("Reserve Statistic")

	rp.columnconfigure(0, weight = 1, minsize = 150)

	rp.columnconfigure(1, weight = 1, minsize = 150)

	rp.columnconfigure(3, weight = 1, minsize = 150)

	rp.columnconfigure(4, weight = 1, minsize = 150)

	rp.rowconfigure(0, weight = 1)

	rp.rowconfigure(1, weight = 1)

	rp.rowconfigure(2, weight = 1)#, minsize = 350)

	rp.rowconfigure(3, weight = 1)

	rp.rowconfigure(4, weight = 1)

	def custom_treeview_style():

		style = ttk.Style()

		style.configure("Custom.Treeview", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("CustomCombobox.TCombobox", bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])), fieldbackground = chip.read_row("settings", "bg")[0])

		style.configure("Custom.Treeview.Heading", background = chip.read_row("settings", "bg")[0], foreground = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0])))

		style.map("Custom.Treeview.", background = [("selected", chip.read_row("settings", "activeforeground")[0])] )

		style.map("Custom.Treeview.Heading", background = [("active", chip.read_row("settings", "activebackground")[0])])

		return style

	custom_treeview_style()

	frame = tk.Frame(rp)

	back_button = tk.Button(rp, text = "back", command = lambda: plot_overview(rp))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(rp, text = "close", command = rp.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	main_window = tk.Button(rp, text = "Main Window", command = lambda: Finanz_Coin.start_window(rp))

	main_window.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	def dic_tolist(dic):

		new_list = []

		for i in dic.keys():

			new_list.append(i)

		return new_list

	def make_xvalues(value):

		new_list = []

		for i in value:

			new_list.append(i[1])

		return new_list

	def make_yvalues(value):

		new_list = []

		for i in value:

			new_list.append(i[2])

		return new_list

	def update_plot():

		actual_tables = table_box.get()

		if not actual_tables:

			return

		plot_values = chip.read_dbtable(actual_tables)

		plot_values = chip.make_list(plot_values)

		x_value = make_xvalues(plot_values)

		y_value = make_yvalues(plot_values)

		fig, ax = plt.subplots(figsize = (10,6))

		if line_var.get():

			ax.plot(x_value, y_value, marker = plot_marker[marker_box.get()], linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label = "Reserve")

			ax.grid(grid_var.get())

			plt.xticks(rotation = 45, ha = "right")

			plt.legend()

			plt.subplots_adjust(bottom = 0.3)

		elif pie_var.get():

			ax.pie( y_value, labels = x_value, autopct = "%1.1f%%")  # color = plot_linecolor[linecolor_box.get()])

			plt.legend(loc = "center right", bbox_to_anchor = (-0.1, 0.2, 0, 0))

		elif bar_var.get():

			ax.bar( x_value, y_value, linestyle = plot_linestyle[linestyle_box.get()], color = plot_linecolor[linecolor_box.get()], label = "Reserve")

			ax.grid(grid_var.get())

			plt.xticks(rotation = 45, ha = "right")

			plt.legend()

			plt.subplots_adjust(bottom = 0.3)


		canvas = FigureCanvasTkAgg(fig, master=frame)

		canvas.draw()

		canvas.get_tk_widget().grid(column = 0, row = 2,columnspan = 4, sticky = "nsew")

		plt.close(fig)

		return

	def select_year(event):

		# canvas.get_tk_widget().destroy()

		update_plot()

		return

	def pie_check():

		bar_var.set(False)

		line_var.set(False)

		linestyle_box.config(state = "disabled")

		marker_box.config(state = "disabled")

		linecolor_box.config(state = "disabled")

		grid_box.config(state = "disabled")

		update_plot()

		return

	def line_check():

		bar_var.set(False)

		pie_var.set(False)

		linestyle_box.config(state = "normal")

		marker_box.config(state = "normal")

		linecolor_box.config(state = "normal")

		grid_box.config(state = "normal")

		update_plot()

		return

	def bar_check():

		line_var.set(False)

		pie_var.set(False)

		marker_box.config(state = "disabled")

		linestyle_box.config(state = "disabled")

		linecolor_box.config(state = "enable")

		grid_box.config(state = "normal")

		update_plot()

		return

	def select_linestyle(event):

		update_plot()

		return

	def marker_style(event):

		update_plot()

		return

	def line_style(event):

		update_plot()

		return

	def grid_style():

		update_plot()

		return

	table_box = ttk.Combobox(rp, style = "CustomCombobox.TCombobox")

	table_box.bind("<<ComboboxSelected>>", select_year)

	table_box["values"] = chip.read_reservetables()

	linestyle_box = ttk.Combobox(rp, style = "CustomCombobox.TCombobox")

	marker_box = ttk.Combobox(rp, style = "CustomCombobox.TCombobox")

	linecolor_box = ttk.Combobox(rp, style = "CustomCombobox.TCombobox")

	marker_box.bind("<<ComboboxSelected>>", marker_style)

	linestyle_box["values"] = dic_tolist(plot_linestyle)

	linestyle_box.bind("<<ComboboxSelected>>", select_linestyle)

	linestyle_box.set(dic_tolist(plot_linestyle)[0])

	marker_box["values"] = dic_tolist(plot_marker)

	marker_box.set(dic_tolist(plot_marker)[0])

	linecolor_box["values"] = dic_tolist(plot_linecolor)

	linecolor_box.set(dic_tolist(plot_linecolor)[7])

	linecolor_box.bind("<<ComboboxSelected>>", line_style)

	grid_var = tk.IntVar()

	grid_box = tk.Checkbutton(rp, text = "Grid", variable = grid_var, command = grid_style)

	grid_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	grid_var.set(True)

	line_var = tk.IntVar()

	line_box = tk.Checkbutton(rp, text = "Line", variable = line_var, command = line_check)

	line_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	bar_var = tk.IntVar()

	bar_box = tk.Checkbutton(rp, text = "Bar", variable = bar_var, command = bar_check)

	bar_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	pie_var = tk.IntVar()

	pie_box = tk.Checkbutton(rp, text = "Pie", variable = pie_var, command = pie_check)

	pie_box.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), bd = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	line_var.set(True)

	bar_var.set(False)

	pie_var.set(False)

	plottable_label = tk.Label(rp, text = "Year")

	plottable_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	linestyle_label = tk.Label(rp, text = "Linestyle")

	linestyle_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	marker_label = tk.Label(rp, text = "Marker Style")

	marker_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	linecolor_label = tk.Label(rp, text = "Line Color")

	linecolor_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	plottable_label.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	table_box.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	linestyle_label.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

	linestyle_box.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

	marker_label.grid(column = 2, row = 0, sticky = "nsew", padx = 5, pady = 5)

	marker_box.grid(column = 2, row = 1, sticky = "nsew", padx = 5, pady = 5)

	linecolor_label.grid(column = 3, row = 0, sticky = "nsew", padx = 5, pady = 5)

	linecolor_box.grid(column = 3, row = 1, sticky = "nsew", padx = 5, pady = 5)

	frame.grid(column = 0, row = 2, columnspan = 4)#, sticky = "nsew", padx = 5, pady = 5)

	line_box.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	bar_box.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	pie_box.grid(column = 2, row = 3, sticky = "nsew", padx = 5, pady = 5)

	grid_box.grid(column = 3, row = 3, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 4, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 1, row = 4, sticky = "nsew", padx = 5, pady = 5)

	main_window.grid(column = 2, row = 4, sticky = "nsew", padx = 5, pady = 5)

	rp.mainloop()

	return

def settings(parent_window):

	if parent_window:

		parent_window.destroy()

	sw = tk.Tk()

	sw.title("Settings")

	sw.columnconfigure(0, weight = 1, minsize = 150)

	sw.columnconfigure(1, weight = 1, minsize = 150)

	sw.columnconfigure(2, weight = 1, minsize = 150)

	sw.columnconfigure(3, weight = 1, minsize = 150)

	sw.columnconfigure(4, weight = 1, minsize = 150)

	sw.columnconfigure(5, weight = 1, minsize = 150)

	sw.columnconfigure(6, weight = 1, minsize = 150)

	sw.rowconfigure(0, weight = 1)

	sw.rowconfigure(1, weight = 1)

	sw.rowconfigure(2, weight = 1)

	sw.rowconfigure(3, weight = 1)

	sw.rowconfigure(4, weight = 1)

	sw.rowconfigure(5, weight = 1)

	sw.rowconfigure(6, weight = 1)

	#sw.config(bg = "#ffffff")

	def make_hex_color(red, green, blue):

		r = f"{red:02x}"

		g = f"{green:02x}"

		b = f"{blue:02x}"

		return[r, g, b]

	def bg_color_update(value):

		red = bg_red_slider.get()

		green = bg_green_slider.get()

		blue = bg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		sw.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_red_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_green_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_blue_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_red_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_blue_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_green_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		close_button.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		designe_button.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_scale.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_size_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_red_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_green_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_blue_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_red_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_green_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_blue_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		highlight_thickness_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_red_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_green_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_blue_slider.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		back_button.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		add_button.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_type_label.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_labe.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_style_label.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		cursor_style_label.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		window_visible_scale.config(bg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		return

	def tx_color_update(value):

		red = tx_red_slider.get()

		green = tx_green_slider.get()

		blue = tx_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		tx_red_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_green_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_blue_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_red_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_green_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_blue_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		close_button.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		designe_button.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_scale.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_size_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_red_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_green_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_blue_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_red_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_green_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_blue_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		highlight_thickness_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_red_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_green_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_blue_slider.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		back_button.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		add_button.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_type_label.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_labe.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_style_label.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		cursor_style_label.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		window_visible_scale.config(fg = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		return
		
	def font_art_update(event):

		tx_red_slider.config(font = (font_box.get()))

		tx_green_slider.config(font = (font_box.get()))

		tx_blue_slider.config(font = (font_box.get()))

		bg_red_slider.config(font = (font_box.get()))

		bg_green_slider.config(font = (font_box.get()))

		bg_blue_slider.config(font = (font_box.get()))

		close_button.config(font = (font_box.get()))

		designe_button.config(font = (font_box.get()))

		border_style_scale.config(font = (font_box.get()))

		font_size_slider.config(font = (font_box.get()))

		acbg_red_slider.config(font = (font_box.get()))

		acbg_green_slider.config(font = (font_box.get()))

		acbg_blue_slider.config(font = (font_box.get()))

		acfg_red_slider.config(font = (font_box.get()))

		acfg_green_slider.config(font = (font_box.get()))

		acfg_blue_slider.config(font = (font_box.get()))

		highlight_thickness_slider.config(font = (font_box.get()))

		hlbg_red_slider.config(font = (font_box.get()))

		hlbg_green_slider.config(font = (font_box.get()))

		hlbg_blue_slider.config(font = (font_box.get()))

		back_button.config(font = (font_box.get()))

		add_button.config(font = (font_box.get()))

		font_type_label.config(font = (font_box.get()))

		border_style_labe.config(font = (font_box.get()))

		font_style_label.config(font = (font_box.get()))

		cursor_style_label.config(font = (font_box.get()))

		window_visible_scale.config(font = (font_box.get()))

		return

	def font_style_update(event):

		tx_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		tx_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		tx_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		bg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		bg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		bg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		close_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		designe_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		border_style_scale.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		font_size_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acbg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acbg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acbg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acfg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acfg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acfg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		highlight_thickness_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		hlbg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		hlbg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		hlbg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		back_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		add_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		font_type_label.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		border_style_labe.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		font_style_label.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		cursor_style_label.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		window_visible_scale.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		return

	def text_size_update(value):

		tx_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		tx_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		tx_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		bg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		bg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		bg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		close_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		designe_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		border_style_scale.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		font_size_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acbg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acbg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acbg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acfg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acfg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		acfg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		highlight_thickness_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		hlbg_red_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		hlbg_green_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		hlbg_blue_slider.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		back_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		add_button.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		font_type_label.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		border_style_labe.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		font_style_label.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		cursor_style_label.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		window_visible_scale.config(font = (font_box.get(), font_size_slider.get(), style_box.get()))

		return

	def border_width_update(value):

		tx_red_slider.config(borderwidth = border_style_scale.get())

		tx_green_slider.config(borderwidth = border_style_scale.get())

		tx_blue_slider.config(borderwidth = border_style_scale.get())

		bg_red_slider.config(borderwidth = border_style_scale.get())

		bg_green_slider.config(borderwidth = border_style_scale.get())

		bg_blue_slider.config(borderwidth = border_style_scale.get())

		close_button.config(borderwidth = border_style_scale.get())

		designe_button.config(borderwidth = border_style_scale.get())

		border_style_scale.config(borderwidth = border_style_scale.get())

		font_size_slider.config(borderwidth = border_style_scale.get())

		acbg_red_slider.config(borderwidth = border_style_scale.get())

		acbg_green_slider.config(borderwidth = border_style_scale.get())

		acbg_blue_slider.config(borderwidth = border_style_scale.get())

		acfg_red_slider.config(borderwidth = border_style_scale.get())

		acfg_green_slider.config(borderwidth = border_style_scale.get())

		acfg_blue_slider.config(borderwidth = border_style_scale.get())

		highlight_thickness_slider.config(borderwidth = border_style_scale.get())
		
		hlbg_red_slider.config(borderwidth = border_style_scale.get())

		hlbg_green_slider.config(borderwidth = border_style_scale.get())

		hlbg_blue_slider.config(borderwidth = border_style_scale.get())

		back_button.config(borderwidth = border_style_scale.get())

		add_button.config(borderwidth = border_style_scale.get())

		font_type_label.config(borderwidth = border_style_scale.get())

		border_style_labe.config(borderwidth = border_style_scale.get())

		font_style_label.config(borderwidth = border_style_scale.get())

		cursor_style_label.config(borderwidth = border_style_scale.get())

		window_visible_scale.config(borderwidth = border_style_scale.get())

		return

	def relief_style_update(event):

		tx_red_slider.config(relief = relief_style_box.get())

		tx_green_slider.config(relief = relief_style_box.get())

		tx_blue_slider.config(relief = relief_style_box.get())

		bg_red_slider.config(relief = relief_style_box.get())

		bg_green_slider.config(relief = relief_style_box.get())

		bg_blue_slider.config(relief = relief_style_box.get())

		close_button.config(relief = relief_style_box.get())

		designe_button.config(relief = relief_style_box.get())

		border_style_scale.config(relief = relief_style_box.get())

		font_size_slider.config(relief = relief_style_box.get())

		acbg_red_slider.config(relief = relief_style_box.get())

		acbg_green_slider.config(relief = relief_style_box.get())

		acbg_blue_slider.config(relief = relief_style_box.get())

		acfg_red_slider.config(relief = relief_style_box.get())

		acfg_green_slider.config(relief = relief_style_box.get())

		acfg_blue_slider.config(relief = relief_style_box.get())

		highlight_thickness_slider.config(relief = relief_style_box.get())

		hlbg_red_slider.config(relief = relief_style_box.get())

		hlbg_green_slider.config(relief = relief_style_box.get())

		hlbg_blue_slider.config(relief = relief_style_box.get())

		back_button.config(relief = relief_style_box.get())

		add_button.config(relief = relief_style_box.get())

		font_type_label.config(relief = relief_style_box.get())

		border_style_labe.config(relief = relief_style_box.get())

		font_style_label.config(relief = relief_style_box.get())

		cursor_style_label.config(relief = relief_style_box.get())

		window_visible_scale.config(relief = relief_style_box.get())

		return

	def active_background_update(value):

		red = acbg_red_slider.get()

		green = acbg_green_slider.get()

		blue = acbg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		tx_red_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_green_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_blue_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_red_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_green_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_blue_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		close_button.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		designe_button.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_scale.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_size_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_red_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_green_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_blue_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_red_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_green_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_blue_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		highlight_thickness_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_red_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_green_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_blue_slider.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		back_button.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		add_button.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_type_label.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_labe.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_style_label.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		cursor_style_label.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		window_visible_scale.config(activebackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		return

	def active_foreground_update(value):

		red = acfg_red_slider.get()

		green = acfg_green_slider.get()

		blue = acfg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		close_button.config(activeforeground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		designe_button.config(activeforeground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		back_button.config(activeforeground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		add_button.config(activeforeground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		return
	
	def cursor_style_update(event):

		tx_red_slider.config(cursor = cursor_style_box.get())

		tx_green_slider.config(cursor = cursor_style_box.get())

		tx_blue_slider.config(cursor = cursor_style_box.get())

		bg_red_slider.config(cursor = cursor_style_box.get())

		bg_green_slider.config(cursor = cursor_style_box.get())

		bg_blue_slider.config(cursor = cursor_style_box.get())

		close_button.config(cursor = cursor_style_box.get())

		designe_button.config(cursor = cursor_style_box.get())

		border_style_scale.config(cursor = cursor_style_box.get())

		font_size_slider.config(cursor = cursor_style_box.get())

		acbg_red_slider.config(cursor = cursor_style_box.get())

		acbg_green_slider.config(cursor = cursor_style_box.get())

		acbg_blue_slider.config(cursor = cursor_style_box.get())

		acfg_red_slider.config(cursor = cursor_style_box.get())

		acfg_green_slider.config(cursor = cursor_style_box.get())

		acfg_blue_slider.config(cursor = cursor_style_box.get())

		highlight_thickness_slider.config(cursor = cursor_style_box.get())

		hlbg_red_slider.config(cursor = cursor_style_box.get())

		hlbg_green_slider.config(cursor = cursor_style_box.get())

		hlbg_blue_slider.config(cursor = cursor_style_box.get())

		back_button.config(cursor = cursor_style_box.get())

		add_button.config(cursor = cursor_style_box.get())

		font_type_label.config(cursor = cursor_style_box.get())

		border_style_labe.config(cursor = cursor_style_box.get())

		font_style_label.config(cursor = cursor_style_box.get())

		cursor_style_label.config(cursor = cursor_style_box.get())

		window_visible_scale.config(cursor = cursor_style_box.get())

		return

	def highlight_thickness_update(value):

		tx_red_slider.config(highlightthickness = highlight_thickness_slider.get())

		tx_green_slider.config(highlightthickness = highlight_thickness_slider.get())

		tx_blue_slider.config(highlightthickness = highlight_thickness_slider.get())

		bg_red_slider.config(highlightthickness = highlight_thickness_slider.get())

		bg_green_slider.config(highlightthickness = highlight_thickness_slider.get())

		bg_blue_slider.config(highlightthickness = highlight_thickness_slider.get())

		close_button.config(highlightthickness = highlight_thickness_slider.get())

		designe_button.config(highlightthickness = highlight_thickness_slider.get())

		border_style_scale.config(highlightthickness = highlight_thickness_slider.get())

		font_size_slider.config(highlightthickness = highlight_thickness_slider.get())

		acbg_red_slider.config(highlightthickness = highlight_thickness_slider.get())

		acbg_green_slider.config(highlightthickness = highlight_thickness_slider.get())

		acbg_blue_slider.config(highlightthickness = highlight_thickness_slider.get())

		acfg_red_slider.config(highlightthickness = highlight_thickness_slider.get())

		acfg_green_slider.config(highlightthickness = highlight_thickness_slider.get())

		acfg_blue_slider.config(highlightthickness = highlight_thickness_slider.get())

		highlight_thickness_slider.config(highlightthickness = highlight_thickness_slider.get())

		hlbg_red_slider.config(highlightthickness = highlight_thickness_slider.get())

		hlbg_green_slider.config(highlightthickness = highlight_thickness_slider.get())

		hlbg_blue_slider.config(highlightthickness = highlight_thickness_slider.get())

		back_button.config(highlightthickness = highlight_thickness_slider.get())

		add_button.config(highlightthickness = highlight_thickness_slider.get())

		font_type_label.config(highlightthickness = highlight_thickness_slider.get())

		border_style_labe.config(highlightthickness = highlight_thickness_slider.get())

		font_style_label.config(highlightthickness = highlight_thickness_slider.get())

		cursor_style_label.config(highlightthickness = highlight_thickness_slider.get())

		window_visible_scale.config(highlightthickness = highlight_thickness_slider.get())

		return

	def highlight_background_update(value):

		red = hlbg_red_slider.get()

		green = hlbg_green_slider.get()

		blue = hlbg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		close_button.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_red_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_green_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		tx_blue_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_red_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_green_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		bg_blue_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		close_button.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		designe_button.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_scale.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_size_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_red_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_green_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acbg_blue_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_red_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_green_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		acfg_blue_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		highlight_thickness_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_red_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_green_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		hlbg_blue_slider.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		back_button.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		add_button.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_type_label.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		border_style_labe.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		font_style_label.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		cursor_style_label.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		window_visible_scale.config(highlightbackground = f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		return
	#work
	def test_click():

		if designe_button.cget("text") == "Designe Exampel":

			designe_button.config(text = "nothing")

		else:

			designe_button.config(text = "Designe Exampel")

		return

	def window_visible_update(value):

		var = window_visible_scale.get()

		if var != 0:

			var = var / 100

		sw.attributes("-alpha", var)

	#work
	def add_designe():

		style_update = []

		style_row = ["bg", "fg", "font", "font_size", "font_style", "borderwidth", "relief", "activebackground", 
		"cursor", "highlightthickness", "highlightbackground", "activeforeground", "window_visible"]

		#background

		red = bg_red_slider.get()

		green = bg_green_slider.get()

		blue = bg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		style_update.append(f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		#foreground

		red = tx_red_slider.get()

		green = tx_green_slider.get()

		blue = tx_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		style_update.append(f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		#font

		if not font_box.get():

			style_update.append(f"None")
			
		else:

			style_update.append(f"{font_box.get()}")

		#font_size

		style_update.append(f"{font_size_slider.get()}")

		#font_style

		if not style_box.get():

			style_update.append(f"None")

		else:

			style_update.append(f"{style_box.get()}")

		#borderwidth

		style_update.append(f"{border_style_scale.get()}")

		#relief

		if not relief_style_box.get():

			style_update.append(f"None")

		else:

			style_update.append(f"{relief_style_box.get()}")

		#activebackground

		red = acbg_red_slider.get()

		green = acbg_green_slider.get()

		blue = acbg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		style_update.append(f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		#cursor
		
		if not cursor_style_box.get():

			style_update.append(f"None")

		else:

			style_update.append(f"{cursor_style_box.get()}")

		#highlightthickness

		style_update.append(f"{highlight_thickness_slider.get()}")

		#highlightbackground

		red = hlbg_red_slider.get()

		green = hlbg_green_slider.get()

		blue = hlbg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		style_update.append(f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		#activeforeground

		red = acfg_red_slider.get()

		green = acfg_green_slider.get()

		blue = acfg_blue_slider.get()

		hex_color = make_hex_color(red, green, blue)

		style_update.append(f"#{hex_color[0]}{hex_color[1]}{hex_color[2]}")

		#window visible

		var = window_visible_scale.get()

		if var != 0:

			var = var / 100

		style_update.append(f"{var}")


		# write in db

		for i, j in zip(style_row, style_update):

			chip.change_row("settings", i, j)

		return

	font_type = ["Arial", "Courier", "Helvetica", "Times"]

	font_style = ["normal", "bold", "italic", "underline", "overstrike"]

	relief_style = ["flat", "raised", "sunken", "groove", "solid"]

	bg_red_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Background Red", command = bg_color_update)

	bg_green_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Background Green", command = bg_color_update)

	bg_blue_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Background Blue", command = bg_color_update)

	close_button = tk.Button(sw, text = "close", command = sw.destroy)

	back_button = tk.Button(sw, text = "back", command = lambda: Finanz_Coin.start_window(sw))

	add_button = tk.Button(sw, text = "Add new Window designe", command = add_designe)
	
	tx_red_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Red Text", command = tx_color_update)

	tx_green_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Green Text", command = tx_color_update)

	tx_blue_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Blue Text", command = tx_color_update)

	designe_button = tk.Button(sw, text = "Designe Exampel", command = test_click)

	font_box = ttk.Combobox(sw)

	style_box = ttk.Combobox(sw)

	font_box["values"] = font_type

	style_box["values"] = font_style

	font_box.bind("<<ComboboxSelected>>", font_art_update)

	style_box.bind("<<ComboboxSelected>>", font_style_update)

	font_size_slider = tk.Scale(sw, from_ = 1, to = 40, orient = "horizontal", label = "Text Size", command = text_size_update)

	border_style_scale = tk.Scale(sw, from_ = 1, to = 20, orient = "horizontal", label = "Border width", command = border_width_update)

	relief_style_box = ttk.Combobox(sw)

	relief_style_box["values"] = relief_style

	relief_style_box.bind("<<ComboboxSelected>>", relief_style_update)

	font_type_label = tk.Label(sw, text = "Font Types")

	border_style_labe = tk.Label(sw, text = "Border Styles")

	font_style_label = tk.Label(sw, text = "Font Style")

	cursor_style_label = tk.Label(sw, text = "Cursor Style")

	#active background

	acbg_red_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Activebackground Red", command = active_background_update)

	acbg_green_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Activebackground Green", command = active_background_update)

	acbg_blue_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Activebackground Blue", command = active_background_update)

	#active foreground

	acfg_red_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Activeforeground Red", command = active_foreground_update)

	acfg_green_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Activeforeground Green", command = active_foreground_update)

	acfg_blue_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Activeforeground Blue", command = active_foreground_update)

	#highlight thickness

	highlight_thickness_slider = tk.Scale(sw, from_ = 1, to = 20, orient = "horizontal", label = "Highlight Thickness", command = highlight_thickness_update)

	#highlight background

	hlbg_red_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Border Red", command = highlight_background_update)

	hlbg_green_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Border Green", command = highlight_background_update)

	hlbg_blue_slider = tk.Scale(sw, from_ = 0, to = 255, orient = "horizontal", label = "Border Blue", command = highlight_background_update)

	#cursor

	cursor_variation = ["arrow", "hand2", "cross", "circle", "plus", "watch", "xterm"]

	cursor_style_box = ttk.Combobox(sw)

	cursor_style_box["values"] = cursor_variation

	cursor_style_box.bind("<<ComboboxSelected>>", cursor_style_update)

	# transparency

	window_visible_scale = tk.Scale(sw, from_ = 0, to = 100, orient = "horizontal", label = "Window transparency", command = window_visible_update)

	# config

	def hex_toint_red(value):

		value = value[1:]

		color_red = value[:2]

		color_red = int(color_red, 16)

		return color_red

	def hex_toint_green(value):

		value = value[1:]

		color_green = value[2:4]

		color_green = int(color_green, 16)

		return color_green

	def hex_toint_blue(value):

		value = value[1:]

		color_blue = value[4:6]

		color_blue = int(color_blue, 16)

		return color_blue

	font_box.set(chip.read_row("settings", "font"))

	style_box.set(chip.read_row("settings", "font_style"))

	font_size_slider.set(int(chip.read_row("settings", "font_size")[0]))

	border_style_scale.set(int(chip.read_row("settings", "borderwidth")[0]))

	relief_style_box.set(chip.read_row("settings", "relief")[0])

	acbg_red_slider.set(hex_toint_red(chip.read_row("settings", "activebackground")[0]))

	acbg_green_slider.set(hex_toint_green(chip.read_row("settings", "activebackground")[0]))

	acbg_blue_slider.set(hex_toint_blue(chip.read_row("settings", "activebackground")[0]))

	acfg_red_slider.set(hex_toint_red(chip.read_row("settings", "activeforeground")[0]))

	acfg_green_slider.set(hex_toint_green(chip.read_row("settings", "activeforeground")[0]))

	acfg_blue_slider.set(hex_toint_blue(chip.read_row("settings", "activeforeground")[0]))

	highlight_thickness_slider.set(int(chip.read_row("settings", "highlightthickness")[0]))

	cursor_style_box.set(chip.read_row("settings", "cursor")[0])

	bg_red_slider.set(hex_toint_red(chip.read_row("settings", "bg")[0]))

	bg_blue_slider.set(hex_toint_blue(chip.read_row("settings", "bg")[0]))

	bg_green_slider.set(hex_toint_green(chip.read_row("settings", "bg")[0]))

	tx_red_slider.set(hex_toint_red(chip.read_row("settings", "fg")[0]))

	tx_green_slider.set(hex_toint_green(chip.read_row("settings", "fg")[0]))

	tx_blue_slider.set(hex_toint_blue(chip.read_row("settings", "fg")[0]))

	hlbg_red_slider.set(hex_toint_red(chip.read_row("settings", "highlightbackground")[0]))

	hlbg_green_slider.set(hex_toint_green(chip.read_row("settings", "highlightbackground")[0]))

	hlbg_blue_slider.set(hex_toint_blue(chip.read_row("settings", "highlightbackground")[0]))

	value = float(chip.read_row("settings", "window_visible")[0])

	if value != 100:

		value = int(value * 100)

	else:

		value = int(value)

	window_visible_scale.set(value)

	sw.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	#(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
	#	int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
	#	relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
	#	highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	font_size_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	bg_red_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	bg_blue_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	bg_green_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	tx_red_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	tx_green_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	tx_blue_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	designe_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], activeforeground = chip.read_row("settings", "activeforeground")[0])

	border_style_scale.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	acbg_red_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	acbg_green_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	acbg_blue_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	highlight_thickness_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	hlbg_red_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	hlbg_green_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	hlbg_blue_slider.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	add_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], 
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	back_button.config(bg = "#ffffff",fg = "#000000", font = (font_box.get(), font_size_slider.get(), style_box.get()), 
		borderwidth = border_style_scale.get(), relief = relief_style_box.get(), activebackground = "#ffffff", activeforeground = "#000000", cursor = cursor_style_box.get(), 
		highlightthickness = highlight_thickness_slider.get(), highlightbackground = "#000000")

	font_type_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	border_style_labe.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	font_style_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	window_visible_scale.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	cursor_style_label.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], activeforeground = chip.read_row("settings", "activeforeground")[0])

	# gui

	bg_red_slider.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	bg_green_slider.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	bg_blue_slider.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady = 5)

	tx_red_slider.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

	tx_green_slider.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

	tx_blue_slider.grid(column = 1, row = 2, sticky = "nsew", padx = 5, pady = 5)

	font_type_label.grid(column = 2, row = 0, sticky = "nsew", padx = 5, pady = 5)

	font_box.grid(column = 2, row = 1, sticky = "nsew", padx = 5, pady = 5)

	font_style_label.grid(column = 2, row = 2, sticky = "nsew", padx = 5, pady = 5)

	style_box.grid(column = 2, row = 3, sticky = "nsew", padx = 5, pady = 5)

	font_size_slider.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)

	border_style_scale.grid(column = 4, row = 3, sticky = "nsew", padx = 5, pady = 5)

	border_style_labe.grid(column = 3, row = 0, sticky = "nsew", padx = 5, pady = 5)

	relief_style_box.grid(column = 3, row = 1, sticky = "nsew", padx = 5, pady = 5)

	acbg_red_slider.grid(column = 4, row = 0, sticky = "nsew", padx = 5, pady = 5)

	acbg_green_slider.grid(column = 4, row = 1, sticky = "nsew", padx = 5, pady = 5)

	acbg_blue_slider.grid(column = 4, row = 2, sticky = "nsew", padx = 5, pady = 5)

	acfg_red_slider.grid(column = 5, row = 0, sticky = "nsew", padx = 5, pady = 5)

	acfg_green_slider.grid(column = 5, row = 1, sticky = "nsew", padx = 5, pady = 5)

	acfg_blue_slider.grid(column = 5, row = 2, sticky = "nsew", padx = 5, pady = 5)

	window_visible_scale.grid(column = 5, row = 3, sticky = "nsew", padx = 5, pady = 5)

	cursor_style_label.grid(column = 3, row = 2, sticky = "nsew", padx = 5, pady = 5)

	cursor_style_box.grid(column = 3, row = 3, sticky = "nsew", padx = 5, pady = 5)

	highlight_thickness_slider.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)

	hlbg_red_slider.grid(column = 6, row = 0, sticky = "nsew", padx = 5, pady = 5)

	hlbg_green_slider.grid(column = 6, row = 1, sticky = "nsew", padx = 5, pady = 5)

	hlbg_blue_slider.grid(column = 6, row = 2, sticky = "nsew", padx = 5, pady = 5)

	designe_button.grid(column = 5, row = 4, sticky = "nsew", padx = 5, pady = 5)

	add_button.grid(column = 3, row = 6, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 6, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 6, row = 6, sticky = "nsew", padx = 5, pady = 5)

	sw.mainloop()

	return

def help_window(parent_window):


	if parent_window:

		parent_window.destroy()

	hw = tk.Tk()

	hw.title("Money Coin")

	hw.config(bg = chip.read_row("settings", "bg")[0], cursor = chip.read_row("settings", "cursor")[0], relief = chip.read_row("settings", "relief")[0])

	hw.columnconfigure(0, weight = 1, minsize = 150)
	
	hw.rowconfigure(0, weight = 1)

	hw.rowconfigure(1, weight = 1)

	hw.rowconfigure(2, weight = 1)

	helptext = tk.Label(hw, text = "to fill values in reserve use in month overview in outgo name reserve an it put automatic in reserve table")

	helptext.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0])

	back_button = tk.Button(hw, text = "back", command = lambda: Finanz_Coin.start_window(hw))

	back_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0],
		activeforeground = chip.read_row("settings", "activeforeground")[0])

	close_button = tk.Button(hw, text = "close", command = hw.destroy)

	close_button.config(bg = chip.read_row("settings", "bg")[0], fg = chip.read_row("settings", "fg")[0], font = (chip.read_row("settings", "font")[0], 
		int(chip.read_row("settings", "font_size")[0]), chip.read_row("settings", "font_style")[0]), borderwidth = int(chip.read_row("settings", "borderwidth")[0]),
		relief = chip.read_row("settings", "relief")[0], activebackground = chip.read_row("settings", "activebackground")[0], cursor = chip.read_row("settings", "cursor")[0],
		highlightthickness = chip.read_row("settings", "highlightthickness")[0], highlightbackground = chip.read_row("settings", "highlightbackground")[0], activeforeground = chip.read_row("settings", "activeforeground")[0])

	helptext.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

	back_button.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)

	close_button.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady = 5)


	return









