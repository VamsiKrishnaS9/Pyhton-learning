# this program will print your result using if/elif/else conditions

score = int(input("Enter your score: "))
if score > 100 or score <0:
    print("Sorry, invalid code")
elif score >= 40:
    print("You've passed the test ")
    print("Congratulations")
else:
    print("Sorry, you've failed the test")