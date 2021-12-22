/*
Problem description: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/#:~:text=A%20binary%20gap%20within%20a,binary%20gap%20of%20length%202.

Examine the LSB of N by taking it's modulo 2
Check if the current bit is in a binary gap by looking at its value and the value of the previous bit
If it is in a binary gap, increment the counter that is keeping track of the size of the current gap
Each iteration check if this counter is greater than the than the size of any gap previously seen (could check this at the end of a gap if you wanted to be bit more efficient)
Divide N by two and repeate until N < 0 (per C++ int division)

Time complexity 	O(log n)
Space complexity 	O(1)
*/

#include <bitset>
#include <vector>
	
int solution(int N) {
	int maxGap = 0;
	int currentGap = 0;
	bool inGap = false;

	int currentBit;
	int previousBit = 0;

	while (N > 0) {
		currentBit = (N % 2);
		if (previousBit == 1 and currentBit == 0) {
			inGap = true;
		}
		if (currentBit == 1) {
			inGap = false;
			currentGap = 0;
		}
		if (inGap == true) {
			currentGap++;

			if (currentGap > maxGap) {
				maxGap = currentGap;
			}
		}
		//cout << currentBit << " " << currentGap << endl;
		previousBit = currentBit;
		N = N / 2;
	}
	return maxGap;
}
