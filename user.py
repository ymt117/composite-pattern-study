from entity import Entity

class User(Entity):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        print(self.name)

    def get_id(self):
        print(self.id)