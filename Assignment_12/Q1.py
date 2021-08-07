
def moreThanNdK(arr, n, k):
     
    
    if (k < 2):
        return
 
  
    temp = [[0 for i in range(2)]
            for i in range(k)]
 
    for i in range(k - 1):
        temp[i][0] = 0
 
    
    for i in range(n):
        j = 0
 
        
        while j < k - 1:
            if (temp[j][1] == arr[i]):
                temp[j][0] += 1
                break
 
            j += 1
 
       
        if (j == k - 1):
            l = 0
 
           
            while l < k - 1:
                if (temp[l][0] == 0):
                    temp[l][1] = arr[i]
                    temp[l][0] = 1
                    break
 
                l += 1
 
            # If all the position in the
            # tempare filled, then decrease
            # count of every element by 1
            if (l == k - 1):
                while l < k:
                    temp[l][0] -= 1
                    l += 1
 
    # Step 3: Check actual counts
    # of potential candidates in temp[]
    for i in range(k - 1):
 
        # Calculate actual count of elements
        ac = 0  # Actual count
        for j in range(n):
            if (arr[j] == temp[i][1]):
                ac += 1
 
        # If actual count is more
        # than n/k, then prit
        if (ac > n // k):
            print("Number:",
                  temp[i][1],
                  " Count:", ac)
 
 
# Driver code
if __name__ == '__main__':
 
    print("First Test")
    arr1 = [4, 5, 6, 7, 8, 4, 4]
    size = len(arr1)
    k = 3
    moreThanNdK(arr1, size, k)
 
    print("Second Test")
    arr2 = [4, 2, 2, 7]
    size = len(arr2)
    k = 3
    moreThanNdK(arr2, size, k)
 
    print("Third Test")
    arr3 = [2, 7, 2]
    size = len(arr3)
    k = 2
    moreThanNdK(arr3, size, k)
 
    print("Fourth Test")
    arr4 = [2, 3, 3, 2]
    size = len(arr4)
    k = 3
    moreThanNdK(arr4, size, k)