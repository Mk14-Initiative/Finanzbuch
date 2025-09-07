
import lib_install

import sqlite3

import os

from contextlib import closing

from os.path import exists

import datetime

curren_path = os.getcwd()

db_path = curren_path + "/" + "coin.db"

year_dic = {1: "January", 2: "February", 3: "March", 4: "April", 5: "Mai", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

# make db
def make_db():

	exists_db = exists(db_path)

	if exists_db == False:
		with closing(sqlite3.connect(db_path)) as db:
		#with closing(sqlite3.connect("test_base.db")) as db:
			
			with closing(db.cursor()) as cu:
			
				pass

			return

	return

# delete from table list squence and money time table
def check_alltabels(tabels):

	new_list = []

	for i in tabels:

		if "sqlite" in i or "money" in i or "Reserve" in i or "settings" in i:

			pass

		else:

			new_list.append(i)

	return new_list

# read specifed table
def read_dbtable(table):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			read_table = f"SELECT ID, Outgo, Sume FROM {table}"

			in_table = cu.execute(read_table).fetchall()

			return in_table

	return

# dlete specified db line
def delete_dbline(table, row):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:
		
			read_row = f"DELETE From {table} WHERE ID = {row}"

			cu.execute(read_row)

			db.commit()

			return

	return

# get last line
def get_lastline(table):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:
	
		with closing(db.cursor()) as cu:
	
			cu.execute(f"SELECT * FROM {table} ORDER BY ROWID DESC LIMIT 1")

			last_line = cu.fetchone()

		return last_line

	return

# check last dbline an delete
def check_dblastline(table):

	line = get_lastline(table)

	if line != None and line[1] == "rest":

		delete_dbline(table, line[0])

	return

# update db line
def update_dbrowline(table, update):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO {table}(outgo, sume) VALUES(?, ?)"

			cu.execute(update_row, update)

			db.commit()

	return

# add specified table with new values
def update_dbrow(table, update):

	check_dblastline(table)

	update_dbrowline(table, update)

	return

def delete_table(value):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			del_table = f"DROP TABLE IF EXISTS {value}"

			cu.execute(del_table)

			db.commit()

	return

# make main outgo table
def make_moneytime():

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute("CREATE TABLE IF NOT EXISTS money_time(ID INTEGER PRIMARY KEY AUTOINCREMENT, outgo Text NOT Null, sume FLOAT NOT Null, time Text NOT NULL, endtime Text Not NULL)")

			db.commit()

			return

# update db line
def update_dbline(table, update):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			update_line = f"UPDATE {table} SET outgo = ?, sume = ? WHERE id = ?"

			cu.execute(update_line, (update[1], update[2], update[0]))

			db.commit()

		return

# get all tables
def read_tables():

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute("SELECT name FROM sqlite_master WHERE type = 'table'; ")

			tabels = cu.fetchall()

			return [tabels[0] for tabels in tabels]

# change line
def change_moneytimerow(update):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			update_row = f"UPDATE money_time SET outgo = ?, sume = ?, time = ?, endtime = ? WHERE id = ?"

			cu.execute(update_row, (update[1], update[2], update[3], update[4], update[0]))

			db.commit()

	return

# add line
def add_moneytimerow(update):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO money_time (outgo, sume, time, endtime) VALUES(?, ?, ?, ?)"

			cu.execute(update_row, update)

			db.commit()

	return

# read table
def read_moneytimetable():

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			read_table = f"SELECT id, outgo, sume, time, endtime FROM money_time"

			in_table = cu.execute(read_table).fetchall()

			return in_table

	return

def initial_moneytime_table():

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO money_time (outgo, sume, time, endtime) VALUES('first', 1.0, 'month', 'none')"

			cu.execute(update_row)

			db.commit()

	return

# make new month table with aut primary key
def new_monthtable(table):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			new_table = f"CREATE TABLE IF NOT EXISTS {table}(ID INTEGER PRIMARY KEY AUTOINCREMENT, outgo Text NOT Null, sume FLOAT NOT Null)"

			cu.execute(new_table)

			db.commit()

			return

	return

# add row
def add_row(table, row):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"ALTER TABLE {table} ADD COLUMN {row} TEXT")

			db.commit()

	return

# change specified row
def change_row(table, row, value):

	#print(table)

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			update = (f"UPDATE {table} SET {row} = ? WHERE ID = 0")

			cu.execute(update, (value,))

			db.commit()

	return

