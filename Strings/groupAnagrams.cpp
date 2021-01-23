// https://leetcode.com/problems/group-anagrams/

// Version 1 - Sort each string with count sort; use sorted strings as keys in a map
// Time complexity      O(n*m)  for n strings of length m
// Space complexity     O(n)
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anaDict;
        for (auto word: strs){
            string sortedWord = countSort(word);
            if (anaDict.find(sortedWord) != anaDict.end()){
                anaDict[sortedWord].emplace_back(word);
            }
            else{
                anaDict[sortedWord] = vector<string>{word};
            }
        }
        
        vector<vector<string>> output;
        for (auto item: anaDict){
            output.emplace_back(item.second);
        }
        
        return output;
    }
    
    string countSort(string ana){
        int counts[26] = {0};
        int m = ana.size();
        for (int i = 0; i < m; ++i){
            ++counts[ana[i] - 97];
        }
        
        string out = "";
        for (int i = 0; i < 26; ++i){
            while(counts[i]-- > 0){
                out += i + 97;
            }
        }
        return out;
    }
};

// Version 2 - Same as 1 but use inbuilt sort
// Turns out it's actually faster in ms despite being worse TC
// Time complexity      O(n * mlogm)
// Space complexity     O(n)
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        for(auto str : strs)
        {
            string temp = str;
            sort(temp.begin(), temp.end());
            mp[temp].push_back(str);
        }
        
        vector<vector<string>> res;
        for(auto mem : mp)
        {
            res.push_back(mem.second);
        }
        
        return res;
    }
};

// Version X - use some kind of hashing
// This is the first approach I had in mind
// Have each nth ASCII value after 97 ("a")
// map to the nth prime
// Then a string would be the product of all the primes the chars mapped to
// This has issues with integer overflow though (unless we use some modulo to keep it bounded)
// Could maybe create hashes from counts instead?
//Eg: cat becomes 1a1c1t. caabbt becomes 2a2b1c1t