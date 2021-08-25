def prime(k):
    if(k<2):
        return False
    elif(k==2):
        return True
    elif(k%2==0):
        return False
    else:
        for i in range(3,int((k**0.5)),2):
            if(k%i==0):
                return False
            
        return True
        

def palin(n):   
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True
    else:
        return False
        
def ispalindromic(s):
    if(prime(s)==True):
        if(palin(s)==True):
            return ("The number is palindromic prime")
    return ("The number is not palindromic prime")