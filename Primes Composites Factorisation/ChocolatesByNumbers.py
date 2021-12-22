'''
Problem Description: https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

Look for the LCM multiple of N and M and then see how many times M goes into it.

Time complexity     O(log a + b)
Space complexity    O(1)

Alternative Solution:
I can think of a linear time solution, where you just counting counting round an each time you "eat a chocolate" you add it's modulo to a hashmap
'''

def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a % b)
        
def lcm(a,b):
    return a * b / gcd(a, b)

def solution(N, M):
    return int(lcm(M,N) / M)