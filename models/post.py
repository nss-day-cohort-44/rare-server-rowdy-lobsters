"""
			SELECT
			p.id,
			p.user_id,
			p.category_id
			p.title,
			p.publication_date,
			p.image_url,
			p.content,
			p.approved
			FROM Posts p
		"""
class Post:
	
	def __init__(self, id, user_id, category_id, title, publication_date, image_url, content, approved = False):
		self.id = id
		self.user_id = user_id
		self.category_id = category_id
		self.title = title
		self.publication_date = publication_date
		self.image_url = image_url
		self.content = content
		self.approved = approved
	