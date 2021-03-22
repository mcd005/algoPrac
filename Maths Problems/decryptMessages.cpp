/*
FROM PRAMP:

Messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

Convert every letter to its ASCII value. 
Add 1 to the first letter.
Then for every letter from the second one to the last one, add the value of the previous letter. 
Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII.
Convert the values back to letters.

For instance, to encrypt the word “crime”

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
Step 3:	100	110	111	116	113
Encrypted message:	d	n	o	t	q
*/

#include <iostream>
#include <string>
using namespace std;

// Version 1 
// If enc[i] = dec[i] + prevStepTwo + 26m
// then dec[i] = enc[i] - prevStepTwo - 26m
// m can be worked out by adding 26 to enc[i] - prevStepTwo until it's greater than 97 

// Since prevStepTwo = 26n + c, where c is prevStepTwo % 26
// We can just say that 
// dec[i] = enc[i] - (prevStepTwo % 26) - 26m
// and m is just smaller

// Time complexity    O(n)
// Space complexity   O(n) can't modify in place
string decrypt( const string& word )
{
    string decrypted = "";

    int n = word.size();
    int prevStepTwo = 1;
    for (int i = 0; i < n; ++i)
    {
      int dec = word[i] - prevStepTwo;
      while (dec < 97) dec += 26;
      decrypted += dec;
      prevStepTwo += dec % 26;
    }

    return decrypted; 
}