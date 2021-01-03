L=[8,6,6,5,3,3,1]
for i in range(len(L)-1):
   print(bin(L[i]^L[i+1]))