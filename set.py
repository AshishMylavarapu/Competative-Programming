# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):

    lis = []
    res1 = [{}]
    for i in range(1,n+1):
        lis.append(i)
        res1.append({i})
    for j in range(1, 1 << n):
        re = []
        re.append({lis[m] for m in range(n) if(j & (1 << m))})
        for z in re:
            if z not in res1:
                res1.append(z)
    return res1[:k]