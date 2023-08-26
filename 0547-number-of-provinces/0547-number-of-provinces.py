class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def bfs(g, u, vis):
            vis[u]=1
            for j in range(0, len(g[u])):
                if g[u][j]==1 and vis[j]==0:
                    bfs(g, j, vis)
            return
    
        c=0
        vis=[0]*len(isConnected)
        for i in range(len(vis)):
            if vis[i]==0:
                c+=1
                bfs(isConnected, i, vis)
        return c
        
        
        
        
        # return count
            
        
        