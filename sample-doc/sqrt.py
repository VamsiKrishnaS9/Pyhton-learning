#this program finds the value of (a+b)2 and (a+b)3

a=int(input("Enter the A value\n"))
b=int(input("Enter the B value\n"))
c=a*a+2*a*b+b*b
print("a+b whole square ",c)
c=a*a*a+3*a*a*b+3*a*b*b+b*b*b
print("a+b whole cube ",c)

