We have a loud talking parrot. We are in trouble if the parrot is talking and the hour is before 6 or after 21.
Define a function taking two parameters (talking and hour) to return True if we are in trouble. The argument to  talking parameter can only be True or False whether it is talking or not. The argument to hour parameter should be the current hour time in the range of 0 to 23.
For example:

Test	Result
print(parrot_trouble(True, 5))
True
print(parrot_trouble(True, 8))
False
print(parrot_trouble(False, 22))
False


def parrot_trouble(talking, hour):
    if talking ==True and (hour < 6 or hour > 21):
        return True
    else:return False
