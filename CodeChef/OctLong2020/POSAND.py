# get_bin = lambda x, n: format(x, 'b').zfill(n)
# for i in range(1,10):
   # print(get_bin(i,4))
import math
def Log2(x):
   if x == 0:
      return False
 
   return (math.log10(x) /
      math.log10(2))
def isPowerOfTwo(n):
   return (math.ceil(Log2(n)) ==
      math.floor(Log2(n)))

T=int(input())
for _ in range(T):
   N=int(input())
   if N==1:
      print(1)
      continue
   if isPowerOfTwo(N):
      print(-1)
      continue
   else:
      ans=list(range(1,N+1))
      ans[0]=2
      ans[1]=3
      ans[2]=1
      ele=3
      while ele<N:
         if isPowerOfTwo(ans[ele]):
            ans[ele],ans[ele+1]=ans[ele+1],ans[ele]
            ele+=1
         ele+=1
      for i in range(N):
         print(ans[i],end=" ")
      print()


