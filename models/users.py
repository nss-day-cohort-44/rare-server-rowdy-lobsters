class User:

    def __init__(self, id, first_name, last_name, email, username, created_on, account_type_id=1):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.created_on = created_on
        self.account_type_id=account_type_id