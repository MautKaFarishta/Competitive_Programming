# This code is Written by MautkaFarishta

def Traverse(X,p,lsd,s,N):
   count=0
   if s=="Left":
      while lsd[p-count]>X:
         count+=1
         if p-count==-1:
            break
   elif s=="Right":
      while lsd[p+count]<X:
         count+=1
         if p+count==N:
            break
   return count


T=int(input())
for _ in range(T):
   N,X,p,k=map(int,input().split())
   p-=1;k-=1
   lsd=list(map(int,input().split()))[:N]
   lsd.sort()
   if p<k:
      if X>lsd[p]:
         print(-1)
      else:
         print(Traverse(X,p,lsd,"Left",N))
   elif p>k:
      if X<lsd[p]:
         print(-1)
      else:
         print(Traverse(X,p,lsd,"Right",N))
   else:
      if X<lsd[p]:
         print(Traverse(X,p,lsd,"Left",N))
      elif X>lsd[p]:
         print(Traverse(X,p,lsd,"Right",N))
      else:
         print(0)