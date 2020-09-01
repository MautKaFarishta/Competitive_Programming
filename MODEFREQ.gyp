try:
    Tests=int(input())
    for _ in range(Tests):
        N=int(input())
        Numbers=[int(i) for i in input().split()][:N]
        print(Numbers)
except:
    pass