class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count0=0
        count1=0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] ==0:
                count0+=1
            if nums[i] ==1:
                count1+=1
            if nums[i] ==2:
                count2+=1
        i = 0
        while i <len(nums):
            
            while count0>0:
                nums[i] = 0
                count0-=1
                i+=1
                continue
            while count1 >0:
                nums[i] =1
                count1-=1
                i+=1
                continue
            while count2 >0:
                nums[i] = 2
                count2-=1
                i+=1
                continue

    

        