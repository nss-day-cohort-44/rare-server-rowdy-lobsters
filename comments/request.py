import sqlite3
import json
from models import Comment

def get_all_comments():
	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
			SELECT
			c.id,
			c.post_id,
			c.author_id,
			c.content,
			c.created_on
			FROM Comments c
		""")

		data = db_cursor.fetchall()
		comments = []

		for row in data:
			comment = Comment(row["id"], row["post_id"], row["author_id"], row["content"], row["created_on"])
			comments.append(comment.__dict__)

		return json.dumps(comments)


def get_single_comment(id):
	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
			SELECT
			c.id,
			c.post_id,
			c.author_id,
			c.content,
			c.created_on
			FROM Comments c
			WHERE c.id = ?
		""", (id,))

		row = db_cursor.fetchone()

		comment = Comment(row["id"], row["post_id"], row["author_id"], row["content"], row["created_on"])

		return json.dumps(comment.__dict__)

def create_comment(comment):
	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		INSERT INTO Comments
		(post_id,
		author_id,
		content,
		created_on)
		VALUES (?, ?, ?, ?)
		""", (comment["post_id"], comment["author_id"], comment["content"], comment["created_on"]))

		id = db_cursor.lastrowid

		comment["id"] = id

		return json.dumps(comment)

def update_comment(id, new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
		
		
        db_cursor.execute("""
		UPDATE comments
			SET 
				id =?,
				post_id= ?,
				author_id=?,
				content=?,
				created_on= ?
		WHERE id=?
		""", ( new_comment['id'],new_comment['post_id'], 
        new_comment['author_id'], new_comment['content'], 
        new_comment['created_on'], id,))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
def delete_comment(id):
	with sqlite3.connect("./rare.db") as conn:

		db_cursor = conn.cursor()

		db_cursor.execute("""
			DELETE FROM Comments
			WHERE id = ?
		""", (id,))
