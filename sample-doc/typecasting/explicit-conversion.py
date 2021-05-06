#here we are converting a higher value variable (string) to lower value vairable (integer)

num_int = 25
num_str = 50

print("Data type of num_int:",type(num_int))
print("Data type of num_str before type casting:",type(num_str))


num_str = int(num_str)
print("Data type of num_str after type casting:",type(num_str))

num_sum = num_int + num_str

print("Value of num_int and num_str:",(num_sum))
print("Datatype of num_sum:",type(num_sum))




