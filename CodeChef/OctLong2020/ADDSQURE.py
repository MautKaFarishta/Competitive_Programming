import time
from random import randint
from bitarray import bitarray

class mybitarray(bitarray):
    def __lshift__(self, count):
        return self[count:] + type(self)('0') * count
    def __rshift__(self, count):
        return type(self)('0') * count + self[:-count]
    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, self.to01())

W=10;H=10;N=3;M=3
Vertical=[3,6,8]
Horizontal=[1,6,10]

# W,H,N,M=map(int(input()))
# Vertical=list(map(int,input().split()))
# Horizontal=list(map(int,input().split()))

# Vertical=list(randint(0,W) for i in range(N))
# Horizontal=list(randint(0,H) for i in range(M))

A=B=bitarray(W)
C=D=bitarray(H)

A.setall(0);B.setall(0);C.setall(0);D.setall(0)
A=mybitarray(A);B=mybitarray(B)


for i in range(1,len(Vertical)):
   diff=Vertical[i]-Vertical[i-1]
   A[diff]=1
   print("Diff and A",diff,A)
   B>>diff
   B[diff]=1   
   print("B",B)
   A=A or B
   print(A)

# print(len(A),A)





# Vertical=list(randint(0,W) for i in range(N))
# Horizontal=list(randint(0,H) for i in range(M))


# t1=time.time()
# HDiff=set();VDiff=set();Conf=set();Final=set()


# for i in range(len(Vertical)):
#    for j in range(i+1,len(Vertical)):
#       VDiff.add(abs(Vertical[i]-Vertical[j]))

# for i in range(len(Horizontal)):
#    for j in range(i+1,len(Horizontal)):
#       HDiff.add(abs(Horizontal[i]-Horizontal[j]))

# Conf=VDiff.intersection(HDiff)
# # print(HDiff,VDiff,Conf)


# for line in range(1,H+1):
#    if line in Horizontal:
#       continue
#    else:
#       newDiff=set()
#       for anyLine in Horizontal:
#          newDiff.add(abs(anyLine-line))
#       Final.add(len(Conf.union(newDiff.intersection(VDiff))))
       
# t2=time.time()_--_-_-_-_-_--_-_-_-_-_-_-_----_---_-_-_-_-_-_-_-_-_----_-_-_-_-__