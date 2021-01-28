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
			c.content
			FROM Comments c
		""")

		data = db_cursor.fetchall()
		comments = []

		for row in data:
			comment = Comment(row["id"], row["post_id"], row["author_id"], row["content"])
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
			c.content
			FROM Comments c
		""")

		row = db_cursor.fetchone()

		comment = Comment(row["id"], row["post_id"], row["author_id"], row["content"])

		return json.dumps(comment.__dict__)

def create_comment(comment):
	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		INSERT INTO Comments
		(post_id,
		author_id,
		content)
		VALUES (?, ?, ?)
		""", (comment["post_id"], comment["author_id"], comment["content"]))

		id = db_cursor.lastrowid

		comment["id"] = id

		return json.dumps(comment)