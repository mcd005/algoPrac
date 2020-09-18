#If we bitwise xor each element with its index + 1, then bitwise xor the results for all indices
#Then the output should be 0 if all values are present (i.e. is a permutation)
#And !0 otherwise (isn't a permutation)

#Time Complexity O(N)
#Space Complexity O(1)

def solution(A):
    result = 0;
    for i in range(len(A)):
        result = (i+1) ^ A[i] ^ result
    return 1 if (not result) else 0
    
#What would it take for a false positive?
#Would need left over 1s to match the excess 1s
#And that could only happen with repeated values or values out of range?