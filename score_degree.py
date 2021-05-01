score = int(input("enter your score: "))
if score > 90:
    if score >= 95:
        degree = "A+"
    else:
        degree = "A"
elif score > 80:
    if score > 85:
        degree = "B+"
    else:
        degree = "B"
else:
    degree = "B-"  
print("Your degree is : ", degree)   
