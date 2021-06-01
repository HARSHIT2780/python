# Example With Multiple Return Statement

def Function4():
    name1 = 'Harry'
    contact = 762333322
    return name1, contact


name1, contact = Function4()
print('Name :', name1)
print('Contact :', contact)