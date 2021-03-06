import json
import sqlite3
from models import Post, User, Tag, Category
from users import get_single_user

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
			u.last_name,
			c.label
		FROM Posts p
		JOIN Users u
			ON u.id = p.user_id
		JOIN Categories c
			ON c.id = p.category_id
		""")

		data = db_cursor.fetchall()
		posts = []

		for row in data:
			post = Post( row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"],
						row["image_url"], row["content"], row["approved"])
			
			user = User(row["user_id"], row['first_name'], row['last_name'])
			
			category=Category(row["category_id"], row["label"])

			db_cursor.execute("""
			SELECT
				t.id,
				t.label,
				pt.id post_tag_id
			FROM Tags t
			JOIN PostTags pt
			WHERE pt.post_id = ? AND pt.tag_id = t.id
			""", (row["id"],))

			tag_data = db_cursor.fetchall()
			tags = []

			for tag_row in tag_data:
				tag = Tag(tag_row["id"], tag_row["label"])
				tag.post_tag_id = tag_row["post_tag_id"]
				tags.append(tag.__dict__)

			post.user = user.__dict__

			post.tags = tags
			
			post.category=category.__dict__
			
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
			u.last_name,
			c.label
		FROM Posts p
		JOIN Users u
			ON u.id = p.user_id
		JOIN Categories c
			ON c.id = p.category_id
		WHERE p.id = ?
		""", (id,))

		row = db_cursor.fetchone()

		post = Post( row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"],
					row["image_url"], row["content"], row["approved"])

		user = User(row["user_id"], row['first_name'], row['last_name'])
		
		category=Category(row["category_id"], row["label"])

		db_cursor.execute("""
			SELECT
				t.id,
				t.label,
				pt.id post_tag_id
			FROM Tags t
			JOIN PostTags pt
			WHERE pt.post_id = ? AND pt.tag_id = t.id
			""", (row["id"],))

		tag_data = db_cursor.fetchall()
		tags = []

		for tag_row in tag_data:
			tag = Tag(tag_row["id"], tag_row["label"])
			tag.post_tag_id = tag_row["post_tag_id"];
			tags.append(tag.__dict__)

		post.user = user.__dict__
		post.category=category.__dict__

		post.tags = tags

		return json.dumps(post.__dict__)

def create_post(new_post):

	with sqlite3.connect("./rare.db") as conn:
		conn.row_factory=sqlite3.Row
		db_cursor=conn.cursor()
# get associated user
# check user type
# if usertype is 1, approved is True
# if usertype is 2, approved is False
		approved=False
		myUser=json.loads(get_single_user(new_post['user_id']))
		if myUser['account_type_id'] ==1:
			approved=True

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
			( ?, ?, ?, ?, null, ?, ?)
			""", ( new_post['user_id'], 
			new_post['category_id'], new_post['title'], 
			new_post['publication_date'],
			new_post['content'], approved))

		id=db_cursor.lastrowid

		new_post['id']=id

	return json.dumps(new_post)

def update_post(id, new_post):
	with sqlite3.connect("./rare.db") as conn:
		db_cursor = conn.cursor()

		db_cursor.execute("""
		UPDATE Posts
		SET 
			id =?,
			user_id= ?,
			category_id=?,
			title= ?,
			publication_date=?,
			image_url= null,
			content=?,
			approved= ?
		WHERE id=?
		""", ( new_post['id'],new_post['user_id'], 
		new_post['category_id'], new_post['title'], 
		new_post['publication_date'],
		new_post['content'], new_post['approved'], id,))

# Were any rows affected?
# Did the client send an `id` that exists?
		rows_affected = db_cursor.rowcount

		if rows_affected == 0:
# Forces 404 response by main module
			return False
		else:
# Forces 204 response by main module
			return True

def delete_post(id):
	with sqlite3.connect("./rare.db") as conn:

		db_cursor = conn.cursor()

		db_cursor.execute("""
		DELETE FROM Posts
		WHERE id = ?
		""", (id,))

# def approve_post(id, new_post):
# 	with sqlite3.connect("./rare.db") as conn:
# 		db_cursor= conn.cursor()
