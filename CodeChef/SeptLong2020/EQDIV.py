K=int(input())
T=int(input())
for _ in range(T):
   N=int(input())
   if K==1 or K==2 or K==3 or K==4:
      A=N**K
      B=(N-1)**K
      List=[0]*N
      # print("Length",len(List))
      List[N-1]=1
      List[N-2]=0
      for i in range(N-2,0,-1):
         j=i**K
         # print(i,j)
         if B > A:
            A+=j
            List[i-1]=1
            # print(i,A,B,"Added in A")
         else:
            B+=j
            List[i-1]=0
            # print(i,A,B,"Added in B")
      print(abs(A-B))
      for i in range(N):
         print(List[i],end="")
      print()

         