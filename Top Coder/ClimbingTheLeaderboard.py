# from collections import Counter
try:
   N=int(input())
   scores=list(map(int,input().split()))[:N]

   # Creating list with unique values and in descending order
   newScores=list(set(scores))
   newScores.sort(reverse=True)
   M=int(input())
   alice=list(map(int,input().split()))[:M]
   # getting index of alice score by deleting overtaken scores
   for aliceScore in alice:
      while len(newScores)>0 and aliceScore>=newScores[-1]:
         del newScores[-1]
      print(len(newScores)+1)
except:
   pass
