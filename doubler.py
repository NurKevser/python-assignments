Given two integer values, return their sum. If the two values are the same, then return double their sum.




For example:

Test	Result
print(sum_double(1, 2))
3
print(sum_double(5, 7))
12
print(sum_double(5, 5))
20



def sum_double(x, y):
    if x==y :
        return (x+y)*2
    else:
        return x+y
