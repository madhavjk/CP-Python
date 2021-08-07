

def lcs(X, Y, m, n):

    if m == 0 or n == 0:
        return 0

    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X,Y,m-1,n-1)
    else:
        return max(lcs(X,Y,m,n-1),lcs(X,Y, m-1,n))




A, B = input().split()
X = ""
Y = ""

for i in range(int(A)):
    X = X + input()

for i in range(int(B)):
    Y = Y + input()    




print( lcs(X , Y, len(X), len(Y)))            