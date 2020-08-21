from user import User
from user_factory import UserFactory
from group import Group
from visitor import PrintVisitor

def main():

    user_factory = UserFactory.get_instance()

    user_A = user_factory.get("Takeshi", 1)
    user_B = user_factory.get("Yuki", 2)
    user_A.get_name()
    user_A.get_id()
    user_B.get_name()
    user_B.get_id()

    # Flyweightパターンを実装したので、
    # 同じインスタンスidが出力される
    user_X = user_factory.get("Takeshi", 1)
    print(id(user_A))
    print(id(user_X))

    class_A = Group(user_A, "class A")
    class_A.get_name()
    class_A.get_members()
    
    class_A.add(user_B)
    class_A.get_name()
    class_A.get_members()

    school = Group(class_A, "SUNSHINE School")
    school.get_name()
    school.get_members()

    user_A.accept(PrintVisitor())
    class_A.accept(PrintVisitor())

if __name__ == "__main__":
    main()