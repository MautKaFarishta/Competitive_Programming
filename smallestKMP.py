#August Challenge 2020
#Tried This Problem but Test Cases Didn't Passed
try:

  def ArrangeLexically(text,pattern):
    newText=sorted(text)
    for i in range(len(P)):
      newText.remove(P[i])
    text="".join(newText)
    return text

  def Merge(S,P):
    new_S=ArrangeLexically(S,P)
    i=0
    while new_S[i]<=P[0]:
      i+=1
    new_S=new_S[:i]+P+new_S[i:]
    return new_S

  TestCases=int(input())
  for _ in range(TestCases):
    S=input()
    P=input()

    print(Merge(S,P))
except:
  pass