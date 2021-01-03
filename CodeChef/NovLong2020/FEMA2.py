def getAttractions(mags,irons,K,S):
   m=set();i=set()
   for mag in mags:
      # print("For Magnet:" ,mag," in",mags)
      for ir in irons:
         # print("for Irons: ",ir," in ",irons)
         if mag>ir:
            if ( K+1-(mag-ir)-S[ir:mag].count(":") ) >= 0:
                  m.add(mag);i.add(ir)
                  # print(mags,irons,mag,ir)
         elif mag<ir:
            if ( K+1-(ir-mag)-S[mag:ir].count(":") ) >= 0:
                  m.add(mag);i.add(ir)
   return min(len(m),len(i))

# ( K+1-(mag-ir)-S[ir:mag].count(":") ) >= 0:
T=int(input())
for _ in range(T):
   mags=[];irons=[];attractions=0
   N,K=map(int,input().split())
   S=input()
   for obj in range(N):
      if S[obj]=="M":
         mags.append(obj)
      elif S[obj]=="I":
         irons.append(obj)
      elif S[obj]=="X":
         attractions+=getAttractions(mags,irons,K,S)
         mags=[];irons=[]
   attractions+=getAttractions(mags,irons,K,S)
   print(attractions)
