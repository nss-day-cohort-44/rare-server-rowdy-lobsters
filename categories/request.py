import sqlite3
import json
from models import Category

def get_all_categories():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM categories c
        """)

        # Initialize an empty list to hold all category representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an category instance from the current row.
            # category that the database fields are specified in
            # exact order of the parameters defined in the
            # category class above.
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(categories)

def get_single_category(id):
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM categories c
        WHERE c.id = ?
        """, (id,))

        row = db_cursor.fetchone()

        category = Category(row['id'], row['label'])

        return json.dumps(category.__dict__)

def create_category(cat):

        with sqlite3.connect("./rare.db") as conn:

            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO categories
            (label)
            VALUES (?)
            """, (cat["label"],))

            id = db_cursor.lastrowid

            cat["id"] = id

            return json.dumps(cat)

def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:

        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM categories
        WHERE id = ?
        """, (id,))

def update_category(id, new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Category
            SET
                id = ?,
                label = ?
            WHERE id = ?
            """, ( 
                    new_category['id'], 
                    new_category['label'], 
                    id,
                )
        )

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
