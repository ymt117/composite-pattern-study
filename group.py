from entity import Entity

class Group(Entity):
    def __init__(self, member, name):
        self.members = []
        self.members.append(member)
        self.name = name

    def get_name(self):
        print(self.name)

    def get_members(self):
        print(self.members)

    def add(self, member):
        self.members.append(member)