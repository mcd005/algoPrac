int solution(vector<int> &A) {
    int result = 0;
    for (int i = 0; i < A.size(); i++){
        result = (i + 1) ^ A[i] ^ result;
    }
    return !result ? 1 : 0;
}