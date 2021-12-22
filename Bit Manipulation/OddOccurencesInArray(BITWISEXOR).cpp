// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
#include <bits/stdc++.h> 
using namespace std; 

// Iterate through the array and bitwise XOR each value with result
// This is the programming equivalent of it all coming out in the wash
// If you bitwise XOR all the elements in the array i.e. 0 ^ arr[0] ^ arr[1] ^ arr[2] etc
// Then all the duplicates (i.e. all of the n multiples of two) will cancel out because A ^ A === 0
// But then the odd values will be left over and B ^ 0 === B
int getOddOccurrence(int ar[], int ar_size) 
{ 
	int res = 0; 
	for (int i = 0; i < ar_size; i++)	 
		res = res ^ ar[i]; 
	
	return res; 
} 

/* Driver code */
int main() 
{ 
	int ar[] = {2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2}; 
	int n = sizeof(ar)/sizeof(ar[0]); 
	
	cout << getOddOccurrence(ar, n); 
	
	return 0; 
} 
