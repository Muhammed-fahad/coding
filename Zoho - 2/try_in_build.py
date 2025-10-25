def appende(words,word):
  new_words = [None] * (len(words) + 1)
  for i in range(len(words)):
      new_words[i] = words[i]
  words = new_words
  words[len(words)] = word
  return words

def maxi(a,b):
  return a if a>b else b

def spplit(val , delimeter=' '):
  word = ""
  words = []
  for i in val:
    if i==delimeter:
      if word:
        words = appende(words,word)
        word = ""
    else:
      word+=i
  if word:
    words.append(word)
  return words

val = input("Enter a string: ")
print(spplit(val))