def frequencyOfCharacters(str):
   b=f=j=p=v=0
   for let in str:
      if let.lower()=='b':b+=1
      elif let.lower()=='f':f+=1
      elif let.lower()=='j':j+=1
      elif let.lower()=='p':p+=1
      elif let.lower()=='v':v+=1
   print("b=",b,"f=",f,"j=",j,"p=",p,"v=",v,"total=",b+f+j+p+v)

frequencyOfCharacters(input())