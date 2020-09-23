try:
    def fillWater(N,Blocks):
        Water=0
        for blockIndex in range(N):
            leftMax=max(Blocks[:blockIndex+1])
            if not blockIndex==N:
                rightMax=max(Blocks[blockIndex:])
            Water=Water+min(leftMax,rightMax)-Blocks[blockIndex]
        return Water
            
    N=int(input())
    Blocks=[int(i) for i in input().split()][:N]
    print(fillWater(N,Blocks))

except:
    pass