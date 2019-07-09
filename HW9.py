class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(S.count(j) for j in J)
    
s=Solution()
J="aA"
S="aAAbbbbb"
print(s.numJewelsInStones(J,S))