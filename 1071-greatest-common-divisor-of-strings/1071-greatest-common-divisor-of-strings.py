class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str1)>=len(str2)):
            base=str2
        else:
            base=str1
        while len(base)>0:
            if len(str1)%len(base)==0 and len(str2)%len(base)==0:
                c1=len(str1)//len(base)
                c2=len(str2)//len(base)
                if(c1*base==str1 and c2*base==str2):
                    return base
                else:
                    base=base[:-1]
                    
            else:
                base=base[:-1]
        return ''
                
            
            
            
            
        