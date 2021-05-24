def my_fact(n):
    for i in range(n):
        if n <= 1:
            return 1
        else:
            return n*my_fact(n-1)
my_fact(5)


