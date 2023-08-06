class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        vis=[0]*n
        order=[0]
        while(order):
            x=order.pop(0)
            if vis[x]==0:
                vis[x]=1
                for j in rooms[x]:
                    order.append(j)    
                
        for i in range(0,len(vis)):
            if vis[i]==0:
                return False
        return True
            
                    
            
        
        