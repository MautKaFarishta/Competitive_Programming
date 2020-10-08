def func(arr):
   arr=list(set(arr))
   arr.sort()
   return arr[-1]-arr[1]

lis=list(map(int,input().split()))
print(func(lis))
