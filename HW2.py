class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(a!=b for a,b in zip(sorted(heights),heights))

s=Solution()

heights=[1,1,4,2,1,3]
print(s.heightChecker(heights))
