import mysql.connector

def create_database():
	init_db = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password"
	)

	init_cursor = init_db.cursor()

	init_cursor.execute("DROP DATABASE IF EXISTS GroupBuy")
	print("Old GroupBuy database removed (if it existed)")

	init_cursor.execute("CREATE DATABASE GroupBuy")
	print("GroupBuy database created")

def create_tables():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password",
        database="GroupBuy"
	)

	mycursor = mydb.cursor()
	mycursor.execute("DROP TABLE IF EXISTS Users")
	print("Old Users table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Groups")
	print("Old Groups table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Orders")
	print("Old Orders table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS UserItems")
	print("Old UserItems table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS GroupMembers")
	print("Old GroupMembers table removed (if it existed)")
	#mycursor.execute("DROP TABLE IF EXISTS Notifications")
	#print("Old Notifications table removed (if it existed)")

	mycursor.execute("CREATE TABLE Users"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" email VARCHAR(255),"
		" password VARCHAR(255),"
		" name VARCHAR(255),"
		" address VARCHAR(255),"
		" rating FLOAT
                " UNIQUE(email))")
	print("created Users table")

	mycursor.execute("CREATE TABLE Groups"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" admin INT,"
		" member_count INT,"
		" max_member INT,"
		" FOREIGN KEY (admin) REFERENCES Users(id))")
	print("created Groups table")

	mycursor.execute("CREATE TABLE Orders"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" group_id INT,"
		" deadline VARCHAR(20),"
		" location VARCHAR(255),"
		" retail_name VARCHAR(255),"
		" retail_link VARCHAR(255),"
		" FOREIGN KEY (group_id) REFERENCES Groups(id)),")
	print("created Orders table")

	mycursor.execute("CREATE TABLE UserItems"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" user_id INT,"
		" order_id INT,"
		" item_name VARCHAR(255),"
		" item_link VARCHAR(255),"
		" FOREIGN KEY (user_id) REFERENCES Users(id)),"
		" FOREIGN KEY (order_id) REFERENCES Orders(id)),")
	print("created UserItems table")

	mycursor.execute("CREATE TABLE GroupMembers"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" group_id INT,"
		" user_id INT,"
		" FOREIGN KEY (user_id) REFERENCES Users(id)),"
		" FOREIGN KEY (group_id) REFERENCES Groups(id)),")
	print("created GroupMembers table")

	'''
	mycursor.execute("CREATE TABLE Notifications"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" user_id INT,"
		" url VARCHAR(255),"
		" viewed BOOLEAN default false,"
		" FOREIGN KEY (user_id) REFERENCES Users(user_id))")
	print("created Notifications table")
	'''

create_database()
create_tables()
