// See BITWISEXOR .cpp for a better solution
#include <map>

int solution(vector<int> &A) {
    map<int,int> occurences;
  
    for (int i = 0; i < A.size(); i++){
        occurences[A[i]]++;
    }
    
    for (auto pair : occurences){
        if (pair.second % 2 == 1){
            return pair.first;
        }
    }
}

