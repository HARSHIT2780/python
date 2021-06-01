class MyClass:
    n1=0
    n2=0
    #constructor
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    #Function
    def func1(self):
        ans=self.n1+self.n2
        print('Ans is : ',ans)

#Create a object of MyClass
myc = MyClass(10,20)

#calling function
myc.func1() 