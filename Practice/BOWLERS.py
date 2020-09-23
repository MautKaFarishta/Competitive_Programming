for _ in range(int(input())):
  overs,bowlers,mx = list(map(int,input().split()))
  if (bowlers<=1 and overs>1) or (bowlers*mx < overs):
    print(-1)
  else:
    l = list(range(1,bowlers+1))
    for o in range(overs):
      print(l[o%bowlers],end=' ')
    print()