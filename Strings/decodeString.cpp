// https://leetcode.com/problems/decode-string/
// Version 1 - Recursive
// while there are letters append them to the output
// while there are digits, convert them to k
// when you hit an open bracket run ahead to the corresponding close bracket (check for levels of nesting)
// call expand on everything between those two brackets
// jump ahead to after that bracket and continue
// Time Complexity         O(n)
// Space Complexity         O(n)
// space is based on how many recursive calls are put on the stack. Based on deepeest nested string 
// improved version of this modifies modifies i in the recursive calls and 
// looks for closing bracket in a way calls on the bottom can benefit from
class Solution {
public:
    string decodeString(string s) {
       return expand(s, 0, s.size());
    }

    string expand(string& str, int start, int end)
    {
        string output = "";
        int curK = 0;

        int i = start;
        while (i < end)
        {
            if (isalpha(str[i])) output += str[i];
            else if (isdigit(str[i])) curK = (curK * 10) + (str[i] - '0');
            else
            {
                int newStart = i + 1;
                int numOpen = 1;
                while (numOpen != 0)
                {
                    ++i;
                    if (str[i] == '[') ++numOpen;
                    else if (str[i] == ']') --numOpen;
                }
                string expanded = expand(str, newStart, i);
                for (int j = 0; j < curK; ++j)
                {
                    output += expanded;
                }
                curK = 0;
            }
            ++i;
        }

        return output;
    }
};