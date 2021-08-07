
class Solution:
    
    def nextPermutation(self, num):
        k = -1;
        #Step 1: find max k A[k]<A[k+1]
        for i in range(0,len(num)-1):
            if num[i]<num[i+1]:
                k = i;
        if k == -1:
            num.reverse();
            return num;
        else:
            #Step 2: find l A[l]>A[k]
            for i in range(k+1, len(num)):
                if num[i]>num[k]:
                    l = i;
            #Step 3: swap A[l] A[k]
            num[l], num[k] = num[k], num[l];
            #Step 4: reverse k+1 to end
            num[k+1:len(num):1] = num[len(num)-1:k:-1];
            return num;

nums = [1,2,3]            

a = Solution()

print(a.nextPermutation(nums))