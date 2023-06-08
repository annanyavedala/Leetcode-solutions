class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(len(nums)<3):
            return False

        n=len(nums)
        maxR=[0]*n
        maxR[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            if(nums[i]>maxR[i+1]):
                maxR[i]=nums[i]
            else:
                maxR[i]=maxR[i+1]
        minn=nums[0]
        for j in range(1, len(nums)-1):
            if(nums[j]>minn and nums[j]<maxR[j+1]):
                return True
            minn=min(minn, nums[j])

        return False
                
    