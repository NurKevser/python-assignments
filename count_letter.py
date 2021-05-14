def count_letter(sentence):
  dicto = {}
  for i in sentence:
    dicto[i]=sentence.count(i)
  return dicto
count_letter('hippo runs to us !') 
