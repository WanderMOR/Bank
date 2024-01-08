class User:
    id = None
    first_name = None
    last_name = None
    email = None
    password = None

    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    

