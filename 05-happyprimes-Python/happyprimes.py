# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

    
def isPrime(x):
    if(x<2):
        return False
    if(x==2):
        return True
    if(x%2==0):
        return False
    n=round(x**0.5)
    for i in range(3,n+1,2):
        if(x%i==0):
            return False

    return True


def powersquare(n):
    sum=0
    while(n>0):
        sum=sum+(n%10)**2
        n=n//10
    return sum
def Happy(n):
    while(True):
        if n==1:
            return True
        elif n==4:
            return False
        else:
            n=powersquare(n)
    return False
def ishappyprimenumber(n):
    if(isPrime(n) and  Happy(n)==True):
        return True
    return False