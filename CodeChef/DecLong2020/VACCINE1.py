try:
   D1,V1,D2,V2,P=map(int,input().split())
   currV=0;day=1
   while currV<P:
      if day>=D1:
         currV+=V1
      if day>=D2:
         currV+=V2
      day+=1
      # print(currV,day)
   print(day-1)
except:
   pass
      