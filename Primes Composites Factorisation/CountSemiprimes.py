'''
https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_semiprimes/

Mark all the semiprimes from 1 to N
    This first involves generating all the primes up to N (using Erathosthenes Sieve)
    Once this is done, we then iterate through the sieve and if a prime is encountered, we multiply it with the other primes encountered and mark the result in an array of size N + 1 called semiprimes
Use to prefix sum array to mark where semiprimes are so you could look up in constant time how many there are in a range
Iterating though the queries, we append the result of each to the array


Time complexity         O(n*log(log n) + n^2 + n + m)   to generate the primes, mark the semiprimes, generate a prefix sum array and process the queries respectively
TC simplified           O(n^2 + m)

Space complexity        O(n + m)

Is there a quicker way to get semiprimes?
'''

#Function to generate primes up to n
def sieve(n):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    
    i = 2
    while i * i < n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = 0
                k += i
        i += 1
        
    return sieve


def solution(N, P, Q):
    n = (N//2) + 1
    
    primes = sieve(n)
    semiprimes = [0] * (N + 1)
            
    for i in range(n + 1):
        if primes[i] == 1:
            for j in range(i, n + 1):
                if i*j > N:
                    break
                elif primes[j] == 1:
                    semiprimes[i*j] = 1
                
    semiprimesPS = [0] * (N + 2)
    for i in range(1,N + 2):
        semiprimesPS[i]  = semiprimes[i - 1] + semiprimesPS[i - 1]
        
    M = len(P)
    result = []
    for i in range(M):
        result.append(semiprimesPS[ Q[i] + 1 ] - semiprimesPS[ P[i] ])
    
    return result