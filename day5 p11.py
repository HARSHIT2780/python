#define parent class
class ParentClass():

    def func1(self):
        print("Parent method called")

#define child class
class ChildClass(ParentClass):

    def func1(self):
        print("child method called")

#object of child
c=ChildClass()
c.func1() 