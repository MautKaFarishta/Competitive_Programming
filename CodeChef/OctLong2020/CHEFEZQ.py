from math import ceil
try:   
   T=int(input())
   for _ in range(T):
      n,k=map(int,input().split())
      Q=list(map(int,input().split()))
      days=len(Q);day=0;f=True
      for day in range(1,n):
         # print(day)
         if Q[day-1]>=k:
            Q[day]+=Q[day-1]-k   
         else:
            f=False
            break 
      if f:
         RemQrs=Q[-1]
         if day==n-1:
            day+=(RemQrs)/k
         print(int(day+1))
      else:print(int(day))
except:
   pass

# try:   
#    T=int(input())
#    for _ in range(T):
#       n,k=map(int,input().split())
#       Q=list(map(int,input().split()))
#       RemQus=0
#       days=len(Q);day=0
#       while RemQus>=0:
#          if day<days:
#             RemQus+=Q[day]
#          RemQus-=k
#          day+=1
#       print(day)
# except:
#    pass


