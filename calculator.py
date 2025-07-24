A = float(input(" enter a number : "))  
B = input(" enter a sign ( + , - , * , / ) : ")  
C = float(input(" enter a number : "))  
if(B=="+"):
    print(float(A) + float(C)) 
elif(B=="-"):
    print(float(A) - float(C)) 
elif(B=="*"):
    print(float(A)*float(C)) 
elif(B=="/"):
    if(float(C)!=0):
        print(float(A)/float(C))
    else:
        print(" divide by 0 is not possible here ") 
else:
    print(" you enter wrong operator or sign ") 

