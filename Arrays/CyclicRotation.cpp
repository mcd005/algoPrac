/*
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

Array slicing problem
Need to do some modulo math and the from there you only need to slice accordingly

Time complexity         O(n)
Space complexity        O(n)
*/

#include <vector>

vector<int> solution(vector<int> &A, int K) {
	if (A.size() == 0{
		return A;
	}
    vector<int> v1;
    vector<int> v2;
    
    K = K % A.size();
    
    v1 = vector<int>(A.end() - K, A.end());
    v2 = vector<int>(A.begin(), A.end() - K);
    v1.insert(v1.end(), v2.begin(), v2.end());
    
    return v1;
}
