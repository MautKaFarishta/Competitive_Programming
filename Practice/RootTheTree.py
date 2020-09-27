T=int(input())
for _ in range(T):
   N=int(input())
   count=-1
   for _ in range(N-1):
      u,v=map(int,input().split())
      if v==1:
         count+=1
   if count<1:
      print(0)
   else:
      print(count)
