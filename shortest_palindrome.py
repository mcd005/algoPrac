# Version 1 - Brute force. Gets TLE
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        end_of_longest = 0
        for i in range(1, n):
            left, right = 0, i
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            if left >= right:
                end_of_longest = i

        return s[n-1:end_of_longest - 1:-1] + s

'''
Try a version with KMP

We need to know the answer to "what is the longest palindrome starting at index 0"
Because then our prefix just needs to be all the characters after that point reversed

Brute force method of finding it
Iterate through s
When we find a char that is that same as s[0] we collapse two pointers inwards, while they point to a char of the same value
If they intersect we have a palindrome
If not then we do not have a palindrome
However this could lead to an overall complexity of O(n^2)
How do we make this operation quicker, ideally constant time?

aacecaaa
   l
   r

end_of_longest = 6



If it's not 
If s is a palindrome then the we'd return s

There is almost certainly a way to save past computations about whether or not a substring is a palindrome
Adding letters means shifting the midpoint to the left by 1

Shortest possible is len(s)
Longest possible is 2 * len(s)

We start with a pointer at the end
We ask is a at the front


abcd
i
j
prefix = "dcb"

aacecaaa
prefix = "aaacecaa" aacecaaa

Naive
Check if s is a palindrome

Iterate through and look for starting spots for palindromes
Then we expand outward

We know the letter at the end of s is not going to change
So checking if it's a palindrome from inside out might mean we are wasting time
You can know straight away if you are going to need to add letters


Maybe the question we are instead trying to answer is: "Where has an existing palindrome been severed?"
Can't we just look at the middle then continually expand out
If we have maintained the palindrome condition until we reach the end of the string then all we need to do is 
add what's left from the longer end

in the case of abcd ---> 
bc not palindrome

b is palindrome
abc is not

ab is not palindrome

a is palindrome
and here we have reached the end so we have to prepend s[1:] but reversed

The problem is O(n) to expand, and we expand maybe n times and the we have to prepend which takes n and reverse which takes n
O(n^2 + n)

What we need to do is collapse inwards
If we have a string that looks like <letters>d<inner letters>c<letters but mirrored>
As soon as we see d and c are not mirrored, we only nede to continue our search on inner letters

aacecaaa
  i    
    j

Ah ok so starting with j at n - 1 didn't work
So we append n - 1 to our string
And we start again with i at 0 and j at n - 2
But because we have already check i from zero to wherever it is now we can just move i back 1

abcd
i
   j

pref = dc


abcdefruvfedcba
      i
        j
pref = a


abcd

hannahyeet

We have a valid palindrome centred around a that looks like dcbabcd
ab is not valid so would also need to same
bc is not valid so would also need the same

faaaaaaaaaab

Maybe we need DP to ask if a given segment is palindromic
Would take O(n^2) to populate though so no real saving



'''