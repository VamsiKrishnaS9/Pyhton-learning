# this python program will provide the multiplication table of a given number

num = int(input("Enter your number : "))
print("Multiplication table of", num)
for i in range(1, 21):
    print(num,"x",i,"=", num * i)