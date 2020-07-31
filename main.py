from abc import ABCMeta, abstractmethod

class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

class User(Entity):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

class Group(Entity):
    def __init__(self, name, *members):
        self.children = []
        self.name = name
        if members:
            self.add(*members)

    def add(self, first, *members):
        self.children.append(first)
        if members:
            self.children.extend(members)

    def get_name(self):
        return self.name

def main():
    user_a = User("aaa", 1)
    user_b = User("bbb", 2)

    group_x = Group("XXX", user_a, user_b)

    print(group_x)

    

if __name__ == "__main__":
    main()