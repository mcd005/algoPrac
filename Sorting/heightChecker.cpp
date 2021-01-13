/*  
https://leetcode.com/problems/height-checker/

Not a well defined problem.
Essentially we need to count the number of integers that are not at the index they would be if they were sorted in ascending order

~~~~Version 1~~~~
The naive approach
Make a copy of the array for reference and then sort it in place
Iterate through both the sorted array and the reference and see where they differ.

Time complexity     O(nlogn)
Space complexity    O(n)


~~~~Version 2~~~~
Count sort
Because each height is in the set of numbers from 1 to 100 (per the problem defintion) we can:
Iterate through the array and count the occurences of each height. This gives us an array that looks like: 
index   0 1 2 3 4 5 ... 101
count   0 3 1 1 1 0 ... 0
i.e. the sorted array will have three 1s first, one 2 etc

Time complexity     O(n)
Space complexity    O(1)    if we agree that the set of heights is a constant
*/

//Version 2
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int heightCount[101] = {0};
        
        for (int height: heights){
            ++heightCount[height];
        }
        
        int result = 0;
        int cntrIdx = 1;
        
        for (int h: heights){
            while (heightCount[cntrIdx] == 0 ) ++cntrIdx;
            
            if (h != cntrIdx){
                ++result;
            }
            
            --heightCount[cntrIdx];
        }
        
        return result;
    }
};

//Version 1
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> original = heights;
        sort(heights.begin(), heights.end());
        
        int result = 0;
        int n = heights.size();
        for (int i = 0; i < n; ++i){
            if (heights[i] != original[i]) result++;
        }
        return result;
    }
};