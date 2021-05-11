// https://leetcode.com/problems/reorder-data-in-log-files//
// Version 1 - Stable partition then sort. All in place
// Time complexity      O(NlogN)
// Space complexity     O(N) if we're being strict but all mem allocated is temporary (partition, sort and std::string())
class Solution
{
public:
    vector<string> reorderLogFiles(vector<string> &logs)
    {
        // Partition so that all the digit logs are at then end in their relative order
        stable_partition(logs.begin(), logs.end(), isLetterLog);

        // Find the first digit log
        int n = logs.size();
        int firstDigLog = n - 1;
        for (int i = 0; i < n; ++i)
        {
            if (!isLetterLog(logs[i]))
            {
                firstDigLog = i;
                break;
            }
        }

        sort(logs.begin(), logs.begin() + firstDigLog,
             [](string &a, string &b) {
                 auto aFirstSpace = a.find(" "), bFirstSpace = b.find(" ");
                // Then sort logs before the index of that log:
                // either the contents of a are lexo less
                // or if the contents are equal
                // then we sort by ids
                 return (lexicographical_compare(a.begin() + aFirstSpace + 1, a.end(), b.begin() + bFirstSpace + 1, b.end()) ||
                         std::string(a.begin() + aFirstSpace, a.end()) == std::string(b.begin() + bFirstSpace, b.end()) &&
                             lexicographical_compare(a.begin(), a.begin() + aFirstSpace, b.begin(), b.begin() + bFirstSpace));
             });

        return logs;
    }

    static bool isLetterLog(string &log)
    {
        return !isdigit(log[log.find(" ") + 1]);
    }
};

// Version 2 - Found on LC. Split letter logs into ID and contents for easier sorting
class Solution
{
public:
    vector<string> reorderLogFiles(vector<string> &logs)
    {
        vector<string> digitLogs, ans;
        vector<pair<string, string>> letterLogs;
        for (string &s : logs)
        {
            int i = 0;
            while (s[i] != ' ')
                ++i;
            if (isalpha(s[i + 1]))
                letterLogs.emplace_back(s.substr(0, i), s.substr(i + 1));
            else
                digitLogs.push_back(s);
        }
        sort(letterLogs.begin(), letterLogs.end(), [&](auto &a, auto &b) {
            return a.second == b.second ? a.first < b.first : a.second < b.second;
        });
        for (auto &p : letterLogs)
            ans.push_back(p.first + " " + p.second);
        for (string &s : digitLogs)
            ans.push_back(s);
        return ans;
    }
};