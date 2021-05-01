age = input("Enter your age : ")
while not age.isdigit() :
    print("You entered incorrectly!")
    age = input("Enter your age correctly please : ")
print("Great! You entered valid age :", age)
