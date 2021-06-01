class employee:

    def __init__ (self,name,designation):
        self.name=name
        self.designation=designation

class subclass(employee):

    def __init__ (self,name,designation,salary):
        print("Name : ",name," Designation : ",designation," Salary : ",salary)

cf=subclass("harshit","Data Analyst","35000")