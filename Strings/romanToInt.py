# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        syms = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
        
        edgeCases = {"IV" : 4,
                     "IX" : 9,
                     "XL" : 40,
                     "XC" : 90,
                     "CD" : 400,
                     "CM" : 900,
                    }
        
        n = len(s)
        prevWasEdge = 0
        output = 0
        for i in range(n - 1):
            if prevWasEdge == 0:
                if (s[i] + s[i + 1]) in edgeCases:
                    output += edgeCases[s[i] + s[i + 1]]
                    prevWasEdge = 1
                else:
                    output += syms[s[i]]
            else:
                prevWasEdge = 0
                
        output += syms[s[-1]] * (not prevWasEdge)
                
        return output 
        
# Slower (in terms of ms not necessarlity Time complexity) alternative but smarter pattern spotting. 
# Recognises that any time a smaller value precedes a larger one then it must be subtracting
class Solution:
    def romanToInt(self, s):
        class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i in s[::-1]:          # rev the s
            if dict[i] >= prev:
                res += dict[i]     # sum the value iff previous value same or more
            else:
                res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
            prev = dict[i]
        return res
                    
                
                    
        
                    
                
                    
        