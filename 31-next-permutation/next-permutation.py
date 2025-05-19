class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        size = len(nums)-1

        while size>0 and nums [size-1]>=nums[size]:
            size-=1
        if  size ==0:
            nums.reverse()
            return
        nsize = len(nums)-1

        while nsize>=size and nums[nsize] <=nums[size-1]:
            nsize-=1
        nums[size-1],nums[nsize] = nums[nsize],nums[size-1]

        nums[size:] = reversed(nums[size:])














        # i = len(nums) - 1
        # while i > 0 and nums[i-1] >= nums[i]:
        #     i -= 1
        
        # if i == 0:
        #     nums.reverse()
        #     return
        
        # j = len(nums) - 1
        # while j >= i and nums[j] <= nums[i-1]:
        #     j -= 1
        
        # nums[i-1], nums[j] = nums[j], nums[i-1]

        # nums[i:] = reversed(nums[i:])