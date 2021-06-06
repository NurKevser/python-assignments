find the missing character. generalize solution
["f","a","b","c","e"] -----> 'd'



liste = ["h","d","a","b","f","c","e"]

res = []
for i in liste:
    res.extend(ord(num) for num in i)
res

[104, 100, 97, 98, 102, 99, 101]


def missing_char(liste):
  res = []
  for i in liste:
    res.extend(ord(num) for num in i)
    for j in range(min(res),max(res)):
      if chr(j) not in liste:
        return chr(j)

missing_char(["f","a","b","c","e"])
'd'
