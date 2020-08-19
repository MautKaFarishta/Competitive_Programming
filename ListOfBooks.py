#CodeChef
#IARCS OPC Judge Problems
try:
  numberOfBooks=int(input())
  Books=[int(i) for i in input().split()][:numberOfBooks]
  registerEntries=int(input())
  register=[]
  for i in range(registerEntries):
    bookNumber=int(input())
    borrowed=Books.pop(bookNumber-1)
    register.append(borrowed)
  for book in register:
    print(book)
except:
  pass

# This is another problem about Indraneel's library. His library has one long shelf. His books are numbered and he identifies the books by their number. Each book has a distinct number.

# He has lost many books, since many of his friends borrow his books and never bother to return them. He does not want to lose any more books and has decided to keep a record of all books that he lends to his friends. To make the task of borrowing a book a little difficult, he has given the following instructions to his friends: when they borrow a book, they must record in a register its position from the left among the books currently on the shelf.

# Suppose there are 5 books in the library and they are arranged as follows:

# 26142153
# If someone walks in and borrows the book 42, then he will record 3 in the register because this book is the third from the left on the shelf. Now the shelf looks like this:

# 261153
# If the next person borrow the book 3, he writes down 4 in the register since this is currently the fourth book from the left on the shelf, and so on.

# Indraneel knows the initial arrangement of the books in his library at the time that he introduced the register system. After a while he examines his register and would like to know which books have been borrowed. Your task is to write a program to help Indraneel solve this problem.

# Input:
# The first line of the input contains a single integer M indicating the number of books in Indraneel's library. The next line contains M distinct positive integers describing the sequence in which the books are arranged on the library shelf. The third line of input contains a single integer N indicating the number of entries in the register. This, in turn, is followed by N lines (lines 4 to N+3), each containing one positive integer. The integer on line 3+i indicates the position from left of the book ith book borrowed. (You may assume that the number on line 3+i is at most M−i+1.)

# Output:
# N lines with one positive integer on each line. The number on line i is the book borrowed by the ith borrower.

# Constraints:
# 1≤M≤1000000.
# 1≤N≤4000.
# Sample Input
# 5
# 26 1 42 15 3 
# 2
# 3
# 4
# Sample Output
# 42
# 3