class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        
        for i in range(0,len(A)):
            if A[i]%2==0:
                even.append(A[i])
            else:
                odd.append(A[i])
        sorted(even)
        sorted(odd)
        
        ans=[]
        for i in range(0,int(len(A)/2)):
            ans.append(even[i])
            ans.append(odd[i])
        
        return ans

s=Solution()
A=[4,2,5,7]
print(s.sortArrayByParityII(A))