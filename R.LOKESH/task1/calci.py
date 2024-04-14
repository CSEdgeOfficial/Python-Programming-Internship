print("SIMPLE CALCULATOR")
A,B=map(int,input("enter space separated numbers:\n").split())
operator=input("enter the operation you want to perform:")
if operator=="+":
    print('addition of {} and {} is {}'.format(A,B,A+B))
elif operator=="-":
    print('Subractin of {} and {} is {}'.format(A,B,A-B))
if operator=="*":
    print('Multiplication of {} and {} is {}'.format(A,B,A*B))
if operator=="/":
    print('Division of {} and {} is {}'.format(A,B,A/B))
if operator=="%":
    print('Remainder of {} and {} is {}'.format(A,B,A%B))
