#include <vector>

int solution(vector<int> &A) {
    int N = A.size();
    
    if (N == 0) return -1;
    
    int candidate = A[0];
    int size = 1;
    
    for (int i = 1; i < N; i++){
        if (size == 0){
            candidate = A[i];
            size++;
        }
        else{
            if (candidate != A[i]){
                size--;
            }
            else{
                size++;
            }
        }
    }
    
    int count = 0;
    for (int i = 0; i < N; i++){
        if (A[i] == candidate){
            count++;
            if (count > N/2){
                return i;
            }
        }

    }
    return -1;
}