'''
Problem Description: https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/

Standard HashMap problem
'''
def solution(A):
    distinct = set()
    
    for i in range(len(A)):
        if abs(A[i]) not in distinct:
            distinct.add(abs(A[i]))
            
    return len(distinct)
    