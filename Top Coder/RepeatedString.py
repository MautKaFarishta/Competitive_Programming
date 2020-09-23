from math import floor
try:
    s=input()
    l=int(input())
    length=len(s)
    factor=floor(l/len(s)) #find complete occurances of string
    numofA=s.count('a') #number of "a" in single string
    totalA=factor*numofA #number of a in complete occurances
    rem=l%length
    totalA=totalA+s[:rem].count('a') #number of a in remaining string
    print(totalA)
except:
    pass