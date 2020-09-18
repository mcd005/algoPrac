#include <vector>
#include <stack>

int solution(vector<int> &H) {
    int N = H.size();
    if (N == 1) return 1;
    
    std::stack<int> s;
    int blocksSaved = 0;
    s.push(H[0]);
    
    for (int i = 1; i < N; i++){
        while (!s.empty() && H[i] < s.top()){
            s.pop();
        }
        if (!s.empty() and H[i] == s.top()){
            blocksSaved++;
        }
        s.push(H[i]);
    }
    return N - blocksSaved;
}
