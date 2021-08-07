
# Function to left-rotate a list by one position
def leftRotateByOne(A):
 
    first = A[0]
    for i in range(len(A) - 1):
        A[i] = A[i + 1]
 
    A[-1] = first
 
 
# Function to left-rotate a list by `r` positions
def rotLeft(A, d):
 
    for i in range(d):
        leftRotateByOne(A)
 
 
if __name__ == '__main__':
 
    A = [1, 2, 3, 4, 5]
    d = 2
 
    rotLeft(A, d)
    print(A)   


