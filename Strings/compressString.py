# https://leetcode.com/problems/string-compression/

# Version 1 - two pointers.
# Time complexity       O(n)
# Space complexity      O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        # read pointer runs ahead an checks the lenght of a char sequence
        # write pointers overwrites the original array with the char and the sequence lenght 
        rptr, wptr = 0, 0 
        
        while rptr < n:
            
            # Establish how long the sequence goes on for
            seqLen = 1
            while rptr + 1 < n and chars[rptr] == chars[rptr + 1]:
                rptr += 1
                seqLen += 1
                
            # Overwrite the existing array with character of the above sequence
            chars[wptr] = chars[rptr]
            
            # And per the stipulations, if the sequence is longer than a single character
            # add it's comma separated digits
            if seqLen > 1:
                strSeqLen = str(seqLen)
                for c in strSeqLen:
                    wptr += 1
                    chars[wptr] = c
            
            rptr += 1
            wptr += 1
                    
        return wptr
        # All the chars after wtpr are going to be the unoverwritten values of original array
        # but those are not checked so we don't care that they are still there