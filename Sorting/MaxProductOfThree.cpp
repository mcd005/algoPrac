#include <algorithm>

int solution(vector<int> &A) {
    std::sort(A.begin(), A.end());
    int N = A.size();
    if (A[N - 1] < 0){
        return (A[N - 3] * A[N - 2] * A[N - 1]);
    }
    else{
        return max( (A[0] * A[1]) , (A[N - 3] * A[N - 2]) ) * A[N - 1];
    }
}