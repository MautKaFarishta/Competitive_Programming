try:
   TestCases=int(input())
   for _ in range(TestCases):
      Money,ChocPrice,WrapRet=map(int,input().split())
      Chocolates=Wrappers=int(Money/ChocPrice)
      while Wrappers>=WrapRet:
         tempChocolates=Wrappers//WrapRet
         Wrappers-=tempChocolates*WrapRet
         Wrappers+=tempChocolates
         Chocolates+=tempChocolates
      print(Chocolates)
except:
   pass