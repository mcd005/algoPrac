/*
https://leetcode.com/problems/stream-of-characters

Version 1
We build a trie but with each of the words reversed (i.e. the children of the root of the trie are all the last chars of each word)
For each query, we append the char to a string which we'll call our given word
Then we iterate backwards over our given word and for each of it's char we ask
    Is this char in the children of the current node?
        If it is then we make that corresponing child the current node and we continue to iterate backwards through the given word
        If it isn't we return false
    If at any point we reach a endOfWord node, we return true

## Time Complexity ##
To Constuct Trie        O(wl)   for w word of an averge length of l letters
For Each Query          O(n)    where n is the length of the given word

## Space Complexity ##
To Construct Trie       O(wlk) for w words of an average length of l letters made up of an alphabet of size k
For all the queries     O(n)
*/

/*
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker* obj = new StreamChecker(words);
 * bool param_1 = obj->query(letter);
*/

class TrieNode
{
public:
    TrieNode* children[26] = {};
    bool isEndOfWord = false;

    bool isLetterChild(char letter)
    {
        return children[letter - 97] != nullptr;
    }

    void addChild(char letter)
    {
        children[letter - 97] = new TrieNode();
    }

    TrieNode* getChild(char letter)
    {
        return children[letter - 97];
    }
};

class SuffixTrie
{
public:
    SuffixTrie(vector<string>& words) : root(new TrieNode())
    {
        for (auto &word : words)
        {
            addWordToTrieBackwards(word);
        }
    }

    void addWordToTrieBackwards(string& word)
    {
        TrieNode* node = root;
        for (auto it = word.end() - 1; it >= word.begin(); --it)
        {
            if (!node->isLetterChild(*it))
            {
                node->addChild(*it);
            }
            node = node->getChild(*it);
        }
        node->isEndOfWord = true;
    }

    void printTrie(TrieNode* node)
    {
        for (int i = 0; i < 26; ++i)
        {
            if (node->children[i] != nullptr)
            {
                printTrie(node->children[i]);
                std::cout << (char) (i + 97) << std::endl;
            }
        }
    }

    TrieNode* root;
};

class StreamChecker {
public:
    SuffixTrie* sufTrie;
    vector<char> givenWord;

    StreamChecker(vector<string>& words) 
    {
        sufTrie = new SuffixTrie(words);
    }
    
    bool query(char letter) 
    {
        givenWord.push_back(letter);

        TrieNode* node = sufTrie->root;
        auto it = givenWord.end() - 1;
        while (it >= givenWord.begin())
        {
            if (node->isEndOfWord) return true;
            if (!node->isLetterChild(*it)) return false;
            node = node->getChild(*it);
            --it;
        }
        return node->isEndOfWord;
    }
};




// We are building up a given word
// When the suffix of the given word is in the wordlist we return true

// Naive
//     Each time a char is added to the given word we 
//         for each word in the wordlist we iterate backwards through our given word and compare
    
// Better
//     Each time a char is added to the given word we
//         Use a trie to compare the suffix of our new given word to all the words in the wordlist
//             You'd DFS the Trie, searching each node while it's children were the next char

// Is there a way to reuse computation between queries?


// Construct a trie from each words in words
// Then iterate over the queries

// Iterate over the characters in queries
//     While there are stil characters to iterate over
//         If we are at leaf and th
//         I assume we return false if we reach a leaf in the trie and we still have chars to go
//     While the char is in the children on the current node of the trie keep going
//     If we get to the end of the word in the query and we're still on the trie we can return true