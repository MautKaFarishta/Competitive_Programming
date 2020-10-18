# cook your dish here
# print(5%4,(-5)%(-4))
T=int(input())
for _ in range(T):
   L,R=map(int,input().split())

   if L==1 or L*2<=R:
      print(-1)
   else:
      print(R)

