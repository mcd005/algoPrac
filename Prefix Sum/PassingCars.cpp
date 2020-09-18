#include <numeric>

int solution(vector<int> &A) {
    int passing = 0;
    int westbound = std::accumulate(A.begin(), A.end(), 0);
    for (int i = 0; i < A.size(); i++){
        if (passing > 1000000000){
            return -1;
        }
        else if (A[i] == 1){
            westbound--;
        }
        else{
            passing += westbound;
        }
    }
    return passing;
}