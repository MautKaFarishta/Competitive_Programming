# IARCSJUD
# This Code is written by MautKaFarishta
try:
    def NextPerm(Perm):
        i=j=len(Perm)-1
        while i > 0 and Perm[i-1] >= Perm[i]:
            i-=1
        if i<=0:
            return False
        while Perm[j] <= Perm[i-1]:
            j-=1
        Perm[i-1],Perm[j]=Perm[j],Perm[i-1]
        Perm[i : ] = Perm[len(Perm) - 1 : i - 1 : -1]
        return True

    N,K=map(int,input().split())
    Perm=[]
    for _ in range(K):
        Perm=list(map(int,input().split()))
        NextPerm(Perm)
        for digit in Perm:
            print(digit,end=" ")
        print()
        
except:
    pass

# It is an interesting exercise to write a program to print out all permutations of 1,2,…,n
# . However, since there are 6227020800
#  permutations of 1,2,…,13
# , it is unlikely that we would ever run this program on an input of size more than 10
# .

# However, here is another interesting problem whose solution can also be used to generate permutations. We can order the permutations of 1,2,…,n
#  under the lexicographic (or dictionary) order. Here are the permutations of 1,2,3
#  in lexicographic order:

# 123132213231312321

# The problem we have is the following: given a permutation of 1,2,…,n
# , generate the next permutation in lexicographic order. For example, for 2314
#  the answer is 2341
# .

# Input:
# The first line of the input contains two integers, N
#  and K
# . This is followed by K
# lines, each of which contains one permutation of 1,2,…,N
# .

# Output:
# The output should consist of K
#  lines. Line i
#  should contain the lexicographically next permutation correponding to the permutation on line i+1
#  in the input.

# Constraints:
# 1≤N≤1000
# .
# 1≤K≤10
# .
# Sample input
# 3 2
# 3 1 2
# 2 3 1
# Sample output
# 3 2 1
# 3 1 2 