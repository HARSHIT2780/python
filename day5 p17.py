class cal4:

    def setdata(self,n1):
        self.num = n1

    def display(self):
        return self.num*self.num
        #print("Square of given number is ",self.sum)


c=cal4()
c.setdata(4)
print(c.display())