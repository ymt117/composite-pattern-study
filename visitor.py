from abc import ABCMeta, abstractclassmethod

class Visitor(metaclass=ABCMeta):
    @abstractclassmethod
    def visit_user(self, user):
        pass

    def visit_group(self, group):
        pass

class PrintVisitor(Visitor):
    def visit_user(self, user):
        print('visit user name: {}'.format(user.name))
        print('visit user id: {}'.format(user.id))

    def visit_group(self, group):
        print('visit group name: {}'.format(group.name))
        print('[')
        for i in range(len(group.members)):
            print('\t', end='')
            print(vars(group.members[i]))
        print(']')