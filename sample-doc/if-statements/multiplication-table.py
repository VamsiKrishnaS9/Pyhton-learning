# this python program will provide the multiplication table of a given number using if statement

num = int(input("Enter the number : "))
print("Multiplication table of", num)
for i in range(1, 11):
    print(num,"x",i,"=", num * i)