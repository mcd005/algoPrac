'''
Given an integer input, reverse this number, add them together and check if the result was a palindrome
If it was not continue using the new number until the answer is a palindrome.
If the result is a palindrome, output the number of times needed to achieve this result and the resulting number
'''

def isPalin(num):
    strNum = str(num)
    if strNum == strNum[::-1]:
        return True
    else:
        return False

def intPalin(integer):
    seen = set()
    count = 0
    while True:
        new = integer + int(str(integer)[::-1])
        count += 1
        if isPalin(new):
            return count
        elif new in seen:
            return -1
        else:
            seen.add(new)
            integer = new

#Driver code
print(intPalin(99))