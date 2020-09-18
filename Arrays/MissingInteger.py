#Max number of distinct intengers that can be encountered is equal to the size of the input array
#Therefore we create a boolean array (result) to mark which  positive integer has been encountered
#After walking through the input array and marking the corresponding positive integers in the result array
#we walk through the result array and the first False encountered is the smallest positive integer that does not occur
#If there are no False values in result then the smallest positiive integer not to occur must be one greater than the max in False

#Time Complexity    O(N)
#Space Complexity   O(N)

def solution(A):
    N = len(A)
    result = [0]*N
    
    for i in range(N):
        #"smallest positive integer" means the value of any negative int is irrelevant
        #Equally if an int encountered is greater than  N its value is alos irrelevant because "smallest" means result is bounded by N
        if (A[i] > 0 and A[i] <= N): 
            result[A[i] - 1] = 1
    
    for i in range(N):
        if result[i] == 0:
            return i + 1
    return i + 2