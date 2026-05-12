def welcome(name):
    print("Welcome",name);

welcome("k")


def add(a,b):
    print(a+b)
add(10,20)


def square(num):
    return num*num
result = square(5)
print(result)

#
def check_even(num):
    if num %2 == 0:
        return "even"
    return "odd"
print(check_even(10))