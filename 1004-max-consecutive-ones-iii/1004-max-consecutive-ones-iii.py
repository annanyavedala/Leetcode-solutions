class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p=0
        q=0
        count=k
        maxx=0
        while(p<len(nums) and q<len(nums)):
            if(count!=0 or nums[q]==1):
                if nums[q]==0:
                    count-=1
                q+=1
            elif(count==0):
                if(nums[p]==0):
                    count+=1
                p+=1
            maxx=max(maxx, q-p)
        return maxx
            
        
            
        
        
        
        
        