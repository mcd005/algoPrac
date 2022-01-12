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