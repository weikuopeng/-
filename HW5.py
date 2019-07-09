from collections import Counter
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N=len(A)/2
        count=Counter(A)
        for x,y in count.items():
            if y==N:
                return x

s=Solution()
A=[2,1,2,5,3,2]
print(s.repeatedNTimes(A))
