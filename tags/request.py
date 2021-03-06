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
			ORDER BY Label COLLATE NOCASE
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

			data = db_cursor.fetchone()

			tag = Tag(data["id"], data["label"])

			return json.dumps(tag.__dict__)

def create_tag(new_tag):
    with sqlite3.connect("./rare.db") as conn:
      db_cursor = conn.cursor()

      db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            (?);
        """, (new_tag['label'], ))

      id = db_cursor.lastrowid

      new_tag['id'] = id

    return json.dumps(new_tag)

def delete_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM tags
        WHERE id = ?
        """, (id, ))

def update_tag(id, new_tag):
    with sqlite3.connect("./rare.db") as conn:

        db_cursor = conn.cursor()
		
        db_cursor.execute("""
		UPDATE tags
			SET 
				id = ?,
				label = ?
		WHERE id = ?
		""", ( new_tag['id'], new_tag['label'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True