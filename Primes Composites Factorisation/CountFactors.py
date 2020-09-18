'''
Count the number of factors of an integer N

Problem description: https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
Implementation of algorithm in 10.1 of https://codility.com/media/train/8-PrimeNumbers.pdf

Time Complexity         O(sqrt(n))
Space Complexity        O(1)
'''


def solution(N):
    i = 1
    count = 0
    
    while (i * i < N):
        if (N % i == 0):
            count += 2
        i += 1
    if (i * i == N):
        count += 1
    return count