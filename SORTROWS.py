# IARCSJUD
# This Code is written by MautKaFarishta
try:
    NumberOfRows=int(input())
    RowOfRows=[]
    for i in range(NumberOfRows):
        Row=list(map(int,input().split()))
        RowOfRows.append(Row)
    RowOfRows.sort()
    for singleRow in RowOfRows:
        singleRow.remove(-1)
        for num in range(len(singleRow)):
            print(singleRow[num],end=" ")
        print()

except:
    pass

# You will be given several lines of input where each line contains a sequence of positive integers. Your task is to sort these lines in lexicographic order. Lexicographic order is the order in which words are listed in the dictionary. The ordering is determined by the left most element (in this case the left most integer on each line) and if the left most elements are equal then by the second element from the left, if the left most and the second element from the left are equal then by the third element from the left and so on.

# For example, when the lines


#   14   38   11   89
#   27   34
#   27   12   34
#   27
#   92    2    3    1
#   17    2

# are sorted in the lexicographic order we get


#   14   38    11   89
#   17    2
#   27
#   27   12    34
#   27   34
#   92    2     3    1

# Input:
# The first line of the input contains a single integer N
#  indicating the number of lines of input. This is followed by N
#  lines (lines 2
#  through N+1
# ) each which consists of a sequence of positive integers followed by a single −1
# . (The −1
#  is there just as an end marker and is not to be used in the sorting). Every line contains at the most 50
#  numbers.

# Output:
# N
#  lines each containing a sequence of integers. These N
#  lines must be the lexicographically sorted presentation of the N
#  input lines.

# Constraints:
# 1≤N≤1000
# .
# There are at the most 50
#  integers on each line.
# Sample input:
# 6
# 14 38 11 89 -1
# 27 34 -1
# 27 12 34 -1
# 27 -1
# 92 2 3 1 -1
# 17 2 -1
# Sample output:
# 14 38 11 89 
# 17 2 
# 27 
# 27 12 34 
# 27 34 
# 92 2 3 1