# change specified row
def read_row(table, row):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"SELECT {row} FROM {table}")

			result = cu.fetchone()

			if result:

				return result

	return
#x = read_row("settings", "bg")

#print(x)
def initial_settings_table(table):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			update_row = f"INSERT INTO {table} (ID) VALUES (0)"

			cu.execute(update_row)

			db.commit()

	return

#settings_table("settings", "background_color")

def make_settings_table(table):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"CREATE TABLE IF NOT EXISTS {table}(ID INTEGER PRIMARY KEY AUTOINCREMENT)")

			db.commit()

			return

	return

def insert_row(table, row, value):

	# with closing(sqlite3.connect(db_path)) as db:
	with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"INSERT INTO {table} (ID, {row}) VALUES (?, ?)",(0, value))

			db.commit()

	return

# get time row from money table
def get_timerow():

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute(f"SELECT id, time, endtime FROM money_time")

			time_row = cu.fetchall()

			return time_row

	return

def make_list_fromtuple(value):

	return list(value)

# make list from tuple
def make_list(value):

	return [list(item) for item in value]

# make table sume with previoius sume and input
def table_sume(table):

	table_inside = read_dbtable(table)

	table_list = make_list(table_inside)

	temp_list = []

	for i in range(len(table_list)):

		if table_list[i][1] == "Lohn" or table_list[i][1] == "rest":

			temp_list.append(i)

	for i in temp_list:

		if i != 0:

			table_list.pop(i - 1)

		else:

			table_list.pop(temp_list[i])

	sume_table = 0.0

	for i in range(len(table_list)):

		#print(table_list[i][2])

		sume_table = sume_table + float(table_list[i][2])

	return sume_table

# get first line
def get_firsttable_line(table):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			query = f"SELECT * FROM {table} LIMIT 1"

			cu.execute(query)

			first_row = cu.fetchone()

			return first_row

	return

# check if table exist
def table_exist(tablename):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			cu.execute("SELECT name FROM sqlite_master WHERE type='table' AND name =?", (tablename,),)

			result = cu.fetchone()

			return result

	return

def previous_month(tablename):

	year = tablename.split("_")[1]

	month = tablename.split("_")[0]

	current_month_number = None

	for key, value in year_dic.items():

		if value == month:

			current_month_number = key

			break

	if current_month_number == 1:

		return 0

	previous_month_number = current_month_number - 1

	previous_month = year_dic[previous_month_number]

	previous_tablename = f"{previous_month}_{year}"

	return previous_tablename

# get sume from prevoius month
def get_restpriviousmonth(tablename):

	year = tablename.split("_")[1]

	month = tablename.split("_")[0]

	current_month_number = None

	for key, value in year_dic.items():

		if value == month:

			current_month_number = key

			break

	if current_month_number == 1:

		return 0

	previous_month_number = current_month_number - 1

	previous_month = year_dic[previous_month_number]

	previous_tablename = f"{previous_month}_{year}"

	if table_exist(previous_tablename) != None:

		previous_rest = get_lastline(previous_tablename)

		return previous_rest[2]

	return 0

def reverse_dic():

	reverse_dic = {v: k for k, v in year_dic.items()}

	return reverse_dic

# combine money time table with new table
def combine_timetablen_newtable(table, ids):

	with closing(sqlite3.connect(db_path)) as db:
	#with closing(sqlite3.connect("test_base.db")) as db:

		with closing(db.cursor()) as cu:

			# values from table similar ids
			query = """SELECT outgo, sume FROM money_time WHERE id IN ({seq})""".format( seq=",".join(["?"] * len(ids)))

			cu.execute(query, ids)

			selected_data = cu.fetchall()

			# join get values with new list
			cu.executemany(f"""INSERT INTO {table} (outgo, sume) VALUES (?,?)""", selected_data)

			db.commit()

	return

# spot year for table
def spot_year(value):

	new_list = []

	for i in value:

		if "year" in i[1]:

			new_list.append(i)

	return new_list

