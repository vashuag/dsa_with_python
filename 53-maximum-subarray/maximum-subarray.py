class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxi = -sys.maxsize-1
        sum =0
        for i in range(len(nums)):
            sum +=nums[i]
            if sum>maxi:
                maxi = sum
            if sum <0:
                sum=0
        
                
           
        return maxi
            
            

        # maxi = -sys.maxsize-1
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         maxi = max(sum,maxi)
        # return maxi
        