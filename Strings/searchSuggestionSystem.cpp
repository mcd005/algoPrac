class Solution
{
public:
    vector<vector<string>> suggestedProducts(vector<string> &products, string searchWord)
    {
        sort(products.begin(), products.end());
        int a = 0;
        int b = products.size() - 1;

        vector<vector<string>> result(searchWord.size());
        for (int i = 0; i < searchWord.size() && a <= b; ++i)
        {
            while (
                a <= b &&
                // Skip products[a] if index i is not a match
                (products[a].size() <= i || products[a][i] != searchWord[i]))
            {
                ++a;
            }
            while (
                a <= b &&
                // Skip products[b] if index i is not a match
                (products[b].size() <= i || products[b][i] != searchWord[i]))
            {
                --b;
            }

            // Pick the first 3 starting from a,
            // but not going over b
            for (int k = a; k <= b && k < a + 3; ++k)
            {
                result[i].push_back(products[k]);
            }
        }
        return result;
    }
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        vector<vector<string>> ret(searchWord.size(), vector<string>());
        sort(products.begin(), products.end());
        auto start = products.begin();
        auto end = products.end();
        string prefix;
        for (size_t index = 0; index < searchWord.size(); ++index) {
            prefix += searchWord[index];
            start = lower_bound(start, end, prefix);
            int count = 0;
            while (count < 3) {
                bool bMatch = true;
                auto ss = start + count;
                if (ss == end) {
                    break;
                }
                
                for (size_t i = 0; i < prefix.size(); ++i) {
                    if (prefix[i] != ss->at(i)) {
                        bMatch = false;
                        break;
                    }
                }
                if (bMatch) {
                    ret[index].emplace_back(*ss);
                }
                else {
                    break;
                }
                
                ++count;
            }
        }
        
        return ret;
    }
};