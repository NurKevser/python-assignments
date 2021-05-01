exp_list = [11, 2, 24, 61, 48, 33, 3]
even = 0
odd = 0
for i in exp_list:
  if i%2 == 0:
    even += 1
  else:
    odd += 1  
print("The number of even numbers :",even)
print("The number of odd numbers :",odd)  
