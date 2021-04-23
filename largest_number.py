x = int(input("How many numbers will you enter: "))
y = 0
numbers = []
while y != x:
  numbers.append(int(input("Please enter a number: ")))
  y += 1
print("The largest number is ", sorted(numbers)[-1])
   
