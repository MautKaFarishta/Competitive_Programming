# This code is written by MautKaFarishta
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
   N=int(input())
   Data=[]
   Scores=[]
   for _ in range(N):
      name = input()
      score = float(input())
      Data.append([name,score])
      Scores.append(score)

for _ in range(Scores.count(min(Scores))):
   Scores.remove(min(Scores))
SecondMinScore=min(Scores)
LowScoreStudents=[]

for studentData in Data:
   if studentData[1]==SecondMinScore:
      LowScoreStudents.append(studentData[0])
LowScoreStudents.sort()
for j in LowScoreStudents:
   print(j)

