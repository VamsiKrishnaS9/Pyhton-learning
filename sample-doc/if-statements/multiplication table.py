# printing multiplication table using while statement 

num = int(input("Enter a number : "))
print("Multiplication table of", num)
count = 1
while count <= 10:
    product = num * count
    print(num, "x", count, "=", product)
    count = count +1