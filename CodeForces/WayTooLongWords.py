N=int(input())
for _ in range(N):
   s=input()
   if len(s)>10:
      print(s[0]+str(len(s)-2)+s[-1])
      continue
   print(s)
   

