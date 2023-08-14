class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        n=len(isConnected)
        vis=[0]*n
        for i in range(n):
            if vis[i]==0:
                order=[i]
                while(order):
                    x=order.pop(0)
                    if vis[x]==0:
                        vis[x]=1
                        for j in range(n):
                            if isConnected[x][j]==1 and vis[j]==0:
                                order.append(j)
                count+=1

        return count
            
        
        