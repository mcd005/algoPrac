// Version 2 - Trie
struct TrieNode
{
    TrieNode* children[26] = { NULL };
    bool isEnd = false;
};

class Solution
{
public:
    int numMatchingSubseq(string s, vector<string> &words)
    {
        TrieNode* root = new TrieNode();
        for (auto word: words)
        {
            addToTrie(root, word);
        }

        int result = 0;

        queue<TrieNode*> curTrieNodes;
    	for (auto letter: s)
        {
            queue<TrieNode*> nextTrieNodes;

            curTrieNodes.push(root);
            while (!curTrieNodes.empty())
            {
                TrieNode* node = curTrieNodes.front();
                curTrieNodes.pop();

                if (node->isEnd) ++result;
                if (node->children[letter - 97])
                {
                    nextTrieNodes.push(root->children[letter - 97]);
                }
            }
            curTrieNodes = nextTrieNodes;
        }

        return result;
    }

private:
    void addToTrie(TrieNode* node, string word)
    {
        for (auto c: word)
        {
            if (!node->children[c - 97])
            {
                node->children[c - 97] = new TrieNode();
            }
            node = node->children[c - 97];
        }
        node->isEnd = true;
    }

    void printTrie(TrieNode* node, string curWord)
    {
        if (node->isEnd) cout << curWord << endl;

        for (int i = 0; i < 26; ++i)
        {
            if (node->children[i]) printTrie(node->children[i], curWord + (char)(i + 97));
        }
    }
};

// Convert words into a trie
// Then you iterate over the words in s
//     First you check if the current char is a child of route (if it is then add it to the q of next)
//     Then you iterate through the queue of pointers on the trie
//     If the pointer is on a trie that is a full word, increment the count
//     If the current char is the child of any of those pointers, put the relevant node in the q of next
//     If not do nothing

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Version 3 - Clean Trie class
class Trie
{
private:
    struct TrieNode
    {
        TrieNode *children[26] = {NULL};
        bool isEnd = false;
    };

    void addToTrie(TrieNode *node, string word)
    {
        for (auto c : word)
        {
            if (!node->children[c - 97])
            {
                node->children[c - 97] = new TrieNode();
            }
            node = node->children[c - 97];
        }
        node->isEnd = true;
    }

    void printTrie(TrieNode *node, string curWord)
    {
        if (node->isEnd) cout << curWord << endl;

        for (int i = 0; i < 26; ++i)
        {
            if (node->children[i]) printTrie(node->children[i], curWord + (char)(i + 97));
        }
    }
}

class Solution
{
public:
    int numMatchingSubseq(string s, vector<string> &words)
    {
        Trie::TrieNode *root = new Trie::TrieNode();

        for (auto word : words)
        {
            Trie::addToTrie(root, word);
        }

        Trie::printTrie(root, "");

        int result = 0;
        return result;
    }
};





class Solution
// Version 1 - Two pointer but too slow
{
public:
    int numMatchingSubseq(string s, vector<string> &words)
    {
        int result = 0;

        N = s.size();
        for (auto &word: words)
        {
            if (isASubsequence(s, word)) ++result;
        }

        return result;
    }

private:
    bool isASubsequence(string& s, string& word)
    {
       int m = word.size();
       int sp = 0, wp = 0;
       while (wp < m)
       {
           if (sp >= N) return false;
           if (s[sp] == word[wp]) ++wp;
           ++sp;
       }
       return true;
    }

    int N;
};

/*

s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]


One algorithm could be to itearate over the words and for each do a linear scan of s
but then time complexity would be O(n * mk) where m the number of words and k is average word size

There may be a solution with a trie where for each letter you check if it's a child of the root
    And then advance those pointers
    But that would introduce up  to n pointers for an O(n^2) runtime whihch is too slow


There has to be a faster way right?

Iterate over words
    Have one pointer on the character we're looking for
    Have the other pointer iterate over s 
        If characters do match increment both pointers
        If characters don't match increment until you do find one
        If you get to the end of s before the end of word then return false
    
*/