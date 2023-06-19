class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        longestWindow = 0
        start = 0

        for i in range(len(nums)):

                # if zero found increase the zeroCount
            if nums[i] == 0:
                zeroCount += 1 

                # Increase start pointer till the zerocount is not reduced to 1 
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1  
                start += 1

                # max of all windows
            longestWindow = max(longestWindow, i - start)

        return longestWindow
                    
        