# IARCSJUD
# This Code is written by MautKaFarishta

from sys import stdin,stdout

Nums = int(stdin.readline())
Seq = []
for i in range(Nums):
    Seq.append(int(stdin.readline()))
LongSeq = [1] * Nums
for i in range(Nums):
    for j in range(i + 1, Nums):
        if Seq[j] % Seq[i] == 0:
            LongSeq[j] = max(LongSeq[i] + 1, LongSeq[j])
stdout.write(str(max(LongSeq)))

# This problem is about sequences of positive integers a1,a2,...,aN
# . A subsequence of a sequence is anything obtained by dropping some of the elements. For example, 3,7,11,3
#  is a subsequence of 6,3,11,5,7,4,3,11,5,3
#  , but 3,3,7
#  is not a subsequence of 6,3,11,5,7,4,3,11,5,3
#  .

# A fully dividing sequence is a sequence a1,a2,...,aN
#  where ai
#  divides aj
# whenever i<j
# . For example, 3,15,60,720
#  is a fully dividing sequence.

# Given a sequence of integers your aim is to find the length of the longest fully dividing subsequence of this sequence.

# Consider the sequence 2,3,7,8,14,39,145,76,320

# It has a fully dividing sequence of length 3
# , namely 2,8,320
# , but none of length 4
#  or greater.

# Consider the sequence 2,11,16,12,36,60,71,17,29,144,288,129,432,993
# .

# It has two fully dividing subsequences of length 5
# ,

# 2,11,16,12,36,60,71,17,29,144,288,129,432,993
#  and
# 2,11,16,12,36,60,71,17,29,144,288,129,432,993
#  and none of length 6
#  or greater.
# Input:
# The first line of input contains a single positive integer N
#  indicating the length of the input sequence. Lines 2,...,N+1
#  contain one integer each. The integer on line i+1
#  is ai
# .

# Output:
# Your output should consist of a single integer indicating the length of the longest fully dividing subsequence of the input sequence.

# Constraints:
# 1≤N≤10000
# 1≤ai≤1000000000
# Sample input 1:
# 9
# 2 
# 3 
# 7 
# 8 
# 14 
# 39 
# 145 
# 76 
# 320
# Sample output 1:
# 3
# Sample input 2:
# 14
# 2
# 11 
# 16 
# 12 
# 36 
# 60 
# 71 
# 17 
# 29 
# 144 
# 288 
# 129 
# 432 
# 993
# Sample output 2:
# 5