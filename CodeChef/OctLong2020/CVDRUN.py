try:
   T=int(input())
   for _ in range(T):
      n,k,x,y=map(int,input().split())
      infected=set()
      new=(x+k)%n
      infected.add(new)
      while new!=x:
         new=(new+k)%n
         infected.add(new)
      if y in infected:print("YES")
      else:print("NO")

except:
   pass