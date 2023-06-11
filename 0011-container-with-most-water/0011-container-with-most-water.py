class Solution:
    def maxArea(self, height: List[int]) -> int:
        p=0
        n=len(height)
        q=n-1
        maxx=-10000000
        while(p<q):
            if(height[p]<height[q]):
                maxx=max(maxx, (q-p)*height[p])
                p+=1
            elif(height[q]<height[p]):
                maxx=max(maxx, (q-p)*height[q])
                q-=1
            else:
                maxx=max(maxx, (q-p)*height[q])
                q-=1
                p+=1
        return maxx
                
            
                
        
        
        