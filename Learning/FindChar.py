s=input()
c=input()
l=len(s)
A=[a for a in range(l) if s[a]==c]

L=[]
for i in range(l):
   L.append(min([abs(x-i) for x in A]))

print(L)

