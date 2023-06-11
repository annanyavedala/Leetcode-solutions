class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        nums.sort()
        p=0
        n=len(nums)
        q=n-1
        while(p<q):
            summ=nums[p]+nums[q]
            if(summ<k):
                p+=1
            elif(summ>k):
                q-=1
            elif(summ==k):
                count+=1
                p+=1
                q-=1
                
        return count
                
            
        
        
        
        