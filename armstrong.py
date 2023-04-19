##print ('Hello World')
num=int(input("Enter a number : "))
temp=num
sum=0
while (num!=0):
    rem=num %10
    sum = sum+(rem*rem*rem)
    num=int(num/10)
if (sum == temp):
    print(temp,"is armstrong number")
else:
    print(temp,"is not a armstrong number")