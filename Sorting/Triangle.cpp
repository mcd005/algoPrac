#include <algorithm>

int solution(vector<int> &A) {
    if (A.size() < 3){
        return 0;
    }
    std::sort(A.begin(), A.end());
    for (int i = 0; i < A.size() - 2; i++){
        long long int a = A[i]; //Long long to account for potential integer overflow            
        long long int b = A[i + 1];
        long long int c = A[i + 2];
        if ( (a + b > c) && (b + c > a) && (c + a > b) ){
            return 1;
        }
    }
    return 0;
}