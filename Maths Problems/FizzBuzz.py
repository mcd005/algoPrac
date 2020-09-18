'''
Classic algo problem

Make sure you avoid mistakes with bad if else statements
Account for the multiples of 15 edge cases

Time compelxity     O(n)
Space complexity    O(1)
'''

def fizzBuzz(N):
    for i in range(1, N + 1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if not result:
            result = i
        print(result)

fizzBuzz(100)