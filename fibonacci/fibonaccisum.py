n = int(input("n : "))
first=0
second=1
i=0
sum=0
while (i<n):
    sum=sum+first
    next=first+second
    first=second
    second=next
    i=i+1
print(sum)
