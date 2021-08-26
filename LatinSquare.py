# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    if(len(lst)==0):
        return None
    else:
        row=len(lst)
        col=len(lst[0])
        c=0
        for i in lst:
            a=set(i)
            if(len(a)==col):
                c+=1
            else:
                return False
        return True