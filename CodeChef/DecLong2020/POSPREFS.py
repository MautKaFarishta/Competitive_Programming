try:
   T=int(input())
   for _ in range(T):
      N,K=map(int,input().split())
      if N==1 and K==1:
         print(1)
         continue
      Lst=[];L=N-1;M=K 
      while L>=0:
         if M>0:
            Lst.append(N-L);L-=1
            if M>0 and L>=0:
               Lst.append(-(N-L));L-=1;M-=1
         else:
            Lst.append(-(N-L));L-=1
      if N%2==1:M-=1
      for el in range(len(Lst),0,-1):
         if M>0:
            if Lst[el-1]<0:
               Lst[el-1]=el
               M-=1
         else:
            break

      for l in Lst:
         print(l,end=" ")
      print()
except:
   pass

