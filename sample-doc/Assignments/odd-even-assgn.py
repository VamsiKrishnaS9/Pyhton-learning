# the following program prints even-odd numbers using function

num = int(input("Enter a number for checking odd or even: "))
def find_EvenOdd(num):

    if (num % 2 == 0):
      print(num, "is an even number");
    else:
      print(num, "is an odd number");

find_EvenOdd(num)
