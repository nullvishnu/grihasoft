
import json
class User_Response:
    id = None
    name = None
    username = None
    password = None
    status = 1
    data = []

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_username(self, username):
        self.username = username

    def set_status(self, status):
        self.status = status

    def set_data(self, data):
        self.data = data

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_status(self):
        return self.status

    def get_data(self):
        return self.data
