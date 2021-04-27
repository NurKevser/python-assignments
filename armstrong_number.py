number = input("Enter a n-digit number: ")
powers = []
while number.isdigit()==False:
  number = input("It is invalid entry. Don't use non-numeric, float, or negative values! ")
for i in sorted(number):
  powers.append(int(i)**len(sorted(number)))
if sum(powers) == int(number):
  print(f"{number} is an Armstrong number")
else:
  print(f"{number} is not an Armstrong number")  
