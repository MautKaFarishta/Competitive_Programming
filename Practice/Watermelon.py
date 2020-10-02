T=int(input())
for _ in range(T):
   N=int(input())
   Nlist=list(map(int,input().split()))
   Sum=sum(Nlist)
   if Sum<0:
      print("NO")
   else:
      print("YES")