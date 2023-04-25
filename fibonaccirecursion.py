def recurFib(n):
    if n<=1:
        return n
    else:
        return(recurFib(n-1)+recurFib(n-2))
n=10
if n <=0:
    print("Invalid number")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(recurFib(i))