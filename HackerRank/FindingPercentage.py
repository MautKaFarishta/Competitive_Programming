# This code is written by MautKaFarishta
# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
   n = int(input())
   student_marks = {}
   for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
   # print(student_marks)
   query_name = input()
   total=0
   for mark in student_marks[query_name]:
      total+=mark
   a=total/len(student_marks[query_name])
   print("%.2f" % a)