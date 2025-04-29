a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))

if (a>=b and a>=c and a>=d):
    print(a,"is the largest number")
elif (b>=a and b>=c and b>=d):
    print(b,"is the largest number")
elif(c>=a and c>=b and c>=d):
    print(c,"is largest number")
else:
    print(d,"is the largest number")

