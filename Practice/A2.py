import math 
  
def isPerfectSquare(x): 
   s = int(math.sqrt(x)) 
   return s*s == x 

def isFibonacci(n): 
   return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def getFibOutput(n):
   if isFibonacci(n):
      print(n)
   else:
      fiblis=[0,1];i=2;final=0
      while fiblis[-1]<n:
         fiblis.append(fiblis[i-2]+fiblis[i-1])
         i+=1
      fiblis.pop()
      for fib in fiblis:
         if fib%2==0:
            final+=fib
      print(final)

getFibOutput(int(input()))