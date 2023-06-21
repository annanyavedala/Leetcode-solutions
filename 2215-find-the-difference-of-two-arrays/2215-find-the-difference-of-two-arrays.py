class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1={}
        d2={}
        l1=[]
        l2=[]
        ans=[]
        x=list(set(nums2))
        y=list(set(nums1))
        for i in range(len(y)):
            if y[i] not in d1:
                d1[y[i]]=1
            else:
                d1[y[i]]+=1
        
        for i in range(0, len(x)):
            if x[i] not in d1:
                l1.append(x[i])
        for i in range(0,len(x)):
            if x[i] not in d2:
                d2[x[i]]=1
            else:
                d2[y[i]]+=1
        for i in range(0, len(set(y))):
            if y[i] not in d2:
                l2.append(y[i])
        ans.append(l2)
        ans.append(l1)
        return ans
        
        