# check is credit end
def check_lifetime(month_list, value):

	new_list = []

	final_list = []

	reverse = reverse_dic()

	# split list name
	month = value.split("_")[0]

	#print(month)

	year = value.split("_")[1]

	# make list with only lifetime year
	for i in range(len(month_list)):

		if month_list[i][2] != "none":

			new_list.append(month_list[i])

	#print(new_list)

	for i in new_list:

		list_year = i[2].split(".")[0]

		list_month = i[2].split(".")[1]

		#print(list_month)

		# if month from list not month from value
		if year_dic.get(int(list_month)) != month:

			# if year from list < year from list
			if int(year) < int(list_year):

				# print("yes1")

				final_list.append(i)

			# if value year == list year and month value lower list month
			elif int(year) == int(list_year) and reverse.get(month) < int(list_month):

				final_list.append(i)

		# if list month == month from value
		elif year_dic.get(int(list_month)) == month:

			# if year value lower list year
			if int(year) < int(list_year):

				final_list.append(i)

			# if value year same list year and value month same list month
			elif int(year) == int(list_year) and reverse.get(month) == int(list_month):

				final_list.append(i)

	return final_list

# spot month for table
def spot_month(value, list_name):

	new_list = []

	# print(value)

	for i in value:

		if "month" in i[1] and "none" in i[2]:

			new_list.append(i)

	life_timelist = check_lifetime(value, list_name)

	new_list.extend(life_timelist)

	# print("nes list with lifetime ", new_list)

	return [new_list]

def check_terzmonth(month, time_list):

	#print("terz")

	# Dictionaries mit den Monatsnamen und den entsprechenden Zahlen
	terz_01_dic = {"January": 1, "April": 4, "July": 7, "October": 10}
	
	terz_02_dic = {"February": 2, "May": 5, "August": 8, "November": 11}
	
	terz_03_dic = {"March": 3, "June": 6, "September": 9, "December": 12}

	# Terz Optionen: jeder dritte Monat
	terz_option = {1: {1, 4, 7, 10}, 2: {2, 5, 8, 11}, 3: {3, 6, 9, 12}}

	# Den Monatsnamen aus dem `month` Argument extrahieren (z.B. "January_2025" -> "January")
	month_name = month.split("_")[0]

	# Liste für gefilterte Werte
	new_list = []

	terz_option = {1: terz_01_dic, 2: terz_02_dic, 3: terz_03_dic}
	
	new_list = []

	for i in range(len(time_list)):
	
		if "terz" in time_list[i][1]:
	
			terz_number = int(time_list[i][1].split(".")[1])
			
			if month.split("_")[0] in terz_option[terz_number]:
	
				new_list.append(time_list[i])

	# Wenn es Einträge in new_list gibt, diese zurückgeben
	if new_list:
	
		return new_list
	
	else:
	
		return False

# check month of quart
def check_quartmonth(month, time_list):

	quart_list = {"January": 1, "April": 4, "August": 8, "December": 12}

	new_list = []

	for i in range(len(time_list)):

		if "quart" in time_list[i][1]:

			if "." in time_list[i][1]:

				pass

			else:

				new_list.append(time_list[i])

	if month in quart_list:

		return new_list

	else:

		return False

	return

# check special quart
def check_specialquart(new_month, month):

	quart_02_dic = {2: "February", 6: "June", 10: "October"}

	quart_03_dic = {3: "March", 7: "July", 11: "November"}

	new_list = []

	temp_list = []

	# add all list items with "quart" to new list
	for i in range(len(month)):

		if "quart" in month[i][1]:

			new_list.append(month[i])

	# delte item from list thats only "quart"
	for i in range(len(new_list)):

		if "quart" in new_list[i]:

			new_list.pop(i)

	quart_list = []

	# split item on "."
	for i in range(len(new_list)):

		temp = new_list[i][1].split(".")

		quart_list.append(temp)

	# make item to int
	for i in range(len(quart_list)):

		quart_list[i][1] = int(quart_list[i][1])

	final_list = []

	# make comparison to first quart dic
	for i in range(len(quart_list)):

		# get dic key
		for comp2 in quart_02_dic:

			# if key in dic
			if comp2 == quart_list[i][1]:

				# get values
				for comp22 in quart_02_dic.values():

					# if value list month
					if comp22 == new_month:

						final_list.append(new_list[i])

		# get dic key
		for comp3 in quart_03_dic:

			# if key in dic
			if comp3 == quart_list[i][1]:

				# get values
				for comp33 in quart_03_dic.values():

					# if value list month
					if comp33 == new_month:

						final_list.append(new_list[i])

	return final_list

