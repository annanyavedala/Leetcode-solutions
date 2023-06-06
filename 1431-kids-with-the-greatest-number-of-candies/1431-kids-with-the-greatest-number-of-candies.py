class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx=max(candies)
        l=[]
        for i in candies:
            if i+extraCandies>=maxx:
                l.append(True)
            else:
                l.append(False)
        return l
        
        