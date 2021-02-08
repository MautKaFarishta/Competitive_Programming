def convert24(str1): 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
    elif str1[-2:] == "AM": 
        return str1[:-2]  
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
    else:
        return str(int(str1[:2]) + 12) + str1[2:5] 
  
def toPoints(st):
   A=convert24(st)
   A=A.strip()
   x=int(A[-2:])
   C=int(A[:2])+(x/60)
   return C-24 if C>=24 else C

# Driver Code      
T=int(input())
for _ in range(T):
   OP=""
   Ctime=toPoints(input())
   F=int(input())
   for _ in range(F):
      t=input()
      t1=toPoints(t[:8]);t2=toPoints(t[9:])
    #   print(f'{t1:.3f} {Ctime:.3f} {t2:.3f}')
      if Ctime>=t1 and Ctime<=t2:
         OP=OP+'1'
      else:
         OP=OP+'0'
   print(OP)
