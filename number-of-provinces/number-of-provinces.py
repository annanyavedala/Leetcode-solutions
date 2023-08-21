class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root=[i for i in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    rootx=root[i]
                    rooty=root[j]
                    if rootx!=rooty:
                        for l in range(len(root)):
                            if root[l]==rooty:
                                root[l]=rootx
        
                        
        # print(isConnected)
        return len(set(root))
        
        # return count
            
        
        