
def countTriplets(arr, n, sum):

    ans = 0

    for i in range(0, n-2):
        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] < sum):
                    ans+=1

    return print(ans)




N, X = input().split()

arr = []

for i in range(int(N)):
    arr.append(int(input()))

countTriplets(arr, int(N), int(X))    




