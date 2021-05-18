

```
# Asama 1.
·     Encode isimli bir fonksiyon olusturacagiz.
·     Bu fonksiyonla, bize verilen string de yer alan tum kucuk sesli harfleri numaralarla degistirecegiz.
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
Ornek: string = ‘hello’  istenilen sonuc ‘h2ll4’
Asama 2.
·     Decode isimli bir fonksiyon olusturacagiz
·     Bize verilen stringde yer alan numaralari kucuk sesli harflere cevirecegiz.
1 -> a
2 -> e
3-> i
4 -> o
5 -> u
Ornek: string = ‘h3 th2r2’ istenilen sonuc ‘hi there’
Testler:
string = 'hello' ,  encode = 'h2ll4' decode = ‘hello’
string = 'How are you today?' encode = 'H4w 1r2 y45 t4d1y?' decode =  'How are you today?' 
string = 'This is an encoding test.'  ' encode = ‘Th3s 3s 1n 2nc4d3ng t2st.' decode = 'This is an encoding test.'

```

def change_vowels(string):
  vowels = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
  new=''
  for j in string:
    if j in vowels.keys():
      j = vowels[j]
      new += j
    else:
      new += j  
    if j in vowels.values() 
  return new   


                        WITH MAKETRANS


def encode(st):
    transTable = st.maketrans('aeiou', '12345')
    return st.translate(transTable)
def decode(st):
    transTable = st.maketrans('12345', 'aeiou')
    return st.translate(transTable)                        


