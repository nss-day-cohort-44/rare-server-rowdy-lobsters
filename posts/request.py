import json
import sqlite3
from models import Post, User

def get_all_posts():

	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		SELECT
			p.id,
			p.user_id,
			p.category_id,
			p.title,
			p.publication_date,
			p.image_url,
			p.content,
			p.approved,
			u.first_name,
			u.last_name
		FROM Posts p
		JOIN Users u
			ON u.id = p.user_id
		""")

		data = db_cursor.fetchall()
		posts = []

		for row in data:
			post = Post( row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"],
						row["image_url"], row["content"], row["approved"])
			
			user = User(row["user_id"], row['first_name'], row['last_name'])

			post.user = user.__dict__
		
			posts.append(post.__dict__)
		
		return json.dumps(posts)

def get_single_post(id):

	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		SELECT
			p.id,
			p.user_id,
			p.category_id,
			p.title,
			p.publication_date,
			p.image_url,
			p.content,
			p.approved,
			u.first_name,
			u.last_name
		FROM Posts p
		JOIN Users u
			ON u.id = p.user_id
		WHERE p.id = ?
		""", (id,))

		row = db_cursor.fetchone()

		post = Post( row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"],
					row["image_url"], row["content"], row["approved"])

		user = User(row["user_id"], row['first_name'], row['last_name'])

		post.user = user.__dict__

		return json.dumps(post.__dict__)