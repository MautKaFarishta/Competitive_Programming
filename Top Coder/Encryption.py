from math import floor,ceil,sqrt
try:

    def Encrypt(Encrypted):
        for word in range(M):
            for index in range(length):
                if index%M==word:
                    Encrypted=Encrypted+Msg[index] # Adds only those characters which were present in columns
            Encrypted=Encrypted+" "
        return Encrypted

    Msg=input().strip()
    Msg=Msg.replace(' ','') #Removing Blank Spaces
    L=floor(sqrt(len(Msg))) 
    M=ceil(sqrt(len(Msg)))
    length=len(Msg)
    Encrypted=''
    Encrypted=Encrypt(Encrypted) #Getting encrypted message
    print(Encrypted)
       
except:
    pass