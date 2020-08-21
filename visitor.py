from abc import ABCMeta, abstractclassmethod

class Visitor(metaclass=ABCMeta):
    @abstractclassmethod
    def visit(self, user):
        pass

class PrintVisitor(Visitor):
    def visit(self, user):
        print('visit user: {} '.format(user.name))