S=input()
vovels='aeiouAEIOU'
ourString=''
letfnd=False
for letter in S:
   # print(letter)
   if letfnd:
      if letter in vovels:
         ourString+=letter
      else:
         letfnd=False
         print(ourString)
         ourString=''
   else:
      if letter in vovels:
         ourString+=letter
         letfnd=True
      
