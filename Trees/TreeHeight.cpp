/*
See TreeHeight.py for problem description

Recursive solution

Time complexity 		O(n)
Space compexlity		O(tree height) == O(n) in worst case	i.e. O(recursion depth) where recursion depth =  no. return statements executed before base case
*/

#include <algorithm> //For std::max

int solution(tree * T) {
    if (T->l == NULL && T->r == NULL){
        return 0;
    }
    else if (T->l == NULL){
        return 1 + solution(T->r);
    }
    else if (T->r == NULL){
        return 1 + solution(T->l);
    }
    else{
        return 1 + std::max(solution(T->l), solution(T->r));
    }
}