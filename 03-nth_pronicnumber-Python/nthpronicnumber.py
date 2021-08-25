# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
def pronic(x):
    i=0
    while(i<=x):
        if(x==(i*(i+1))):
            return True 
        i=i+1
    return False
def nthpronicnumber(n):
	if(n==0):
		return 0
	count=0
	k=1
	while(True):
		if(pronic(k)==True):
			count=count+1
		if(count==n):
			return k
		k=k+1