a=int(input("Type the first number."))
b=int(input("Type the second number."))
c=int(input("Type the third number."))
if (a<b) and (a<c):
    print("This is the minimum number",a)
elif (b<a) and (b<c):
    print("This is the minimum number",b)
else:
    print("This is the minimum number",c)

