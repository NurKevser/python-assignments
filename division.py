This question was asked by ContextLogic.
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

def division(x,y):
  toplam = 0
  count = 0
  while toplam != x:
    toplam += y
    count += 1
  return count
division(100,4)
