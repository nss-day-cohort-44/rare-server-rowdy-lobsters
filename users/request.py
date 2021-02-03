import sqlite3
import json
from models import User, Account_Type

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
            u.created_on,
            u.account_type_id,
            a.label
        FROM Users u
        JOIN AccountTypes a
            ON a.id = u.account_type_id
        ORDER BY u.username ASC
        """)

        users=[]
        dataset=db_cursor.fetchall()

        for row in dataset:
            user=User(row['id'], row['first_name'], row['last_name'], row['email'], row['username'],
            None,
            row['created_on'],
            row['account_type_id'])

            account_type = Account_Type(row['account_type_id'], row['label'])

            user.account_type = account_type.__dict__

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
            u.created_on,
            u.account_type_id
        FROM Users u
        WHERE u.id=?
        """, (id,))

        
        data=db_cursor.fetchone()

        
        user = User(data['id'], data['first_name'], data['last_name'], data['email'], data['username'],
        None,
        data['created_on'],
        data['account_type_id'])

    return json.dumps(user.__dict__)

# POST METHODS HERE

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()
        print(new_user)
        db_cursor.execute("""
        INSERT INTO Users
            (first_name,
            last_name,
            email,
            bio,
            username,
            password,
            profile_image_url,
            created_on,
            active,
            account_type_id)
        VALUES
            ( ?, ?, ?, null, ?, ?, null, ?, null, ?)
        """, ( new_user['first_name'], 
        new_user['last_name'], new_user['email'], 
        new_user['username'],
        new_user['password'],
        new_user['created_on'],
        new_user['account_type_id']))

        id=db_cursor.lastrowid

        new_user['id']=id
    
    return json.dumps(new_user)
   


def login(current_user):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()
        db_cursor.execute("""
            SELECT email, password, id, account_type_id
            FROM users
            WHERE email = ? AND password = ?
        """, (current_user["username"], current_user["password"]))

        data = db_cursor.fetchone()

        if data:
            found_user = {"id": data["id"], 'valid': True, "account_type_id":data["account_type_id"]}
            
        else:
            found_user = {"valid": False}
        
        return(json.dumps(found_user))
