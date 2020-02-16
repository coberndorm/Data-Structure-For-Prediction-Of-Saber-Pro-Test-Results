
def lcs (X, Y, x, y):
    if (x == 0 or y == 0):
        return 0
    if (X [x-1] == Y[y-1]):
        return 1 + lcs (X,Y,x-1,y-1)
    return max (lcs (X, Y, x-1, y), lcs (X,Y,x,y-1))

## https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/

def fillingWays (n):
    if (n < 2):
        return 1;
    return fillingWays(n-1) + fillingWays(n-2)



print(lcs( "AGGTAB","CXTXAYB",len("AGGTAB"),len("CXTXAYB")))
print(fillingWays(32))