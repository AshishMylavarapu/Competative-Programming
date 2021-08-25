# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isPrime(n):
    if(n==0):
        return False
    if(n==2):
        return True
    else:
        for i in range(2,n//2+1):

            if(n%i==0):
                return False
    return True

def isSmith(n):
    if(isPrime(n)!=True):
        k=n
        m=0
        sum=0
        li=[]
        if n==1:
            return False
        for i in range(2,(n//2) + 1):
            if((isPrime(i)==True) and (n%i==0)):
                li.append(i)
         
        for i in str(n):
            sum+=int(i)
        temp=[]
        for i in li:
            while (k%i==0 and k!=0):
                temp.append(i)    
                m+=i
                k=k//i
        sum1=0        
        for j in temp:
            if(j>9):
                for i in str(j):
                    sum1+=int(i)
            else:
               sum1+=j
        if(sum==sum1):
            return True
        else:
            return False

def fun_nth_smithnumber(n):
    count=0
    temp=1
    a =0
    while(n+1!=count):
        if(isSmith(temp)==True):
            count+=1
            b=temp
        temp+=1
    return b