# check year in money time table
def check_year(year_list, list_name):

	new_list = []

	final_list = []

	# split item on "."
	for i in range(len(year_list)):

		temp = year_list[i][1].split(".")

		new_list.append(temp)

	# make int year month
	for i in range(len(new_list)):

		new_list[i][1] = int(new_list[i][1])

	# go furthur list
	for i in range(len(year_list)):

		# get dic keys
		for comp in year_dic:

			# check is key in list
			if comp == new_list[i][1]:

				temp = year_dic.get(comp)

				# check values in list
				if temp == list_name:

					final_list.append(year_list[i])

	return final_list

# make primary key table
def primary_keytable(value):

	# print("value", value)

	new_list = []

	for i in value:

		for j in i:

			new_list.append(j[0])

	return new_list

# make auto values in new table
def new_tableauto(value):

	#print(value)

	# get list from money time table
	list_oftime = get_timerow()

	# print("list of time", list_oftime, "\n")

	# make list from tuple
	get_monthtime = make_list(list_oftime)

	#print("get_monthtime ", get_monthtime, "\n")

	# get only months in table back
	month_list = spot_month(get_monthtime, value)

	# print("month_list ", month_list, "\n")

	# get only years from list back
	year_list = spot_year(get_monthtime)

	# print("year_list ", year_list, "\n")

	new_month = value.split("_")

	# print("new_month ", new_month, "\n")

	# check money time list of quart
	check_result = check_quartmonth(new_month[0], list_oftime)

	#print("check_result ", check_result, "\n")

	if check_result != False:

		month_list.append(check_result)

		# print("quart month ", month_list, "\n")

	# check money time list of special quart
	special_quartresult = check_specialquart(new_month[0], get_monthtime)

	# print("special_quartresult ", special_quartresult, "\n")

	if len(special_quartresult) > 0:

		month_list.append(special_quartresult)

		# print("month list special quart ", month_list, "\n")

	terz_result = check_terzmonth(new_month[0], get_monthtime)

	#print("terz_result ", terz_result)

	if terz_result != False:

		month_list.append(terz_result)

	# check of onec years in money time table
	year_check = check_year(year_list, new_month[0])

	if len(year_check) > 0:

		month_list.append(year_check)

		# print("month list with year ", month_list)

	# make list of primary key values
	key_list = primary_keytable(month_list)

	month_list = key_list

	#	 print(month_list)

	return month_list

def make_month_rest(year_list):

	for i in year_list:

		check_dblastline(i)

		pre_rest = 0.0

		#print(i)

		sume_table = table_sume(i)

		if sume_table == 0.0 or sume_table == None:

			sume_table = 0.0

		temp_value = get_firsttable_line(i)

		if temp_value:

			money_value = float(temp_value[2])

		else:

			sume_table = 0.0

		final_rest = round((float(money_value) - float(sume_table)) + float(pre_rest), 2)

		# print(final_rest)

		check_dblastline(i)

		update_dbrowline(i, ["rest", final_rest])

	return

def month_sort(year_list):

	month_dic = reverse_dic()

	try:

		year_list.sort(key=lambda x: month_dic[x.split("_")[0]])

	except:

		pass

	return year_list

def year_list(tablename):

	year = tablename.split("_")[1]

	table_list = read_tables()

	table_list = check_alltabels(table_list)

	new_list = []

	for i in table_list:

		if year in i.split("_")[1]:

			new_list.append(i)

	return new_list

def make_old_yearsumerest(list_year):

	# print("old yer list ", list_year)

	temp_value = 0.0

	for i in list_year:

		# print(i)

		now_rest = get_lastline(i)

		# print("now rest ", now_rest)

		if now_rest:

			now_rest = float(now_rest[2])

			# print("index =", list_year.index(i))

			previous_rest = list_year.index(i)

			if previous_rest == None or previous_rest == 0:

				pre_rest = 0.0

			else:

				pre_rest = get_lastline(list_year[previous_rest - 1])

				# print(pre_rest)

			if pre_rest == None or pre_rest == 0:

				pre_rest = 0.0

			else:

				pre_rest = float(pre_rest[2])

			# print("pre rest ", pre_rest)

			new_rest = round(now_rest + pre_rest, 2)

			# print("new rest = ", new_rest)

			check_dblastline(i)

			update_dbrowline(i, ["rest", new_rest])

	return

