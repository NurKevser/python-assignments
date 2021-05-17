Given a string, return a new string where the first and last chars have been exchanged.
For example:

Test	Result
print(front_back('clarusway'))
ylaruswac
print(front_back('a'))
a
print(front_back('ab'))
ba



def front_back(word):
    xx = list(word)
    ilk= word[0]
    xx[0] = xx[-1]
    xx.pop(-1)
    xx.append(ilk)
    result = "".join(xx)
    return result



