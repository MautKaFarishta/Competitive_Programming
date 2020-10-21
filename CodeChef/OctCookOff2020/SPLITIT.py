# This code is written by MautKaFarishta
T=int(input())
for _ in range(T):
   N=int(input())
   S=input()
   if S[-1:] in S[:N-1] :
      print("YES")
   else:
      print("NO")
