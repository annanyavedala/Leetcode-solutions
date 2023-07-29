class RecentCounter:

    def __init__(self):
        self.listt=[]
        

    def ping(self, t: int) -> int:
        if len(self.listt)==0:
            self.listt.append(t)
            return len(self.listt)
        else:
            while(len(self.listt)!=0 and self.listt[0]<t-3000):
                self.listt=self.listt[1:]
            self.listt.append(t)
                
            return len(self.listt)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)