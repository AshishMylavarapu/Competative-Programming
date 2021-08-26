# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

	
def check(n,l,i=0,total=0):
		total=(3**i)
		if(total<=n):
				l.append(total)
		i+=1
		if(total>=n):
    			return l
		return check(n,l,i,total)

def recursion_powersof3ton(n):
	# Your code goes here
	
	l=[]
	if(n<1):
    		return None
	else:
    		return check(n,l)
