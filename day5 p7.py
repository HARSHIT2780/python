class Parent:

    def __init__(self):
        print("calling parent constructor")

    def parentMethod(self):
        print("calling parent method")

#define child class
class Child(Parent):
    def __init__(self):
        print("calling child constructor")

    def childMethod(self):
        print("calling child method")

#define subchild class
class Subchild(Child):
    def __init__(self):
        print("calling sub child constructor")

    def subchildMethod(self):
        print("Calling subchild method")

sc = Subchild()  #object of sub child
sc.subchildMethod() #sub child class method
sc.childMethod() #child class method
sc.parentMethod() #parent class method