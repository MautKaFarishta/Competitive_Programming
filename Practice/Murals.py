from math import ceil
T=int(input())
for _ in range(T):
   N=int(input())
   beauty=input()
   beautyList=[]
   for bty in beauty:
      beautyList.append(int(bty))
   B=0
   B_length=len(beautyList)
   B_indx=ceil(B_length/2)
   for buty in range(B_length-B_indx):
      if sum(beautyList[buty:buty+B_indx])>B:
         B=sum(beautyList[buty:buty+B_indx])
         # print(B,buty,buty+B_indx)
   print(B)


