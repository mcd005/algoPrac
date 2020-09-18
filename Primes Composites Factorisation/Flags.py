'''
Establish where the peaks are
Choosing to take less flags than peaks sets an upper limit on the number of flags that can be set

How many potential flag settings are we losing by taking fewer flags vs taking lots of flags
Surely you want to at least start with the maximum because the peaks could be reasonably well spaced out

Edge case: there are 4 peaks but each have a seperation of 3. If you took 4 flags then you could only place 2 of them
If you took three flags instead then you could place all three

Say there are 5 peaks, each with a seperation of 2
'''

def solution(A):
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
    print(peaks)
