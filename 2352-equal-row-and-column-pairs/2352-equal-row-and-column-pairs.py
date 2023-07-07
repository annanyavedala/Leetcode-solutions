class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            l=[x[i] for x in grid]
            print(l)
            # print(grid[i])
            for j in range(0, len(grid)):
                if l==grid[j]:
                    c+=1
        return c
                
                
                
            
        
        
                
            
            
        
        
        
        
        