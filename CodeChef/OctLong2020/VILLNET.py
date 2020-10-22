# This code is written by MautKaFarishta

maxval=9999999

def checkKey(dict, key): 
      
    if key in dict.keys(): 
        return True
    else: 
        return False

def solve(x1,y1,fx,fy,c,Dmap):
   if c>6:
      return maxval
   if x1==fx and y1==fy:
      return c
   if checkKey(Dmap,str(x1)+str(y1)):
      if Dmap.get(str(x1)+str(y1))==True:
         return maxval
   Dmap[str(x1)+str(y1)]=True
   d1=solve(x1+2*y1,y1,fx,fy,c+1,Dmap)
   d2=solve(x1-2*y1,y1,fx,fy,c+1,Dmap)
   d3=maxval;d4=maxval
   if 2*x1+y1>0:
      d3=solve(x1,y1+2*x1,fx,fy,c+1,Dmap)
   elif 2*x1+y1<0:
      d3=solve(-x1,-y1-2*x1,fx,fy,c+1,Dmap)
   if -2*x1+y1>0:
      d4=solve(x1,y1-2*x1,fx,fy,c+1,Dmap)
   elif 2*x1+y1<0:
      d4=solve(-x1,-y1+2*x1,fx,fy,c+1,Dmap)
   Dmap[str(x1)+str(y1)]=False

   return min(d1,min(d2,min(d3,d4)))

def solv(x1,y1,fx,fy,c,Dmap):
   if x1>=10 or x1<=-10  or y1<=0 or y1>=10:
      return maxval
   if x1==fx and y1==fy:
      return c
   if checkKey(Dmap,str(x1)+str(y1)):
      if Dmap.get(str(x1)+str(y1))==True:
         return maxval
   Dmap[str(x1)+str(y1)]=True
   d1=solve(x1+2*y1,y1,fx,fy,c+1,Dmap)
   d2=solve(x1-2*y1,y1,fx,fy,c+1,Dmap)
   d3=maxval;d4=maxval
   if 2*x1+y1>0:
      d3=solve(x1,y1+2*x1,fx,fy,c+1,Dmap)
   elif 2*x1+y1<0:
      d3=solve(-x1,-y1-2*x1,fx,fy,c+1,Dmap)
   if -2*x1+y1>0:
      d4=solve(x1,y1-2*x1,fx,fy,c+1,Dmap)
   elif 2*x1+y1<0:
      d4=solve(-x1,-y1+2*x1,fx,fy,c+1,Dmap)
   Dmap[str(x1)+str(y1)]=False

   return min(d1,min(d2,min(d3,d4)))




T=int(input())
for _ in range(T):
   x1,y1,x2,y2=map(int,input().split())

   Dmap={}

   if x1>-10 and x2>-10 and x1<10 and x2<10 and y1>0 and y2>0 and y1 <10 and y2<10:
      print(solv(x1,y1,x2,y2,0,Dmap))
   else:
      print(solve(x1,y1,x2,y2,0,Dmap))
