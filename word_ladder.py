class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass

'''
We can try a dfs method
Create a dict from the word list that looks like {word: idx}
As we are building the dict we want to check the distance of each word from our begin word
If we see that there is only a distance of 1 from any given word and our begin word we mark that with an idx -1
This is to denote that we would no longer need to dfs in our dict when we find a word with this index
If none of the words have a distance of 1 then there is no valid path

We begin the dfs by
Checking if end word is in word list
Then dfs the two neighbouring words
Check whichever returns the min path and return that

Because every adjacent word differs by only one letter
We could have whole runs of words that are at a distance of 1 from our target
e.g hot, dot, pot, lot, got
If our end word was got, there would be no need to go through dot, pot etc

Maybe it's a case of the path is only as long as there are transitions from one distance to another?
Are distances always montonic sequences originating from the begin word?

["hot","dot","dog","lot","log","cog"]
   1     2     3     2     3     3

["hot","dot","lot","dog","log","cog"]
   1     2     2     3     3     3
'''