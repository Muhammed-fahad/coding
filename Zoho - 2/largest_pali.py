def largestPalindrome(text):
  pali = ''
  for i in range(len(text)):
    for j in range(len(text)-1,i-1,-1):
      if(text[i:j+1] == text[i:j+1][::-1]):
        if(len(pali) < len(text[i:j+1])):
          pali = text[i:j+1]
  return pali
      

text = input("Enter the text: ")
print("Largest Palindrome: " , largestPalindrome(text))