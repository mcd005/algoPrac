#https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
#Sum all the ones in the array
#Then walk through the array
    #When a 1 is encountered decremet the sum
    #When zero is encountered add the sum to the result
    #Check each iteration if result exceeds max cars
#Return result at the end of the loop

#Time complexity:   O(N)
#Space complexity:  O(1)

def solution(A):
    passing = 0
    westbound = sum(A)
    for car in A:
        if passing > 1000000000:
            return -1
        elif car == 1:
            westbound -= 1
        else:
            passing += westbound
    return passing

#NB: Considered usign a suffix sum method where number of remianing westobound cars for a given index would be stored at the index of a corresponding array, however this would require O(N) space