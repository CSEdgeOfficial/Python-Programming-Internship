def add(x,y):
    return x+y 
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def moddiv(x,y):
    return x%y
print("ENTER 1.ADDITION \n\n 2.SUBTRACTION \n\n 3.MULTIPLICATION \n\n 4.DIVISION \n\n 5.MODULUS_DIVISION\n\n 6.EXIT\n\n")
#ch=int(input("Enter Your Choice:"))
n=int(input("enter no of operations you want to do:").upper())
for i in range(1,n+1):
 ch=int(input("Enter Your Choice:"))
 if ch==1:
    x=int(input("enter x value:").capitalize())
    y=int(input("enter x value:").capitalize())
    print("THE SUM OF",x,"AND",y,"IS",add(x,y))
 elif ch==2:
    x=int(input("enter x value:").capitalize())
    y=int(input("enter x value:").capitalize())
    print("THE SUBTRACTION OF",x,"AND",y,"IS",sub(x,y))
 elif ch==3:
    x=int(input("enter x value:").capitalize())
    y=int(input("enter x value:").capitalize())
    print("THE MULTIPLICATION OF",x,"AND",y,"IS",mul(x,y))
 elif ch==4:
    x=int(input("enter x value:").capitalize())
    y=int(input("enter x value:").capitalize())
    print("THE DIVISION OF",x,"BY",y,"IS",div(x,y))
 elif ch==5:
    x=int(input("enter x value:").capitalize())
    y=int(input("enter x value:").capitalize())
    print("THE MODDIVISON OF",x,"AND",y,"IS",moddiv(x,y))
 else:
    exit()