# make pre test for new table
def pre_autotest(tablename, money_value):

	# split tablename from year
	temp_name = tablename.split("_")

	# get now date
	now_date = datetime.datetime.now().strftime("%Y")

	if table_exist(tablename) == None:

		# check if now date year in tablename
		if int(temp_name[1]) >= int(now_date):

			new_monthtable(tablename)

			update_dbrowline(tablename, ["Lohn", money_value])

			#print(tablename)

			join_list = new_tableauto(tablename)

			combine_timetablen_newtable(tablename, join_list)

			pre_rest = get_restpriviousmonth(tablename)

			if pre_rest == None:

				pre_rest = 0.0

			sume_table = table_sume(tablename)

			final_rest = round((float(money_value) - float(sume_table)) + float(pre_rest), 2)

			check_dblastline(tablename)

			update_dbrowline(tablename, ["rest", final_rest])

			return True

		else:

			new_monthtable(tablename)

			update_dbrowline(tablename, ["Lohn", money_value])

			list_year = year_list(tablename)

			list_year = month_sort(list_year)

			make_month_rest(list_year)

			make_old_yearsumerest(list_year)

			# print(list_year)

			return True

		return None

	return None

# pre_autotest("Mai_2022", 2800)

# make rest on tables
def make_resttofuture(tablename):

	pre_rest = get_restpriviousmonth(tablename)

	sume_table = table_sume(tablename)

	first_line = get_firsttable_line(tablename)

	first_line = float(first_line[2])

	if pre_rest == None:

		pre_rest = 0.0

	final_rest = round((first_line - sume_table) + pre_rest, 2)

	return final_rest

# get list from now to future
def compare_tableinsidetofurute(date, table, year):

	change_list = []

	for j in table:

		temp = j.split("_")[0]

		temp_1 = int(j.split("_")[1])

		# print(temp)

		if (temp_1 > int(date[2])) or (temp_1 == int(date[2]) and year[temp] >= year[date[1]]):
			
			change_list.append(j)

	return change_list

# make list from all tables to now year
def change_tabletofuture(now_date, table):

	change_table = []

	for i in table:

		temp = i.split("_")

		# print(temp)

		temp = int(temp[1])

		if int(now_date[2]) == temp or int(now_date[2]) < temp:

			change_table.append(i)

	return change_table

# get date dd yy and mm from next one
def change_date():
	now_date = []

	now_date.append(datetime.datetime.now().strftime("%d"))

	temp = datetime.datetime.now()

	temp = temp.month

	temp = temp + 1

	if temp > 12:

		temp = 1

	now_date.append(datetime.datetime(1, temp, 1).strftime("%B"))

	now_date.append(datetime.datetime.now().strftime("%Y"))

	return now_date

# change month tables up to last from now to future
def change_moneytime_tableyear(update):

	change_moneytimerow(update)

	now_date = change_date()

	all_tables = read_tables()

	all_tables = check_alltabels(all_tables)

	change_table = change_tabletofuture(now_date, all_tables)

	# print(change_table)

	new_dic = reverse_dic()

	# print(new_dic[now_date[1]])

	change_list = compare_tableinsidetofurute(now_date, change_table, new_dic)

	# print(change_list)

	for i in change_list:

		now_tabel = read_dbtable(i)

		now_tabel = make_list(now_tabel)

		# print("i ", i)

		for j in now_tabel:

			if update[1] in j:

				j[2] = update[2]

				# print("j ", j)

				update_dbline(i, j)

		final_rest = make_resttofuture(i)

		check_dblastline(i)

		update_dbrowline(i, ["rest", final_rest])

	return

# delete line in money_timen and change all tabels till to the end
def money_timedeleteline(tablename, value):

	delete_dbline(tablename, value[0])

	now_date = change_date()

	all_tables = read_tables()

	all_tables = check_alltabels(all_tables)

	change_table = change_tabletofuture(now_date, all_tables)

	new_dic = reverse_dic()

	change_list = compare_tableinsidetofurute(now_date, change_table, new_dic)

	for i in change_list:

		now_tabel = read_dbtable(i)

		now_tabel = make_list(now_tabel)

		for j in now_tabel:

			if value[1] in j:
				# print(j)

				delete_dbline(i, j[0])

		final_rest = make_resttofuture(i)

		# print(final_rest)

		check_dblastline(i)

		update_dbrowline(i, ["rest", final_rest])

	return

def delete_yearsume(delete_value):

	# print(delete_value)

	list_year = year_list(delete_value)

	list_year = month_sort(list_year)

	# print(list_year)

	make_month_rest(list_year)

	make_old_yearsumerest(list_year)

	return

