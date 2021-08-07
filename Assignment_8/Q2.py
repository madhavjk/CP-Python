

def posneg(a,n):

    b = []
    j = k= 0

    for i in range(n):

        if a[i]>=0:
            b[j] = a[i]
            j = j+1

        else:
            b[n-1-k] = a[i]
            k = k+1

    return print(b)        


a = [-12,11,-13,-5,6,-7,5,-3,-6]

posneg(a,9)
