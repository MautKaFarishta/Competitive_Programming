def getMax(a,b,c):
   return abs(a-b)+abs(b-c)+abs(c-a)

try:
   T=int(input())
   for _ in range(T):
      N=int(input())
      In=list(map(int,input().split()))
      In.sort()
      print(max(getMax(In[0],In[1],In[-1]),getMax(In[0],In[-2],In[-1])))

except:
   pass