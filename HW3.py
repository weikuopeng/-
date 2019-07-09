class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(0,len(A)):
            A[i]=A[i]**2
        
        return sorted(A)
s=Solution()
A=[-4,-1,0,3,10]
print(s.sortedSquares(A))