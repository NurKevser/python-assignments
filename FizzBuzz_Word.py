for i in range(1,51):
  if i%5==0 and i%3==0:
    print("FizzBuzz")
  elif i%5 == 0:
    print("Buzz")
  elif i%3 == 0:
    print("Fizz")  
  else:
    print(i)

                   WITH TERNARY CONDITIONS

for i in range(1,51):
  print("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else \
        "Buzz" if i % 5 == 0 else i)
