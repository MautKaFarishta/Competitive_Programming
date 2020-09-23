# IARCSJUD
# This Code is written by MautKaFarishta

from sys import stdin,stdout
from bisect import bisect
try:
    Wealths=[]
    for j in range(int(stdin.readline())):
        Merchant=int(stdin.readline())
        count = bisect(Wealths,Merchant)
        pos=len(Wealths)-count+1
        Wealths.insert(count,Merchant)
        stdout.write(str(pos)+'\n')

except:
    pass