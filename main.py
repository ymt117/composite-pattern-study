from user import User
from group import Group

def main():

    user_A = User("Takeshi", 1)
    user_B = User("Yuki", 2)
    user_A.get_name()
    user_A.get_id()
    user_B.get_name()
    user_B.get_id()

    class_A = Group(user_A, "class A")
    class_A.get_name()
    class_A.get_members()
    
    class_A.add(user_B)
    class_A.get_name()
    class_A.get_members()

    school = Group(class_A, "SUNSHINE School")
    school.get_name()
    school.get_members()

if __name__ == "__main__":
    main()