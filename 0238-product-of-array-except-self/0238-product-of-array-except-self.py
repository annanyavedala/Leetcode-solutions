class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        result2=1
        result1=1
        l=[i for i in nums if i==0]
        if(len(l)>1 or len(l)==0):
            for i in range(0,len(nums)):
                result = result * nums[i]
            for i in range(0,len(nums)):
                if(nums[i]==0):
                    nums[i]=0
                else:
                    nums[i]=result//nums[i]
        else:
            for i in range(0,len(nums)):
                if(nums[i]!=0):
                    result2=result2 * nums[i]
                    result1 = result1 * nums[i]
                else:
                    result1 = result1 * nums[i]
            for i in range(0,len(nums)):
                if(nums[i]==0):
                    nums[i]=result2
                else:
                    nums[i]=result1//nums[i]
                
        return nums
            