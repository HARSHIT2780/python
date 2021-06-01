# Variable Length Arguments

def add(*number):
    sum = 0

    for n in number:
        sum = sum + n
    print("Sum :", sum)

add(10, 30)
add(10, 30, 50)