// Version 1 
class Solution
{
public:
    vector<string> topKFrequent(vector<string> &words, int k)
    {
        // word : occurence
        unordered_map<string, int> m;
        for (auto word : words)
            m[word]++;

        priority_queue<pair<int, string>> pq;
        for (auto &[word, occurrence] : m)
        {
            pq.push({-occurrence, word}); // trick to build min heap
            if (pq.size() > k)
                pq.pop(); // pop off the smaller pair
        }
        vector<string> result(k);
        int i = pq.size() - 1;
        while (!pq.empty())
        {
            result[i] = pq.top().second;
            pq.pop();
            i--;
        }
        return result;
    }
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> count;
        for (string& w : words) {
            count[w]++;
        }
        vector<pair<string, int>> freq;
        for (auto c : count) {
            freq.push_back(make_pair(c.first, c.second));
        }
        partial_sort(freq.begin(), freq.begin()+k, freq.end(), [] (auto& l, auto& r) {
            if (l.second == r.second) {
                return l.first < r.first;
            }
            return l.second > r.second;});
        vector<string> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(freq[i].first);
        }
        return ans;
    }
};