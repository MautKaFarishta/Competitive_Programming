# This Code is written by MautKaFarishta
# https://www.hackerrank.com/challenges/python-lists/problem

N=int(input())
L=[]
for _ in range(N):
   opr=list(input().split())
   if len(opr)==1 and opr[0]=='print':
      print(L)
   elif len(opr)==1:
      exec('L.'+opr[0]+'()')
   elif len(opr)==2:
      exec('L.'+opr[0]+'('+opr[1]+')')
   elif len(opr)==3:
      exec('L.'+opr[0]+'('+opr[1]+','+opr[2]+')')     

