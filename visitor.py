from abc import ABCMeta, abstractclassmethod
import json

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
        print('"', end='')
        print(group.name, end='')
        print('": ', end='')

        print('[')
        for i in range(len(group.members)):
            print('\t', end='')
            print(json.dumps(vars(group.members[i])))
        print(']')