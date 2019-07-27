import mysql.connector

def db_connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="SIDRAT"
    )
    return conn

# user = { username, password, email, name }
def add_user(user):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Users "
            "(username, password, email, name) "
            "VALUES (%(username)s, %(password)s, %(email)s, %(name)s) ")
    try:
        cursor.execute(query, user)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        return insert_id
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()

# login = { username, password }
def check_login(username, password):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * from Users "
            "WHERE username=%s AND password=%s ")
    try:
        cursor.execute(query, (username, password))
        rows = cursor.fetchone()
        if rows:
            return rows[0]
        else:
            return -1
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()

# article = { user_id, url, headline }
def save_article(article):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Articles "
            "(user_id, url, headline, text, date) "
            "VALUES (%(user_id)s, %(url)s, %(headline)s, %(text)s, %(date)s) ")
    try:
        cursor.execute(query, article)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        return insert_id
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()

def get_articles(user_id):
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True, buffered=True)
    query  = ("SELECT * FROM Articles WHERE user_id=%(user_id)s")
    articles = []
    
    try:
        cursor.execute(query, user_id)
        for row in cursor:
            articles.append(row.copy())
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()
    
    return articles

def remove_saved_article(article):
    pass

# subscription = { user_id, start_date, key_terms, location }
def add_subscription(subscription):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Subscriptions "
            "(user_id, start_date, key_terms, location) "
            "VALUES (%(user_id)s, %(start_date)s, %(key_terms)s, %(location)s) ")
    try:
        cursor.execute(query, subscription)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        return insert_id
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()

#####
def update_subscription():
    pass

def add_notification(article):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Notifications "
            "(user_id, url) "
            "VALUES (%(user_id)s, %(url)s) ")
    try:
        cursor.execute(query, article)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        return insert_id
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()

def update_notification():
    pass
