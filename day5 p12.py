#define parent class
class ParentClass():

    def func1(self):
        print("parent method called")

#define child class
class ChildClass():

    def func1(self):
        print("Child method called")

#object of child
c=ChildClass()
c.func1()

#object of parent
p=ParentClass()
p.func1() 