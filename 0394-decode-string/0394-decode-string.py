class Solution:
    def decodeString(self, s: str) -> str:
        digits=['0','1','2','3','4','5','6','7','8','9']
        st=[]
        x=''
        out=[]
        for i in s:
            st.append(i)
            if(st[-1]==']'):
                st.pop(-1)
                while(st[-1]!='['):
                    x+=st[-1]
                    st.pop(-1)
                st.pop(-1)
                num=''
                while(st and st[-1] in digits):
                    num+=st[-1]
                    st.pop(-1)
                num=num[::-1]
                x=int(num)*x
                # print(x)
                # st.pop(-1)
                for o in x[::-1]:
                    st.append(o)
                x=''
        return ''.join(st)
                
        
                
        