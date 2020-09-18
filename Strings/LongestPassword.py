'''
Problem description: https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password/

Iterate through the entire string
    Check if letter is alphanumeric
    Increment the relevant counter
    When a space is encountered check if the password is valid based on these counts
        If one of the chars encountered was illegal then this check immediately fails
        Otherwise if it is valid then compare it's length to the current max
        Reset counts to zero and validity to false
Repeat until the end of the string
Then check the valdidity of the last password

Time complexity         O(n)
Space complexity        O(1)

For interests sake this could have also been done by splitting the string at the spaces, sorting the passwords by size and then iterating
through them until a valid one was encountered and reutrning it's length
However this would have been slower time wise ( O(nlogn) ) and taken up more space O(n)
'''

def solution(S):
    N = len(S)

    legalChars = True
    numLetters = 0
    numDigits = 0
    maxValid = -1

    for i in range(N):
        if S[i].isalpha():
            numLetters += 1
        elif S[i].isdigit():
            numDigits += 1
        elif S[i].isspace():
            if legalChars and (numLetters % 2 == 0) and (numDigits % 2 == 1):
                maxValid = max(maxValid, numLetters + numDigits)
            legalChars = True
            numLetters = 0
            numDigits = 0
        else:
            legalChars = False

    if legalChars and (numLetters % 2 == 0) and (numDigits % 2 == 1):
                maxValid = max(maxValid, numLetters + numDigits)

    return maxValid