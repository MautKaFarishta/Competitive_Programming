from sys import stdin,stdout

try:
    N=int(stdin.readline())
    Nums=[]
    S={}
    for _ in range(N):
        Element=int(stdin.readline())
        Nums.append(Element)
        if Element in S:
            S[Element]+=1
        else:
            S[Element]=1
    AvgCount=0
    for i in range(N-1):
        for j in range(i+1,N):
            tempAvg=(Nums[i]+Nums[j])
            if tempAvg%2==0:
                tempAvg=tempAvg/2
                if tempAvg in S:
                    AvgCount+=S[tempAvg]
                    S[tempAvg]=0
    stdout.write(str(AvgCount))

except:
    pass