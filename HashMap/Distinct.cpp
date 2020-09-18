#include <set>

int solution(vector<int> &A) {
    std::set<int> seen;
    for (int i = 0; i < A.size(); i++){
        if (seen.find(A[i]) == seen.end()){
            seen.insert(A[i]);
        }
    }
    return seen.size();
}