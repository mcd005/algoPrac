// you can use includes, for example:
// #include <algorithm>
#include <map>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

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

