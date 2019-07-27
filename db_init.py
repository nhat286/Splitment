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
	mycursor.execute("DROP TABLE IF EXISTS Notifications")
	print("Old Notifications table removed (if it existed)")

	mycursor.execute("CREATE TABLE Users"
		" (user_id INT AUTO_INCREMENT PRIMARY KEY,"
		" username VARCHAR(255),"
		" password VARCHAR(255),"
		" email VARCHAR(255),"
		" name VARCHAR(255),"
                " UNIQUE(username),"
                " UNIQUE(email))")
	print("created Users table")

	mycursor.execute("CREATE TABLE Groups"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" user_id INT,"
		" url VARCHAR(255),"
		" headline VARCHAR(255),"
        " text VARCHAR(5000),"
        " date VARCHAR(20),"
                " UNIQUE(url,headline),"
		" FOREIGN KEY (user_id) REFERENCES Users(user_id))")
	print("created Groups table")

	mycursor.execute("CREATE TABLE Orders"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" user_id INT,"
		" start_date VARCHAR(255),"
		" key_terms VARCHAR(255),"
		" location VARCHAR(255),"
		" FOREIGN KEY (user_id) REFERENCES Users(user_id))")
	print("created Orders table")

	mycursor.execute("CREATE TABLE Notifications"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" user_id INT,"
		" url VARCHAR(255),"
		" viewed BOOLEAN default false,"
		" FOREIGN KEY (user_id) REFERENCES Users(user_id))")
	print("created Notifications table")

create_database()
create_tables()
