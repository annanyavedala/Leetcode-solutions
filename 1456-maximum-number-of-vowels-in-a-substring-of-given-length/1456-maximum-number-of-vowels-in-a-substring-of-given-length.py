class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        v=['a','e','i','o','u']
        p=0
        q=k
        count=-10000000
        c=0
        for i in range(p,q):
            if(s[i] in v):
                c+=1
        count=max(count,c)
        p+=1
        while(q<n):
            if s[p-1] in v:
                c-=1
            if(s[q] in v):
                c+=1
            p+=1
            q+=1
            count=max(count, c)
            
        
        return count
                
            
            
            
            
        