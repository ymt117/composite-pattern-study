from entity import Entity
from visitor import Visitor

class User(Entity):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        print(self.name)

    def get_id(self):
        print(self.id)

    def accept(self, visitor):
        visitor.visit_user(self)