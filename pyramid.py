for number in range(10):
  print(number*str(number))
for i in range(8,0,-1):
  print(i*str(i)) 


1
22
333
4444
55555
666666
7777777
88888888
999999999
88888888
7777777
666666
55555
4444
333
22
1


for i in range (10):
  if i % 2:
    print((f"{i-1}" * i).center(len(range(10))), end="  ")
    print((f"{i}" * i).center(len(range(10))))

    0           1     
   222         333    
  44444       55555   
 6666666     7777777  
888888888   999999999
