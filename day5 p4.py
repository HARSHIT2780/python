class MyClass:
    name = " "

    def __init__(self,name):
        self.name = name

    def func1(self):
        print('Name is : ',self.name)

#create a object of MyClass
myc = MyClass("harshit")