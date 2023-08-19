import collections
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs=((0,1), (-1,0), (1,0), (0,-1))
        rows=len(maze)
        cols=len(maze[0])
        i,j=entrance
        maze[i][j]='+'
        q=collections.deque()
        q.append([i,j, 0])
        
        while q:
            curr_row, curr_col, dist=q.popleft()
            for d in dirs:
                next_row=curr_row+d[0]
                next_col=curr_col+d[1]
                
                if 0<=next_row<rows and 0<=next_col<cols and maze[next_row][next_col]=='.':
                    if 0==next_row or next_col==0 or next_row==rows-1 or next_col == cols -1:
                        return dist+1
                    
                    maze[next_row][next_col]='+'
                    q.append([next_row, next_col, dist + 1])
        return -1
                    
                    
                
            
  
        
                
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        