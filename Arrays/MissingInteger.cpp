int solution(vector<int> &A) {
    int N = A.size();
    int result[N] = {};
    
    for (int i = 0; i < N; i++){
        if (A[i] > 0 && A[i] <= N){
            result[A[i] - 1] = 1;
        }
    }
    
    for (int i = 0; i < N; i++){
        if (result[i] == 0){
            return i + 1;
        }
    }
    return N + 1;
}
