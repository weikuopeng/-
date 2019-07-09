class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N=len(S)
        fin=[]
        nh, nt = 0,N
        
        for i in range(0,N):
            if S[i]=="I":
                fin.append(nh)
                nh+=1
            else:
                fin.append(nt)
                nt-=1
        fin.append(nh)
        return fin
    
s=Solution()
S="IDID"
print(s.diStringMatch(S))
