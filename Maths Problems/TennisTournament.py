'''
Problem Description: https://app.codility.com/programmers/lessons/92-tasks_from_indeed_prime_2016_college_coders_challenge/tennis_tournament/

Trivial modulo maths

Time complexity         O(1)
Space complexity        O(1)
'''

def solution(P, C):
    return min(C, P // 2)