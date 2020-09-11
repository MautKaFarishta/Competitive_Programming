#This Code is written by MautKaFarishta
#Codechef September Long challenge 2020
try:
    def stepUp(N,Pos,Aths):
        for t in range(1,5):
            Pos[t]=[Pos[t-1][i]+Aths[i] for i in range(N)]
        return Pos

    def GoAhead(Pos,N):
        FinalInfected=set()
        infectedForThisRound=[i for i in range(N)]
        # print(infectedForThisRound)
        for infctd in infectedForThisRound:
            Inf=[infctd]
            # print("Infected for this round is----------->",infctd)
            # print("Initial Positions-------->",Pos[0])
            for t in Pos[1:]:
                # print("Getting for Positions--->",infctd,t)
                for INF in Inf:
                    # print("For Infected",INF,"In",Inf)
                    for ath in range(infctd,N):
                        # print("Right Loop",infctd,N,ath)
                        if t[INF]>=t[ath]:
                            if not ath in Inf:
                                Inf.append(ath)
                                # print("Infected are-->",Inf)
                    for ath in range(infctd,-1,-1):
                        # print("Left Loop",infctd,0,ath)
                        if t[INF]<=t[ath]:
                            # print("Here-->>>",t[INF],t[ath])
                            if not ath in Inf:
                                Inf.append(ath)
                                # print("Infected are-->",Inf)
            FinalInfected.add(len(Inf))
            # print("Infected Athletes are---->",len(Inf),Inf)
            # print("\n")
        return min(FinalInfected),max(FinalInfected)

    Tests=int(input())
    for _ in range(Tests):
        TotalAths=int(input())
        Aths=[int(i) for i in input().split()][:TotalAths]
        Positions=[[]]*5
        Positions[0]=[i+1 for i in range(TotalAths)]
        Positions=stepUp(TotalAths,Positions,Aths)
        # print(Aths)
        # for i in Positions:
            # print(i)
        minInf,maxInf=GoAhead(Positions,TotalAths)
        print(minInf,maxInf)
except:
    pass

# There are N
#  athletes (numbered 1
#  through N
# ) in a line. For each valid i
# , the i
# -th athlete starts at the position i
#  and his speed is Vi
# , i.e. for any real number t≥0
# , the position of the i
# -th athlete at the time t
#  is i+Vi⋅t
# .

# Unfortunately, one of the athletes is infected with a virus at the time t=0
# . This virus only spreads from an infected athlete to another whenever their positions are the same at the same time. A newly infected athlete may then infect others as well.

# We do not know which athlete is infected initially. However, if we wait long enough, a specific set of athletes (depending on the athlete that was infected initially) will become infected. Your task is to find the size of this set, i.e. the final number of infected people, in the best and worst possible scenario.

# Input
# The first line of the input contains a single integer T
#  denoting the number of test cases. The description of T
#  test cases follows.
# The first line of each test case contains a single integer N
# .
# The second line contains N
#  space-separated integers V1,V2,…,VN
# .
# Output
# For each test case, print a single line containing two space-separated integers ― the smallest and largest final number of infected people.

# Constraints
# 1≤T≤104
# 3≤N≤5
# 0≤Vi≤5
#  for each valid i
# Subtasks
# Subtask #1 (1 point): N=3

# Subtask #2 (99 points): original constraints

# Example Input
# 4
# 3
# 1 2 3
# 3
# 3 2 1
# 3
# 0 0 0
# 3
# 1 3 2
# Example Output
# 1 1
# 3 3
# 1 1
# 1 2
# Explanation
# Example case 1: No two athletes will ever have the same position, so the virus cannot spread.

# Example case 2: It does not matter who is initially infected, the first athlete would always spread it to everyone.

# Example case 3: The athletes are not moving, so the virus cannot spread.

# Example case 4: The best possible scenario is when the initially infected athlete is the first one, since he cannot infect anyone else. In the worst possible scenario, eventually, the second and third athletes are infected.



#------------------------------------Differant solution but failed-------------
# try:
#     Tests=int(input())
#     for _ in range(Tests):
#         N=int(input())
#         Aths=[int(i) for i in input().split()][:N]
#         max_affctd=0
#         min_affctd=N
#         for infthR in range(N):
#             print("------infthR----------",infthR)
#             affctd=1
#             time=0
#             for i in range(infthR,N-1):
#                 print("Right Check-----",i)
#                 if Aths[i]==Aths[i+1] or Aths[i]==0 or Aths[i+1]==0:
#                     continue
#                 t=1/(Aths[i]-Aths[i+1])
#                 print(Aths[i],Aths[i+1],"t->",t)
#                 if t>0 and t>=time:
#                     affctd+=1
#                     print("Affected -->",affctd)
#                     time=t
#                 else:
#                     continue
#             time=0
#             for i in range(infthR,1,-1):
#                 print("Left Check-----",i)
#                 if Aths[i]==Aths[i-1] or Aths[i]==0 or Aths[i-1]==0:
#                     continue
#                 t=1/(Aths[i]-Aths[i-1])
#                 print(Aths[i],Aths[i-1],"t->",t)
#                 if t>0 and t>=time:
#                     affctd+=1
#                     print("Affected -->",affctd)
#                     time=t
#                 else:
#                     continue
#             if affctd>max_affctd:
#                 max_affctd=affctd
#             if affctd<min_affctd:
#                 min_affctd=affctd

#         print(min_affctd,max_affctd)

                    
# except:
#     pass
# 		