# add_moneytimerow(update):
def single_yearfutur(value, month):

	# print(value[2])

	if not "." in value[2]:

		return

	month_value = int(value[2].split(".")[1])

	# month_value = int(month_value)

	month_dic = reverse_dic()

	final_list = []

	if "year" in value[2] and "none" in value[3]:

		for i in month:

			month_list = i.split("_")[0]

			if month_dic.get(month_list) == month_value:

				final_list.append(i)

	return final_list

def single_lifetimefuture(value, month):

	if value[2] == "month" and value[3] != "none" and "." in value[3]:

		value_temp_0 = value[3].split(".")[0]

		value_temp_1 = value[3].split(".")[1]

	else:

		return

	new_list = []

	if "month" in value[2] and "none" != value[3]:

		for i in month:

			month_temp_0 = i.split("_")[0]

			month_temp_1 = i.split("_")[1]

			if (month_temp_0 == year_dic[int(value_temp_1)] and value_temp_0 == month_temp_1):

				new_list.append(i)

	return new_list

def singel_sepcialquart(value, month):

	quart_02_dic = ["Februar", "June", "Oktober"]

	quart_03_dic = ["March", "July", "November"]

	new_list = []

	if "quart.2" == value[2]:

		for i in month:

			temp = i.split("_")[0]

			if temp in quart_02_dic:

				new_list.append(i)

				# print("do")

	if "quart.3" == value[2]:

		for i in month:

			temp = i.split("_")[0]

			if temp in quart_03_dic:

				new_list.append(i)

				# print("else")

	return new_list

def single_quart(value, month):

	quart_list = {"Januar": 1, "April": 4, "August": 8, "Dezember": 12}

	new_list = []

	if "quart" == value[2]:

		for i in month:

			temp = i.split("_")[0]

			if temp in quart_list:

				new_list.append(i)

		return new_list

	return

def single_terz(value, month):

	terz_01_dic = {"January": 1, "April": 4, "July": 7, "October": 10}

	terz_02_dic = {"February": 2, "Mai": 5, "August": 8, "November": 11}

	terz_03_dic = {"March": 3, "June": 6, "September": 9, "December": 12}

	new_list = []

	if "terz.1" == value[2]:

		for i in month:

			temp = i.split("_")[0]

			if temp in terz_01_dic:

				new_list.append(i)

				# print("do")

	if "terz.2" == value[2]:

		for i in month:

			temp = i.split("_")[0]

			if temp in terz_02_dic:

				new_list.append(i)

				# print("else")

	if "terz.3" == value[2]:

		for i in month:

			temp = i.split("_")[0]

			if temp in terz_03_dic:

				new_list.append(i)

				# print("else")

	return new_list

# make new spot
def new_spot(value):
	if "month" in value[2] and "none" in value[3]:

		value

	else:

		value = None

	return value

def add_moneytimerowchangetable(update):

	add_moneytimerow(update)

	# print(update)

	now_date = change_date()

	all_tables = read_tables()

	all_tables = check_alltabels(all_tables)

	change_table = change_tabletofuture(now_date, all_tables)

	# print(change_table)

	new_dic = reverse_dic()

	change_list = compare_tableinsidetofurute(now_date, change_table, new_dic)

	# print(change_list)

	# is month only in update
	month_value = new_spot(update)

	# check is update month
	if month_value:

		for i in change_list:

			check_dblastline(i)

			update_dbrowline(i, update[:2])

			final_rest = make_resttofuture(i)

			update_dbrowline(i, ["rest", final_rest])

	quart = single_quart(update, change_list)

	if quart:

		for i in change_list:

			if i in quart:

				check_dblastline(i)

				update_dbrowline(i, update[:2])

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

			else:

				check_dblastline(i)

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

	special_quart = singel_sepcialquart(update, change_list)

	if special_quart:

		for i in change_list:

			if i in special_quart:

				check_dblastline(i)

				update_dbrowline(i, update[:2])

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

			else:

				check_dblastline(i)

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

	terz_result = single_terz(update, change_list)

	if terz_result:

		for i in change_list:

			if i in terz_result:

				check_dblastline(i)

				update_dbrowline(i, update[:2])

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

			else:

				check_dblastline(i)

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

	lifetime = single_lifetimefuture(update, change_list)

	# print(lifetime)

	bool_temp = False

	if lifetime:

		for i in range(len(change_list)):

			if bool_temp == False:

				# print("i ", change_list[i])

				check_dblastline(change_list[i])

				update_dbrowline(change_list[i], update[:2])

				final_rest = make_resttofuture(change_list[i])

				update_dbrowline(change_list[i], ["rest", final_rest])

				if change_list[i] in lifetime:

					bool_temp = True

					i = i + 1

					for j in range(i, len(change_list)):

						# print("j ", change_list[j])

						check_dblastline(change_list[j])

						final_rest = make_resttofuture(change_list[j])

						update_dbrowline(change_list[j], ["rest", final_rest])

						# i = i + 1

	one_year = single_yearfutur(update, change_list)

	if one_year:

		for i in change_list:

			if i in one_year:

				check_dblastline(i)

				update_dbrowline(i, update[:2])

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

			else:

				check_dblastline(i)

				final_rest = make_resttofuture(i)

				update_dbrowline(i, ["rest", final_rest])

	return

