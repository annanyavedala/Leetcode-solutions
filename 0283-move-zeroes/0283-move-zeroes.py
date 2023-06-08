class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p=0
        q=1
        while(q<len(nums)):
            if(nums[p]==0 and nums[q]!=0):
                nums[p]=nums[q]
                nums[q]=0
                p+=1
            if(nums[p]!=0):
                p+=1
            q+=1
                
        """
        Do not return anything, modify nums in-place instead.
        """
        