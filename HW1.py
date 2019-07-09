class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")

s=Solution()
address="1.1.1.1"
print(s.defangIPaddr(address))