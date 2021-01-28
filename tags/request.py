import json
import sqlite3
from models import Tag

def get_all_tags():
	with sqlite3.connect("./rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
			SELECT
			t.id,
			t.label
			FROM Tags t
		""")

		data = db_cursor.fetchall()
		tags = []

		for row in data:
			tag = Tag(row["id"], row["label"])

			tags.append(tag.__dict__)
		
		return json.dumps(tags)

def get_single_tag(id):
		with sqlite3.connect("./rare.db") as conn:

			conn.row_factory = sqlite3.Row
			db_cursor = conn.cursor()

			db_cursor.execute("""
				SELECT
				t.id,
				t.label
				FROM Tags t
				WHERE t.id = ?
			""", (id,))

			row = db_cursor.fetchone()

			tag = Tag(row["id"], row["label"])

			return json.dumps(tag.__dict__)