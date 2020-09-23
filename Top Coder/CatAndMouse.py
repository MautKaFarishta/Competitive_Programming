try:
   def catAndMouse(A,B,M):
      if abs(A-M)<abs(B-M):
         return 'Cat A'
      if abs(A-M)>abs(B-M):
         return 'Cat B'
      return 'Mouse C'

   Q=int((input()))
   for _ in range(Q):
      Apos,Bpos,Mpos=map(int,input().split())
      print(catAndMouse(Apos,Bpos,Mpos))
except:
   pass