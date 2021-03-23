// https://leetcode.com/problems/verifying-an-alien-dictionary
// Version 2 
// Array as map for encoding but convert each char to and int
// Then can just check if ints are in order
// Time complexity      O(k + n*m)
// Space complexity     O(k)
class Solution {
public:
     bool isAlienSorted(vector<string> words, string order) {
            int mapping[26];
            for (int i = 0; i < 26; i++)
                mapping[order[i] - 'a'] = i;
            for (string &w : words)
                for (char &c : w)
                    c = mapping[c - 'a'];
            return is_sorted(words.begin(), words.end());
        }
};

// Version 1 - Same as V1 in .py
// Time complexity      O(n*m)
// Space complexity     O(k)
class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        std::unordered_map<char, int> encoding;
        for (int i = 26; i >= 1; --i)
        {
            encoding[order[26 - i]] = i;
        }
        
        string prev = words[0];
        int n = words.size();
        for (int i = 1; i < n; ++i)
        {
            string cur = words[i];
            int prevSize = prev.size();
            int curSize = cur.size();
            int j = 0;
            while (j < prevSize && j < curSize)
            {
                if (encoding[cur[j]] > encoding[prev[j]]) break;
                else if (encoding[cur[j]] == encoding[prev[j]]) ++j;
                else return false;
            }
            if (j == curSize && curSize < prevSize) return false; 
            prev = cur;
        }
        return true;
    }
};
    
