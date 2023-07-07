class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!='*':
                stack.append(s[i])
            else:
                if(len(stack)>0):
                    stack.pop(-1)
        return ''.join(stack)
        