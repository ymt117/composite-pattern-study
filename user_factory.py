from user import User

class UserFactory():
    __singleton = None

    def __init__(self):
        if UserFactory.__singleton is not None:
            raise Exception("error Singleton")
        else:
            self.__pool = {}
            UserFactory.__singleton = self

    @staticmethod
    def get_instance():
        if UserFactory.__singleton is None:
            UserFactory()
        return UserFactory.__singleton

    def get(self, name, id):
        # 同じユーザのインスタンスが存在するかidで確認する
        user = self.__pool.get(id)

        if user is None:
            user = User(name, id)
            self.__pool[id] = user
        return user