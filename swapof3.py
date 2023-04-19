x=int(input("The value of x is : "))
y=int(input( "The value of y is : "))
z=int(input("The value of z is : "))
if(x>y and x>z):
    if(y<z):
        temp=x
        x=y
        y=z
        z=temp
    else:
        temp=x
        x=z
        z=temp
elif (y>x and y>z):
    if(x<z):
        temp=y
        x=z
        z=temp
    else:
        temp=y
        y=x
        x=z
        z=temp
else:
    if(x>y):
        temp=y
        y=x
        x=temp
print("The value of x is : ",x)
print("The value of y is : ",y)
print("The value of z is : ",z)