from user import User
from group import Group

def main():

    user_A = User("Takeshi", 1)
    user_B = User("Yuki", 2)
    user_A.get_name()
    user_A.get_id()
    user_B.get_name()
    user_B.get_id()

    group_X = Group(user_A, "SUNSHINE")
    group_X.get_name()
    group_X.get_members()

    group_X.add(user_B)
    group_X.get_members()

if __name__ == "__main__":
    main()