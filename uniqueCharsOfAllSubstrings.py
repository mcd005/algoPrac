# We have a string s
# In string s[:0] we have 0 unique chars
# In string s[:1] we have 1 unique char
# In string s[:2] we have the number of unqiue chars in s[:1] + 1 if s[1] is 
# But that only gets us substrings starting at s[0]
# So I guess we need to do 2D right, how many unique chars in a string s[i:j]
# Still O(n^2)
# If we had a matrix how would it save us time

# Here is the problem
# A naive implemntation of countUniqueChars(t) is O(m) where m is the length of t
# You also need to make O(n^2) queries to enumerate all the possible substrings

# Is there a way to make the helper function O(1)?
# Is there a way to make only O(n) queries?

# You can co

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        word = "Hello"
        print(word[:0])

sln = Solution()
sln.uniqueLetterString("word")