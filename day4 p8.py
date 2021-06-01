#Example With Keyword Arguments

def func(**arg):
    for i,j in arg.items():
        print(i,j)

func(Name ='Harshit',Lastname = 'soni')