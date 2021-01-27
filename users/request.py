import sqlite3
import json
from models import User

# GET METHODS HERE
def get_all_users():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.username,
            u.account_type_id
        FROM Users u
        """)

        users=[]
        dataset=db_cursor.fetchall()

        for row in dataset:
            user=User(row['id'], row['first_name'], row['last_name'], row['email'], row['username'],
            row['account_type_id'])

            users.append(user.__dict__)
    return json.dumps(users)

def get_single_user(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.username,
            u.account_type_id
        FROM Users u
        WHERE u.id=?
        """, (id,))

        
        data=db_cursor.fetchone()

        
        user = User(data['id'], data['first_name'], data['last_name'], data['email'], data['username'],
        data['account_type_id'])

    return json.dumps(user.__dict__)

# POST METHODS HERE

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()

        db_cursor.execute("""
        INSERT INTO Users
            (first_name,
            last_name,
            email,
            bio,
            username,
            profile_image_url,
            created_on,
            active,
            account_type_id)
        VALUES
            ( ?, ?, ?, null, ?, null, null, null, ?)
        """, ( new_user['first_name'], 
        new_user['last_name'], new_user['email'], 
        new_user['username'],
        new_user['account_type_id']))

        id=db_cursor.lastrowid

        new_user['id']=id
    
    return json.dumps(new_user)

def login(current_user):
    all_users=json.loads(get_all_users())
    list_of_email=[]
    for user in all_users:
        list_of_email.append(user['email'])

    if current_user['username'] in list_of_email:
        
        return json.dumps(current_user)
    else:
        return json.dumps(False)
    
    