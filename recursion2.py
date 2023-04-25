def doJob2(n):
    if n<=5:
        return
    doJob2(n-1)
    print(n,end=" ")
    doJob2(n-1)
    print(n,end=" ")
doJob2(8)