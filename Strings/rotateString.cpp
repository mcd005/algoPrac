/*
https://leetcode.com/problems/rotate-string/

See Python solution for explanation
Included this C++ solution so I can refer to this if I need to remember CPP-specific .find(str) function
*/

bool rotateString(string A, string B) {                
    return A.size() == B.size() && (A + A).find(B) != string::npos;
}  