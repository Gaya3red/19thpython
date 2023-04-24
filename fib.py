def Fibonacci (n):
    if n < 0:
        print("Incorrect input")
        return
    elif n == 0:
        print(0)
        return 
    elif n == 1 or n == 2:
        print(1)
        return 
    a=0
    b=1
    print(a," ",b)
    count = 3
    while(count<=n):
        next = a+b
        print(next,end = " ")
        a=b
        b=next
        count+=1
Fibonacci(9)
