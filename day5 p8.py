class MyParentClass1():

    def method_Parent1(self):
        print("Parent1 method called")

#define parent class 2
class MyParentClass2():

    def method_Parent2(self):
        print("parent2 method called")

#define child class
class ChildClass(MyParentClass1,MyParentClass2):

    def child_method(self):
        print("Child method")

c=ChildClass()  #object of solid
c.method_Parent1()
c.method_Parent2()
c.child_method()