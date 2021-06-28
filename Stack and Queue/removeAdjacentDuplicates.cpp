// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/submissions/

// Version 1 - Stack and two pointers
// Time complexity     O(n)
// Space complexity    O(n)
class Solution
{
public:
    string removeDuplicates(string s, int k)
    {
        // String builder stack (which we'll implement using a vector for simplicity)
        // char, num_adjacent
        vector<pair<char, int>> stack;

        int n = s.size();
        int back = 0;
        // Back is used to mark char at start of run of adj chars
        for (int front = 0; front < n + 1; ++front)
        {
            // Either we are at the end of run or at the end of the string
            if (front == n || s[back] != s[front])
            {
                int runLength = (front - back) % k;
                if (runLength != 0)
                {
                    // If this current run is going to extend a previous run
                    if (!stack.empty() && s[back] == stack.back().first)
                    {
                        stack.back().second += runLength;
                        stack.back().second %= k;
                        // The additional run may result enough adj chars for the run to removed
                        if (stack.back().second == 0) stack.pop_back();
                    }
                    else stack.emplace_back(s[back], runLength);
                }
                // Start a new run
                back = front;
            }
        }

        // Construct the string from the stack
        string output = "";
        for (auto el: stack)
        {
            output.append(el.second, el.first);
        }

        return output;
    }
};

// Version 2 - Just a stack (from leetcode submissions)
// Time complexity     O(n)
// Space complexity    O(n)
class Solution
{
public:
    string removeDuplicates(string s, int k)
    {

        vector<pair<char, int>> st;
        for (char c : s)
        {
            if (st.empty() || st.back().first != c)
            {
                st.push_back({c, 1});
            }
            else if (++st.back().second == k)
                st.pop_back();
        }
        string result = "";
        for (auto t : st)
        {
            result.append(t.second, t.first);
        }
        return result;
    }
};

// Version 3 - Just two pointers (from leetcode discussions)
// Time complexity     O(n)
// Space complexity    O(n)
class Solution
{
public:
    string removeDuplicates(string s, int k)
    {
        // i is our write pointer and j our is read pointer
        int i = 0, n = s.length();
        // count[x] records the number of chars in a row before s[x] that are the same as s[x]
        vector<int> count(n);
        for (int j = 0; j < n; ++j, ++i)
        {
            s[i] = s[j];
            // Read head moves along and counts number of chars in a row
            count[i] = i > 0 && s[i - 1] == s[j] ? count[i - 1] + 1 : 1;
            // We move back the write head by k chars, allowing them to be overwritten
            if (count[i] == k) i -= k;
        }
        // Return only the prefix of the string that the write head has written to
        return s.substr(0, i);
    }
};