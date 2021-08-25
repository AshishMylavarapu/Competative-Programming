# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def even(a,b=0):
    if a==0:
        return b
    else:
        if(a%10)%2==0:
            return even(a//10,b=b*10+a%10)
        else:
            return even(a//10,b)

def reverse(a,b=0):
    if a==0:
        return b
    else:
        return reverse(a//10,b=b*10+a%10)

def listing(l,i):
    if len(l)==i:
        return l
    else:
        a=l[i]
        l[i]=reverse(even(a))
        return listing(l,i+1)
def fun_recursion_onlyevendigits(l): 
    # your code goes here
    if len(l)==0:
        return l
    return listing(l,0)