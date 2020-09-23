N=int(input())

for _ in range(N):
   s=input()
   if len(s)>1 and s[0]=='a' and s[-1]=='a':
      print("Yes")
   else:
      print("No")
