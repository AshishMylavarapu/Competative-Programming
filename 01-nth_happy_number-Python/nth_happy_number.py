# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)



def ishappynumber(n):
	# your code goes here

	x = DigiSum(n)
	while(x>9):
		x=DigiSum(x)
	sol=0
	while(x>0):
		R = x%10
		x =x//10
		sol += R
	return (sol == 1 )

def DigiSum(n):
	sum=0
	while(n>0):
		r = n%10
		n = n//10
		sum +=(r*r)
	return sum

def nth_happy_number(n):
	count = 0
	i = 0
	while(True):
		i+=1
		if(ishappynumber(i)):
			count+=1
		if(count == n):
			return i


			