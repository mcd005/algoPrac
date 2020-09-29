struct TrieNode {
    map<char,TrieNode*> children;
    bool isComplete;
};