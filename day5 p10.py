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

#define child class2
class childclass2(MyParentClass1):
    def childMethod2(self):
        print("Child Method2")

c=ChildClass()
c.method_Parent1()
c.method_Parent2()
c.child_method()

c2 = childclass2()
c2.childMethod2()
c2.method_Parent1() 