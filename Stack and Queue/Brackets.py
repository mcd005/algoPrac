'''
Problem Description: https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

Iterate through the string
If the character is an opening parenthesis then enqueue 
If the character is a closing parenthesis, check if it closes the parenthesis at the back of the queue
If it does pop remove that item from the back of the queue
If not then return 0
Or check the queue at the end an if it is not empty return 0

Time complexity     O(n)
Space complexiy     O(n)
'''

def solution(S):
    if len(S) == 0:
        return 1
    elif len(S) == 1:
        return 0
        
    opens = {"(", "{", "["}
    q = []
    for char in S:
        if char in opens:
            q.append(char)
        elif not q:
            return 0
        else:
            if ((q[-1] == "(") and (char == ")")) or ((q[-1] == "{") and (char == "}")) or ((q[-1] == "[") and (char == "]")):
                q.pop()
            else:
                return 0
    if (not q):
        return 1
    else:
        return 0