def add_newtableline_resttill_end(tablename, value):

	check_dblastline(tablename)

	update_dbrowline(tablename, value)

	list_year = year_list(tablename)

	list_year = month_sort(list_year)

	#print("make rest")

	make_month_rest(list_year)

	make_old_yearsumerest(list_year)

	return

#
def delete_monthline_rest_tillfutur(tablename, delete_value):

	delete_dbline(tablename, delete_value)

	check_dblastline(tablename)

	make_resttofuture(tablename)

	list_year = year_list(tablename)

	list_year = month_sort(list_year)

	make_month_rest(list_year)

	make_old_yearsumerest(list_year)

	return

#
def change_monthline_rest_tillfutur(tablename, change_value):

	update_dbline(tablename, change_value)

	check_dblastline(tablename)

	make_resttofuture(tablename)

	list_year = year_list(tablename)

	list_year = month_sort(list_year)

	make_month_rest(list_year)

	make_old_yearsumerest(list_year)

	return

def check_reservein_table(tablename, value_list):

	temp_list = read_dbtable(tablename)

	temp_list = make_list(temp_list)

	temp_list = check_alltabels(temp_list)

	# print(value_list)

	# print(temp_list)
	# return
	if not temp_list:

		for i in value_list:

			save_value = [tablename, i[0], i[1][2]]

			update_dbrowline(save_value[0], [save_value[1], save_value[2]])

		return

	else:

		max_len = max(len(value_list), len(temp_list))

		for i in range(max_len):

			if i < len(value_list) and i < len(temp_list):

				if value_list[i][0] == temp_list[i][1]:

					if value_list[i][1][2] == temp_list[i][2]:

						pass

					else:

						save_value = [tablename, temp_list[i][0], value_list[i][0], value_list[i][1][2]]

						# print(value_list[i][1][0])

						update_dbline( save_value[0], [save_value[1], save_value[2], save_value[3]])

				else:

					save_value = [ tablename, temp_list[i][0], value_list[i][0], value_list[i][1][2]]

					# print(value_list[i][1][0])

					# table, update

					update_dbline(save_value[0], [save_value[1], save_value[2], save_value[3]])

			elif i < len(value_list):

				# print(temp_list[i][0])

				if i >= len(temp_list):

					temp_value = temp_list[-1][0] + 1

					# print(temp_value)

				else:

					temp_value = temp_list[i][0]

				save_value = [tablename, value_list[i][0], value_list[i][1][2]]

				# print(save_value)

				# table, update

				update_dbrowline(save_value[0], [save_value[1], save_value[2]])

				# update_dbline(save_value[0], [save_value[1], save_value[2], save_value[3]])

			elif i < len(temp_list):

				delete_dbline(tablename, temp_list[i][0])

	return

def get_yearreserve(table_list):

	new_list = []

	table_list = month_sort(table_list)

	for i in table_list:

		temp = read_dbtable(i)

		# print(temp)

		for j in temp:

			# print(j)

			if "reserve" in j:

				j = make_list_fromtuple(j)

				new_list.append([i, j])

	return new_list

def make_reserve_year(table_list, reserve):

	new_list = []

	# print(reserve)

	# print(table_list)

	year = reserve.split("_")[1]

	for i in table_list:

		if year in i:

			new_list.append(i)

			pass

	# print(new_list)

	return new_list

def read_reservetables():

	table_list = read_tables()

	new_list = []

	for i in table_list:

		if "Reserve" in i:

			new_list.append(i)

	return new_list

