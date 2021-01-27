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
            u.password,
            u.is_staff
        FROM Users u
        """)

        users=[]
        dataset=db_cursor.fetchall()

        for row in dataset:
            user=User(row['id'], row['first_name'], row['last_name'], row['email'], row['username'],
            row['password'], row['is_staff'])

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
            u.password,
            u.is_staff
        FROM Users u
        WHERE u.id=?
        """, (id))

        
        data=db_cursor.fetchone()

        
        user = User(data['id'], data['first_name'], data['last_name'], data['email'], data['username'],
        data['password'], data['is_staff'])

    return json.dumps(user.__dict__)

# POST METHODS HERE

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()

        db_cursor.execute("""
        INSERT INTO Users
            first_name,
            last_name,
            email,
            username,
            password,
            is_staff
        VALUES
            ( ?, ?, ?, ?, ?, ?)
        """, ( new_user['first_name'], 
        new_user['last_name'], new_user['email'], 
        new_user['username'], new_user['password'],
        new_user['is_staff']))

        id=db_cursor.lastrowid

        new_user['id']=id
    
    return json.dumps(new_user)