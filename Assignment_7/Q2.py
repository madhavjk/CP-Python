def rotate(arr, n):
    x = arr[n - 1]
     
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];
         
    arr[0] = x;
 
 

arr= [1, 2, 3, 4, 5]
n = len(arr)
print ("Given array is")
for i in range(0, n):
    print (arr[i], end = ' ')
 
rotate(arr, n)
 
print ("\nRotated array is")
for i in range(0, n):
    print (arr[i], end = ' ')
 
