Arrlen,N=map(int,input().split())
Arr=[0]*Arrlen

for _ in range(N):
   I_indx,L_indx=map(int,input().split())
   for i in range(I_indx,L_indx+1):
      Arr[i-1]+=1
# print(Arr)

maxEL=max(Arr)
maxFound=False
Ranges=0
RangesInDetail=[]
specialItr=0
for i in range(Arrlen):
   if Arr[i]==maxEL:
      if maxFound:
         RangesInDetail[specialItr-1]+=1
      else:
         maxFound=True
         Ranges+=1
         RangesInDetail.append(i+1)
         RangesInDetail.append(i+1)
         specialItr+=2

   else:
      maxFound=False

print(Ranges)
for itr in range(0,len(RangesInDetail),2):
   print(RangesInDetail[itr],RangesInDetail[itr+1])

