# this python program will provide the multiplication table of a given number using  for loop

num = int(input("Enter the number : "))
print("Multiplication table of", num)
for count in range(1, 11):
    product = num * count
    print(num, "x", count, "=", product)