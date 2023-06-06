class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l=list(s)
        p=0
        q=len(l)-1
        while(p<=q):
            if l[p] in vowels and l[q] in vowels:
                temp=l[p]
                l[p]=l[q]
                l[q]=temp
                p+=1
                q-=1
            elif l[p] not in vowels:
                p+=1
            elif l[q] not in vowels:
                q-=1
        return ''.join(l)
            
        