import json
import sqlite3
from models import PostTag, post

def get_all_post_tags():
	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
			SELECT
			t.id,
			t.post_id,
			t.tag_id
			FROM PostTags t
		""")

		data = db_cursor.fetchall()
		post_tags = []

		for row in data:
			post_tag = PostTag(row["id"], row["post_id"], row["tag_id"])
			post_tags.append(post_tag.__dict__)
		
		return json.dumps(post_tags)

def create_post_tag(post_tag):
	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		INSERT INTO PostTags
		(post_id, tag_id)
		VALUES (?, ?)
		""", (post_tag["post_id"], post_tag["tag_id"]))

		id = db_cursor.lastrowid

		post_tag["id"] = id

		return json.dumps(post_tag)