try:
   def eveodd(X):
      if X%2==0:
         return X/2,X/2
      else:
         a=X//2
         return a,X-a

   T=int(input())
   for _ in range(T):
      A,B=map(int,input().split())
      a,b=eveodd(A);x,y=eveodd(B)
      print(int(a*x+b*y))
except:
   pass