def delete_t(tablename):

	temp_list = read_dbtable(tablename)

	# print(temp_list)

	for i in temp_list:

		# print(i[0])

		delete_dbline(tablename, i[0])

	return

def get_apart_reserve(tablename):

	reserve_list = read_dbtable(tablename)

	# print(reserve_list)

	temp_list = []

	for i in reserve_list:

		part = i[1].split("_")

		if len(part) != 2:

			temp_list.append(i)

	temp_list = make_list(temp_list)

	# print(temp_list)

	return temp_list

def make_reserve_sume(tablename):

	sume_table = table_sume(tablename)

	update_dbrowline(tablename, ["rest", sume_table])

	return

def get_reservevalues(tablename):

	# print(tablename)

	table_list = read_tables()

	table_list = check_alltabels(table_list)

	table_list = make_reserve_year(table_list, tablename)

	# print(table_list)

	table_list = month_sort(table_list)

	# print(table_list)

	table_list = get_yearreserve(table_list)

	check_dblastline(tablename)

	apart_values = get_apart_reserve(tablename)

	# print(apart_values)

	check_reservein_table(tablename, table_list)

	if apart_values:

		for i in apart_values:

			update_dbrowline(tablename, [i[1], i[2]])

	# t(tablename, table_list)

	check_dblastline(tablename)

	sume_table = table_sume(tablename)

	update_dbrowline(tablename, ["rest", sume_table])

	return

def make_yearlist_plot(year):

	table_list = read_tables()

	table_list = check_alltabels(table_list)

	table_list = month_sort(table_list)

	# table_list = year_list(table_list[0])

	# print(table_list)

	new_list = []

	for i in table_list:

		if year in i:

			new_list.append(i)

	# print(new_list)

	return new_list

def make_yearplot_valuelist(year_list):

	new_list = []

	# get_firsttable_line(table)

	# get_lastline(table)

	for i in year_list:

		# temp_list = (read_dbtable(i))

		# new_list.append(i)

		# new_list.append(make_list(temp_list))

		first_line = get_firsttable_line(i)

		first_line = make_list_fromtuple(first_line)

		last_line = get_lastline(i)

		last_line = make_list_fromtuple(last_line)

		temp_list = [i, first_line, last_line]

		new_list.append(temp_list)

	# print(new_list)

	# print(new_list[0][1])

	return new_list


def format_yearplot_list(year_list):

	new_list = []

	for i in range(0, len(year_list), 2):

		month = year_list[i]

		value = year_list[i + 1]

		if isinstance(month, str) and isinstance(value, list):

			new_list.append([month, [[entry[1], entry[2]] for entry in value if len(entry) >= 1]])

	return new_list

def make_yearplot(year):

	year_list = make_yearlist_plot(year)

	# print(year_list)

	year_values = make_yearplot_valuelist(year_list)

	return year_values

def run_install_script():
	
	try:
	
		# Das Skript als externen Prozess ausführen
		subprocess.check_call(["python3", "lib_install.install_packages.py"])
	
	except subprocess.CalledProcessError as e:
	
		print(f"Fehler beim Ausführen des Installationsskripts: {e}")

	return

# check or make tabel at programm start
def make_db_tabels():

	if __name__ == "__main__":
	
		run_install_script()

	make_db()

	result = table_exist("money_time")

	if result is None:

		make_moneytime()

		initial_moneytime_table()

	result = table_exist("settings")

	if result is None:

		make_settings_table("settings")

		initial_settings_table("settings")

		style_row = ["bg", "fg", "font", "font_size", "font_style", "borderwidth", "relief", "activebackground", 
		"cursor", "highlightthickness", "highlightbackground", "activeforeground", "window_visible"]

		standart_values = ["#ffffff", "#000000", "Arial", 10, "normal", 1, "flat", "#ffffff", "arrow", 1, "#000000", "#000000", 100]

		for i in style_row:

			add_row("settings", i)

		for i, j in zip(style_row, standart_values):

			change_row("settings", i, j)
		
	return
#make_db_tabels()
def check_reservetable_change(tablename):

	table_list = read_tables()

	table_list = check_alltabels(table_list)

	table_list = make_reserve_year(table_list, tablename)

	table_list = month_sort(table_list)

	# print(table_list)

	return table_list


# check_reservetable_change("Reserve_2022")
