import time
try:
   BigNum=10**5+7

   def SummationFunction(SubsSet):
      summation=0
      for substring in SubsSet:
         tempSum=distinct(substring)
         print("TempSum Is------",substring,tempSum)
         if tempSum>BigNum:
            summation+=(tempSum%BigNum)
         else:
            summation+=tempSum
      return summation

   def distinct(P):
      return len(P)**len(set(P))

   def distinctSubstring(str): 
      result = set()
      for i in range(len(str)): 
         for j in range(i + 1, len(str) + 1): 
            result.add(str[i:j])
      return result

   # TestCases=int(input())
   for _ in range(1):
      P=input()
      t0=time.time()
      SubsSet=distinctSubstring(P)
      t1=time.time()
      print(SummationFunction(SubsSet))
      t2=time.time()
   t3=time.time()
   tt=t3-t0
   tc1=(t1-t0)/tt*100
   tc2=(t2-t1)/tt*100
   print(tt,tc1,tc2)


except:
   pass