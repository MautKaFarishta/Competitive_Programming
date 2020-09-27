T=int(input())
for _ in range(T):
   N=int(input())
   Nlist=list(map(int,input().split()))
   tpr="YES"
   for i in range(N):
      if (i+1)%Nlist[i]!=0:
         tpr="NO"
         break
   print(tpr)