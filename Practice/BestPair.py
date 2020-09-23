def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
def lcm(a,b): 
    return (a*b) / gcd(a,b) 

N=int(input())
arrset=[int(i) for i in input().split()][:N]
greatestLCM=0
itr=0
for i in arrset:
   itr+=1
   # print("FOr i----->>>",i)
   for j in arrset[itr:]:
      # print("For J--->",j)
      tempLCM=lcm(i,j)
      if tempLCM>greatestLCM:
         greatestLCM=tempLCM

print(int(greatestLCM))
