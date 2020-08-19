#CodeChef
#IARCS OPC Judge Problems
try:
  first,second,third=map(int,input().split())
  Voters=[]
  AuthorisedVoters=[]
  for _ in range(first+second+third):
    voter=int(input())
    if Voters.count(voter)==0:
      Voters.append(voter)
    else:
      if AuthorisedVoters.count(voter)==0:
        AuthorisedVoters.append(voter)

  print(len(AuthorisedVoters))

  for voter in AuthorisedVoters:
    print(voter)
except:
  pass