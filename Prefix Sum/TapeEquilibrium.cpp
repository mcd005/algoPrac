/* 
https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

Sum all of the elements but the first: this is the right half of the array
The left half is the first element
Iterate through the array and for each value subtract the element from right and add it to left
Keep track of the min difference between the two halves and return it at the end

Time complexity     O(n)
Space complexity    O(1)
 */
#include <math.h>
#include <numeric>

int solution(vector<int> &A) {
    int left = A[0];
    int right = accumulate(A.begin()+1, A.end(), 0);
    int minDiff = abs(left - right);

    for (int i = 0; i < A.size() - 1; i++){
        left += A[i];
        right -= A[i];
        if (abs(left - right) < minDiff){
            minDiff = abs(left - right);
        }
    }
    return minDiff;
}
