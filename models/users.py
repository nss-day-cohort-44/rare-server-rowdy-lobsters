class User:

    def __init__(self, id, first_name, last_name, email="", username="", password="", created_on="", account_type_id=2):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

        if email != "":
            self.email = email

        if username != "":
            self.username = username

        if password != "":
            self.password = password

        if created_on != "":
            self.created_on = created_on

        self.account_type_id=account_type_id