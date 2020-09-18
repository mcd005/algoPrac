'''
Problem description: https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/

Used the alorithm that can determine the factors of a number in O(srqt(n))
And for each pair of factors checked if it's perimeter was smaller than the smallest perimeter seen until this point

Time complexity         O(srqt(n))
Space complexity        O(1)
'''

def solution(N):
    minPerim = 2 * (1 + N)
    
    i = 2
    while (i * i <= N):
        if (N % i == 0):
            minPerim = int(min(minPerim, 2 * (i + N/i)))
        i += 1
    return minPerim