// See .py for solution

using namespace std;

vector<int> solution(int N, vector<int> &A) {
    vector<int> result(N,0);
    int currentMax = 0;
    int currentBaseline = 0;
    
    for (int i = 0; i < A.size(); i++){
        if (A[i] <= N){
            if (result[A[i] - 1] > currentBaseline){
                result[A[i] - 1]++;
            }
            else{
                result[A[i] - 1] = currentBaseline + 1;
            }
            currentMax = max(result[A[i] -1], currentMax);
        }
        else{
            currentBaseline = currentMax;
        }
    }
    
    for (int i = 0; i < result.size(); i++){
        if (result[i] < currentBaseline){
            result[i] = currentBaseline;
        }
    }
    
    return result;
}