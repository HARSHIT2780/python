#default constructor example




class myclass:
    name = " "

    def func1(self):
        print('hey')

    def func2(self, name):
        self.name = name

    def show(self):
        print('value is' , self.name)

        m1 = myclass()
        m1.func1()
        m1.func2('harshit')
        m1.show()



