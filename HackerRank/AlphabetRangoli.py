def print_rangoli(size):
    # your code goes here
    # Alphabet Rangoli in Python - Hacker Rank Solution START
    width  = size*4-3
    string = ''

    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
                print(string)
        for k in range(i-1,0,-1):    
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
                print(string)
        print(string.center(width,'-'))
        string = ''

    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
                print(string)
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
                print(string)
      #   print(string.center(width,'-'))
        
    # Alphabet Rangoli in Python - Hacker Rank Solution END

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)