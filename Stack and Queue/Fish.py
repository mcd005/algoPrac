'''
Problem description: https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

Time complexity     O(n)
Space complexity    O(n)
'''

def solution(A, B):
    N = len(A)
    if N == 1: #i.e. there's only 1 fish, no eating will take place so no extra computation required
        return 1
       
    #Initialise two queues which will be used to keep track of the surviving fishes and their directions
    sizes = [A[0]]
    directions = [B[0]]
    
    #Iterate through the list of fishes, starting from the most upstream fish to the most downstream fish
    for i in range(1, N):
        nextFish = 0
        #Determine if two fish are meeting. This only occurs when an upstream fish is swimming downstream and a downstream fish is swimming upstream
        #After a fish eats, it can go on to meet other fish hence the while loop
        while directions[-1] == 1 and B[i] == 0:
            #If the upstream fish is bigger, it eats the downstream fish
            if sizes[-1] > A[i]:
                #This flag is used to make sure the fish that has just been eaten is not appened to the q of surviving fishes
                nextFish = 1
                break
            elif sizes[-1] == A[i]:
                break
            else:
                #If the downstream fish is bigger it eats the upstream fish.
                #The uptream fish is removed from the q of surviving fishes
                sizes.pop()
                directions.pop()
                if not sizes:
                    break
                    #This is necesarry if a downstream fish eats all the fishes upstream of it
        if nextFish == 0:       
            sizes.append(A[i])
            directions.append(B[i])
            #If two fish aren't meeting then add the current fish to the list of surviving fish
            
    return len(sizes)