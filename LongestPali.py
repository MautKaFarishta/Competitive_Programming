#CodeChef
#IARCS OPC Judge Problems
try:
  def isPalindrome(string): 
    for k in range(len(string) // 2):
        if string[k] != string[len(string) - (k + 1)]: return False
    return True

  def LongestPali(length,text):
    K=""
    Max=0
    for i in range(length):
      for j in range(length):
        if i+j<=length:
          K=text[i:i+j]
          if isPalindrome(K) and len(K)>Max:
            Max=len(K)
            pal=K
    print(len(pal))
    print(pal)

  Length=int(input())
  text=input()
  if isPalindrome(text):
    print(Length)
    print(text)
  else:
    LongestPali(Length,text)
except:
  pass

# As we all know, a palindrome is a word that equals its reverse. Here are some examples of palindromes: malayalam, gag, appa, amma.

# We consider any sequence consisting of the letters of the English alphabet to be a word. So axxb,abbba and bbbccddx are words for our purpose. And aaabbaaa, abbba and bbb are examples of palindromes.

# By a subword of a word, we mean a contiguous subsequence of the word. For example the subwords of the word abbba are a, b, ab, bb, ba, abb, bbb, bba, abbb, bbba and abbba.

# In this task you will given a word and you must find the longest subword of this word that is also a palindrome.

# For example if the given word is abbba then the answer is abbba. If the given word is abcbcabbacba then the answer is bcabbacb.

# Input:
# The first line of the input contains a single integer N indicating the length of the word. The following line contains a single word of length N, made up of the letters a,b,…, z.

# Output:
# The first line of the output must contain a single integer indicating the length of the longest subword of the given word that is a palindrome. The second line must contain a subword that is a palindrome and which of maximum length. If there is more than one subword palindrome of maximum length, it suffices to print out any one.

# Constraints:
# 1≤N≤5000.
# You may assume that in 30% of the inputs 1≤N≤300.
# Sample Input 1:
# 5
# abbba
# Sample Output 1:
# 5
# abbba
# Sample Input 2:
# 12
# abcbcabbacba
# Sample Output 2:
# 8
# bcabbacb