try:
   from math import ceil
   T=int(input())
   for _ in range(T):
      N,D=map(int,input().split())
      pat=[int(i) for i in input().split()][:N]
      atRisk=[p for p in pat if p<=9 or p>=80]
      a=len(atRisk);b=len(pat)-len(atRisk)
      print(ceil(a/D)+ceil(b/D))
except:
   pass