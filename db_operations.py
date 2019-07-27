import mysql.connector

def db_connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="GroupBuy"
    )
    return conn

# user = { email, password, name, address }
def add_user(user):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Users "
            "(email, password, name, address, rating) "
            "VALUES (%(email)s, %(password)s, %(name)s, %(address)s, %(rating)s) ")
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

# login = { email, password }
def check_login(email, password):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * from Users "
            "WHERE email=%s AND password=%s ")
    try:
        cursor.execute(query, (email, password))
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

# group = { admin, member_count, max_member }
def add_group(group):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Groups "
            "(admin, member_count, max_member) "
            "VALUES (%(admin)s, %(member_count)s, %(max_member)s) ")
    try:
        cursor.execute(query, group)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        group_id = insert_id
        query  = ("INSERT INTO GroupMembers "
                "(group_id, user_id) "
                "VALUES (%(group_id)s, %(admin)s) ")
        cursor.execute(query, (group_id, group['admin']))
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

def add_member(group, member):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO GroupMembers "
            "(group_id, user_id) "
            "VALUES (%(group_id)s, %(user_id)s) ")
    try:
        cursor.execute(query, (group, member))
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

# shop = { location, name, link }
def add_order(group, shop, deadline):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Orders "
            "(group_id, deadline, location, retail_name, retail_link) "
            "VALUES (%(group_id)s, %(deadline)s, %(location)s, %(retail_name)s, %(retail_link)s) ")
    try:
        cursor.execute(query, (group, deadline, shop))
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

# item = { order_id, item_name, item_link }
def add_item(user, item):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO UserItems "
            "(user_id, order_id, item_name, item_link) "
            "VALUES (%(user_id)s, %(order_id)s, %(item_name)s, %(item_link)s) ")
    try:
        cursor.execute(query, (user, item))
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

def get_orders():
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True, buffered=True)
    query  = ("SELECT * FROM Orders")
    orders = []
    
    try:
        cursor.execute(query)
        for row in cursor:
            orders.append(row.copy())
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()
    
    return orders

def get_groups():
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True, buffered=True)
    query  = ("SELECT * FROM Groups")
    groups = []
    
    try:
        cursor.execute(query)
        for row in cursor:
            groups.append(row.copy())
    except Exception as ex:
        print(ex)
        return -1
    finally:
        cursor.close()
        conn.close()
    
    return groups

