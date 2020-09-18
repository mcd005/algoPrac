#include <vector>
#include <deque>

int solution(vector<int> &A, vector<int> &B) {
    int N = A.size();
    if (N == 1) return 1;
    
    std::deque<int> sizes;
    std::deque<int> directions;
    
    sizes.push_back(A[0]);
    directions.push_back(B[0]);
    
    for (int i = 1; i < N; i++){
        int nextFish = 0;
        while (directions.back() == 1 and B[i] == 0){
            if (sizes.back() > A[i]){
                nextFish = 1;
                break;
            }
            else if (sizes.back() == A[i]){
                break;
            }
            else{
                sizes.pop_back();
                directions.pop_back();
                if (sizes.empty()){
                    break;
                }
            }
        }
        if (nextFish == 0){
            sizes.push_back(A[i]);
            directions.push_back(B[i]);
        }
    }
    
    return (sizes.size());
}