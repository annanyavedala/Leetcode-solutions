class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        revv=nums[::-1]
      
        for i in range(1, len(nums)):
            nums[i]=nums[i]+nums[i-1]
      
        for i in range(1, len(revv)):
            revv[i]=revv[i]+revv[i-1]
        revv=revv[::-1]
        
        
        for i in range(len(nums)):
            if nums[i]==revv[i]:
                return i
        return -1
        
            
        
        