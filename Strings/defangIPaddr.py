'''
https://leetcode.com/problems/defanging-an-ip-address/

Very basic string manipulation

Time complexity 	O(n)
Space compexity 	O(1)
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return(address.replace(".", "[.]"))