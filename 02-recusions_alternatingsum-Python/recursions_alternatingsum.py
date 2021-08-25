# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def sum(l,i,a):
    if(len(l)==i):
        return a
    elif(i%2==0):
        a=a+l[i]
        return sum(l,i+1,a)
    else:
        a=a-l[i]
        return sum(l,i+1,a)
def fun_recursions_alternatingsum(l):
    # your code goes here
    
    return sum(l,0,0)
