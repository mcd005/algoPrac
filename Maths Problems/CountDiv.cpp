/*
Problem description: https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

Time complexity         O(1)
Space complexity        O(1)
*/

int solution(int A, int B, int K) {
    if (A % K == 0){
        return (B-A)/K + 1;
    }
    else{
        return ((B-A) + (A % K))/K;
    }
}