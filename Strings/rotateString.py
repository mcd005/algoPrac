# https://leetcode.com/problems/rotate-string
#
# Initially I tried to implement Version 1 which works by
#     Walking through A and putting the indices for each char in a list inside a dict (where char is key)
#     We then take the first char of B and check in the dictionary all the possible indices it could have been shifted from
#     We put all these possible shifts in a set and then repeat the process for the second char of B
#     The union of these two sets gives should yield the correct shift for the whole string
#     (i.e. possibleShifts(B[0]) U possibleShifts(B[1]) = shift)
#     We then iterate through B ad if all elements are the same as their index + shift in A then the string has been rotated
# However this version did not seem to work; likely my modulo maths was wrong for shifts based on odd or even length arrays
#
# So I did Version 2: An O(n^2) solution that checks if the strings are equal for all n possible shifts
# Obviously not ideal
#
# Version 3 is the solution I found after I gave up banging my head against a wall
# By adding the strings you can then call Pythons "subtr in string", which I belive is O(N) on average (Boyers-Moore)
# and O(NM) worst case
#
# Alternatively you could have simulated adding the strings together with some modulo maths and then used KMP
# However I'm not tatally familiar
#
# In any case it appears best case time complexity is O(N + M)    N to copy, M for "in" or "find"
# And best case space complexity is O(N)

# Version 3
class Solution:
    def rotateString(self, A, B):        
        return len(A) == len(B) and B in A + A

# Version 2
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        n = len(A)
        m = len(B)
        if n != m:
            return False
        if (n <= 1 and n == m):
            return True

        for offset in range(n):
            for i in range(m):
                if A[(i + offset) % n] != B[i]:
                    break
                if (i == m - 1) and (A[(i + offset) % n] == B[i]):
                    return True

        return False

# Version 1
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        n = len(A)
        if (n != len(B)) or (n == 1 and A != B):
            return False

        dict = {}
        for i, char in enumerate(A):
            if char not in dict:
                dict[char] = [i]
            else:
                dict[char].append(i)

        possibleShifts = set()
        for idx in dict[B[0]]:
            possibleShifts.add((0 - idx) % n - n % 2)

        shift = None
        for idx in dict[B[1]]:
            if ((1 - idx) % n - n % 2) in possibleShifts:
                shift = ((1 - idx) % n - n % 2)

        if shift == None:
            return False

        for j in range(n):
            if B[j] != A[(j + shift) % n]:
                return False

        return True  




