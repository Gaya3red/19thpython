def add():
    try:
        a=int(input())
    except ValueError as err:
        print(err)
    try:
        b=int(input())
    except ValueError as err:
        print(err)
    print(a+b)
add()

def addNumber(a,b):
    return a+b
sum=addNumber(10,30)