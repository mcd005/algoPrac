'''
Problem description: https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

My solution based on https://rafal.io/posts/codility-genomic-range-query.html

Time complexity     O(N + M)
Space complexity    O(N + M)
'''

#Helper function so can index 2D array more easily
def computeImpFac(ntide):
        if ntide is "A":
            return 0
        elif ntide is "C":
            return 1
        elif ntide is "G":
            return 2
        elif ntide is "T":
            return 3
        else:
            print("Invalid nucleotide")


def solution(S, P, Q):
    N = len(S)
    M = len(P)
    #Create a 2D array where each of the 4 rows will be a prefix sum array for one of the nucleotides 
    prefs = [[0 for x in range(N)] for y in range(4)]
    result = [0] * M
    
    #Iterate through the whole genomic sequence and mark the positition of each nucleotide in its respective row of the 2D array 
    for i in range(N):
        nuc = S[i]
        IF = computeImpFac(nuc) #IF is impact factor
        prefs[IF][i] = 1
    
    #Now convert the rows into prefix sum arrays
    #These will allow us to get the number of occurences of a given nucleotide between two indices of the genomic sequence
    for i in range(1,N):
        for j in range(4):
            prefs[j][i] += prefs[j][i -1]

    #Iterate through the list of queries
    for i in range(M):
        x = P[i]
        y = Q[i]
        
        #If the query asks for the minimum IF of a sequence 1 element long, then the result is just the IF of that element 
        if x == y:
            result[i] = computeImpFac(S[x]) + 1
        else:
            #Otherwise, we ask: "Is nucleotide A present between indices in the query?" 
            #   Yes - return IF of A
            #   No - then we ask "Is nucleotide C present between indices in the query?"
            #And so on, going up the list of nucleotides in ascending order
            for j in range(4):
                sub = 0
                if (x - 1 >= 0):
                    sub = prefs[j][x - 1]
                if(prefs[j][y] - sub > 0):  #this difference would be zero if no nucleotides of the type in question are present in that range
                    result[i] = j + 1
                    break
                #Sub is to account for edge cases where queries have P[i] = 0 and thus would have "index out of range" if we applied the usual -1 shift to the index used for the prefix sum
    
    return result