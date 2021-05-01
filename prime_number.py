n = int(input("Enter a number: "))
divisions = []

for i in range(2,n):
  for j in range(i+1,n):
    if i*j == n:
      divisions.append((i,j))
      if any(divisions):
        print(f"{i}*{j}, {n} isn't a prime number")
      else:
        print(f"{n} is a prime number")
