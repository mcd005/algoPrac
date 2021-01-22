# https://leetcode.com/problems/fraction-to-recurring-decimal/
# See .cpp for explantion

#Version 2 - same approach as below but slightly more Pythonic
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        n, remainder = divmod(abs(numerator), abs(denominator))
        res = [sign+str(n), '.']
        
        remainders = {}
        
        while remainder and remainder not in remainders:
            remainders[remainder] = len(res) 
            n, remainder = divmod(remainder * 10, abs(denominator))
            res.append(str(n))
        
        if remainder in remainders: 
            idx = remainders[remainder]
            res.insert(idx, "(")
            res.append(")")
            
        return "".join(res).rstrip(".") 

# Version 1 - a translation of the fastests cpp algorithm
# Not especially fast here though
# possibly because of .py string immutability
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator % denominator == 0): return str(numerator // denominator)
        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        preDecimal = "0."
        if numerator > denominator:
            preDecimal = str(numerator // denominator) + "."
            numerator = numerator % denominator
        
        postDecimal = ""
        i = 0
        seenNumerators = { numerator : i }
        
        while numerator > 0:
            postDecimal += str(numerator * 10 // denominator)
            
            nextNumerator = numerator * 10 % denominator
            
            if nextNumerator in seenNumerators:
                whereSeen = seenNumerators[nextNumerator]
                postDecimal = postDecimal[:whereSeen] + "(" + postDecimal[whereSeen:] + ")"
                break
            
            seenNumerators[numerator] = i
            i += 1
            numerator = nextNumerator

        return sign + preDecimal + postDecimal
