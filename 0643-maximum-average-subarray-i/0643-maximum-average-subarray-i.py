class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        summ=nums[0]
        for i in range(1,k):
            summ=summ+nums[i]
        avg=summ/k 
        maxx=avg
        p=0
        q=k
        while(q<n):
            summ-=nums[p]
            summ+=nums[q]
            avg=summ/k
            maxx=max(maxx,avg)
            p+=1
            q+=1
        return maxx
            
            
            
        
        
        
        