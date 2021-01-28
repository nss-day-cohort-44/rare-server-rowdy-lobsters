import json
import sqlite3
from models import Post

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
			p.approved
			FROM Posts p
		""")

		data = db_cursor.fetchall()
		posts = []

		for row in data:
			post = Post( row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"],
						row["image_url"], row["content"], row["approved"])
			
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
			p.approved
			FROM Posts p
			WHERE id = ?
		""", (id,))

		row = db_cursor.fetchone()

		post = Post( row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"],
					row["image_url"], row["content"], row["approved"])

		return json.dumps(post.__dict__)

def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor=conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Posts
            (user_id,
			category_id,
			title,
			publication_date,
			image_url,
			content,
			approved)
        VALUES
            ( ?, ?, ?, ?, null, ?, null)
        """, ( new_post['user_id'], 
        new_post['category_id'], new_post['title'], 
        new_post['publication_date'],
        new_post['content']))

        id=db_cursor.lastrowid

        new_post['id']=id
    
    return json.dumps(new_post)
		
