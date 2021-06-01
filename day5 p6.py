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


c=Child()  #object of child
c.childMethod() #child class method
c.parentMethod() #parent class method
