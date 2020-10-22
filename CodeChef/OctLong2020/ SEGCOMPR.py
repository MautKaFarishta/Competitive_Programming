# This code is written by MautKaFarishta
# Try Attempt Code not accepted
import math

def setBitNumber(n): 
   if n==0:
      return 0
   k = int(math.log(n,2)) 
   return 2**k 

def getSegment(ls):
   n=len(bin(max(ls)))-2
   xor=[0]*n
   for dig in ls:
      b=bin(dig);itr=n-1
      for j in reversed(b):
         if j=="1":
            xor[itr]+=1
         if j=="b":
            break
         itr-=1
   print(ls)
   print(xor)
   it=n-1
   for x in xor:
      if x%2!=0:
         break
      it-=1
   if it==-1:return 0
   return 2**it


N=10# N=int(input())
digs=[0,1,2,3,4,5,6,7,8,9]# digs=list(map(int,input().split()))[:N]
final=0

digs.sort()
for i in range(N):
   for j in range(i,N):
      f=getSegment(digs[i:j+1])
      final+=f
      print("Final+",f,final)
print(final)




# def setBitNumber(n): 
#    if n==0:
#       return 0
#    k = int(math.log(n,2)) 
#    return 2**k 

# def getSegment(lst):
#    print(lst)
#    for digit in lst:
#       print(bin(digit),end=" ")
#    print()
#    if len(lst)==1:
#       # return [0]
#       lst[0]=setBitNumber(lst[0])
#    for i in range(len(lst)-1,0,-1):
#       sig=setBitNumber(lst[i]^lst[i-1])      
#       print(lst[i],lst[i-1],"-XOR-->",sig)
#       lst.pop();lst.pop()
#       lst.append(sig)
#    return lst


# N=int(input())
# digs=list(map(int,input().split()))[:N]
# final=0
# # ls=[15,14,13,12,11,10,9,8]
# # print(getSegment(ls))
# co=0
# digs.sort()
# for i in range(N):
#    for j in range(i,N):
#       f=getSegment(digs[i:j+1])
#       final+=max(f)
#       print(final-max(f),"+=-------->",f)

# print(co,final)

