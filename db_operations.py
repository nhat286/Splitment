import mysql.connector

def db_connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Splitment"
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
            return rows[0], rows
        else:
            return -1, None
    except Exception as ex:
        print(ex)
        return -1, None
    finally:
        cursor.close()
        conn.close()

def get_user(id):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * from Users "
            "WHERE id= " + str(id))
    try:
        cursor.execute(query)
        rows = cursor.fetchone()
        if rows:
            return 0, rows
        else:
            return -1, None
    except Exception as ex:
        print(ex)
        return -1, None
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
                "VALUES (%s, %s) ")
        cursor.execute(query, (group_id, group['admin']))
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        return group_id
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
            "VALUES (%s, %s) ")
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

# order = {group_id, deadline, location, retail_name, retail_link }
def add_order(order):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Orders "
            "(group_id, deadline, location, retail_name, retail_link) "
            "VALUES (%(group_id)s, %(deadline)s, %(location)s, %(retail_name)s, %(retail_link)s) ")
    try:
        cursor.execute(query, (order))
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

def get_orders(user_id):
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True, buffered=True)
    query  = ("SELECT * FROM Orders "
            "WHERE group_id=("
            "SELECT group_id FROM GroupMembers "
            "WHERE user_id= " + str(user_id) + " )")
    orders = []
    
    try:
        cursor.execute(query)
        for row in cursor:
            orders.append(row.copy())
    except Exception as ex:
        print(ex)
        return -1, None
    finally:
        cursor.close()
        conn.close()
    
    return 0, orders

def get_group_info(id):
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True, buffered=True)
    query  = ("SELECT * FROM Groups "
            "WHERE id= " + str(id))
    
    try:
        cursor.execute(query)
        for row in cursor:
            if row:
                return 0, row
    except Exception as ex:
        print(ex)
        return -1, None
    finally:
        cursor.close()
        conn.close()
    
    return -1, None

def get_total_groups(user):
    err, curr_group = get_groups(user)
    if err == -1:
        return -1, None
    groups = []
    for group in curr_group:
        err, info = get_group_info(group['group_id'])
        if err == -1:
            break
        groups.append(info)
    return 0, groups

def get_group_members(group_id):
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True, buffered=True)
    query  = ("SELECT * FROM GroupMembers "
            "WHERE group_id= " + str(group_id))
    group_members = []
    
    try:
        cursor.execute(query)
        for row in cursor:
            group_members.append(row.copy())
    except Exception as ex:
        print(ex)
        return -1, None
    finally:
        cursor.close()
        conn.close()
    
    members = []
    for i in group_members:
        err, user = get_user(i['user_id'])
        if err > -1:
            members.append(user[1])
    
    return 0, members

def get_groups(user_id):
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True, buffered=True)
    query  = ("SELECT * FROM GroupMembers "
            "WHERE user_id= " + str(user_id))
    groups = []
    
    try:
        cursor.execute(query)
        for row in cursor:
            groups.append(row.copy())
    except Exception as ex:
        print(ex)
        return -1, None
    finally:
        cursor.close()
        conn.close()
    print(groups)
    return 0, groups

