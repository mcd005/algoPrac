// Version 1 - Like V1 in .cpp, except we don't use a trie to prune searches
class Solution {
public:
    
    void solve(string &s, int l, string curr, unordered_map<string,bool> &hash, vector<string> &answer) {
        if(l == s.size()) {
            answer.push_back(curr.substr(1, curr.size() - 1));
            return;
        }
        string temp = "";
        for(int i = l; i < s.size(); ++i) {
            temp += s[i];
            if(hash[temp]) {
                string ncurr = curr + " " + temp;
                solve(s, i + 1, ncurr, hash, answer);
            }
        }
    }
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> answer;
        unordered_map<string,bool> hash;
        for(auto w : wordDict) {
            hash[w] = true;
        }
        string curr = "";
        solve(s, 0, curr, hash, answer);
        return answer;
    }
};