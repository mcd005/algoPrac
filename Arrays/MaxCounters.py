# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

#Iterate through A
#Apply increase as instructed
#Check if the new value exceeds the max
#Set that as the max above baseline
#When max counter oepration is applied, update the baseline
#Lazy write policy: if a value to be increased is below the baseline, then it has yet to be written to. 
#   Update its value with the correct baseline
#   Then iterate through all the results at the end updating correct baseline

#Time O(N + M)
#Space O(N)

def solution(N, A):
    result = [0]*N #Ideally would do this with itertools so that time complexity is O(1)
    currentMax = 0
    currentBaseline = 0
    
    for i in range(len(A)):
        if A[i] <= N:
            if result[A[i]-1] > currentBaseline:
                    result[A[i]-1] += 1
            else:
                result[A[i]-1] = currentBaseline + 1
            currentMax = max(result[A[i]-1],currentMax)
        else:
            currentBaseline = currentMax
            
        # print(result)
        # print("Current max is: {} \n".format(currentMax))
        # print("Current baseline is: {} \n\n".format(currentBaseline))
            
    for i in range(len(result)):
        if result[i] < currentBaseline:
            result[i] = currentBaseline
            
    return result