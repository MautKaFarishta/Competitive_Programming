Days,Hours=map(int,input().split())
minHrs=[0]*Days
maxHrs=[0]*Days
for i in range(Days):
   minHrs[i],maxHrs[i]=map(int,input().split())

print(minHrs,maxHrs)

if sum(minHrs)>Hours or sum(maxHrs)<Hours:
   print("NO")
else:
   