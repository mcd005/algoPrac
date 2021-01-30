// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting

// Version 1 - Sort the dict in descending length
// Use two pointers to scan the string to find matching chars
// Time complexity      O(nlogn + nm)
// Space complexity     O(1)
// where n is the number of words in d and m is the length of s
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(), d.end(), [](string &a, string &b) {
            return (a.size() > b.size() || a.size() == b.size() && a < b);
            });
        
        int m = s.size();
        for (auto word: d){
            int n = word.size(), i = 0, j = 0;
            while (i < n){
                if (j < m && s[j] != word[i]) ++j;
                else if (s[j] == word[i]) ++i, ++j;
                else break;
            }
            if (i >= n) return word;
        }
        return "";
    }
};

// Version 2 - Fastest I could find on LC
// Fairly similar to v1 but string search
// made own function for speed
class Solution {
public:
    static bool is_subsequence(const string& sup, const string& sub) {
        int i = 0;
        for (const char c : sub) {
            while (i < sup.size() && sup[i] != c) i++;
            if (i == sup.size()) return false;
            i++;
            // cout << i << " " << char(sup[i]) << endl;
        }
        return true;
    }
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(), d.end(), [](auto& a, auto& b) {
            return a.size() == b.size() ? a < b : a.size() > b.size();
        });
        for (const auto& t : d) {
            // cout << t << endl;
            if (is_subsequence(s, t)) return t;
        }
        return "";
    }
};