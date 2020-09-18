// you can use includes, for example:
// #include <algorithm>
#include <math.h>
#include <numeric>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

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
