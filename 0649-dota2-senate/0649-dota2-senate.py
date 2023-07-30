class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        
        r_deque=deque()
        d_deque=deque()
        
        for i, s in enumerate(senate):
            if s=='R':
                r_deque.append(i)
            else:
                d_deque.append(i)
        while (len(r_deque)!=0 and len(d_deque)!=0):
            r_turn=r_deque.popleft()
            d_turn=d_deque.popleft()
            if(r_turn<d_turn):
                r_deque.append(r_turn+n)
            else:
                d_deque.append(d_turn+n)
        if(len(r_deque)>0):
            return 'Radiant'
        else:
            return 'Dire'
        
        
        
            
        