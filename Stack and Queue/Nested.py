'''
This problem is just a simpler version of Brackets.py
'''

def solution(S):
    if len(S) == 0:
        return 1
    elif len(S) == 1:
        return 0
        
    q = []
    for char in S:
        if char == '(':
            q.append(char)
        elif not q:
            return 0
        else:
            if ((q[-1] == "(") and (char == ")")):
                q.pop()
            else:
                return 0
    if (not q):
        return 1
    else:
        return 0