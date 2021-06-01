class Parent:
    def __init__(self):
        print("calling parent constructor")

    def parentMethod(self):
        print("calling parent method")

#define child1 class
class Child1(Parent):
    def __init__(self):
        print("calling child constructor")

    def childMethod(self):
        print("calling child method1")

#define class child2
class Child2(Parent):
    def __init__(self):
        print("calling child2 constructor")

    def childMethod2(self):
        print("Calling child2 method")

sc = Child2()  #object of child
sc.childMethod2()
sc.parentMethod()