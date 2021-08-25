# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
def check(n):
	a=n**5
	g=str(a)
	res=[]
	for i in g:
		if(g.count(i)>=1):
			res.append(i)
	res=set(res)
    # print(len(res))
	if(len(res)==10):
		return True
	else:
		return False


def nthwithproperty309(n):
	# Your code goes here
	found=0
	guess=308
	while(found<=n):
		guess+=1
		if(check(guess)):
			found+=1

	return guess
