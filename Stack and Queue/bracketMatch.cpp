/*
FROM PRAMP

A string of brackets is considered correctly matched if 
every opening bracket in the string can be paired up with a later closing bracket, and vice versa. 
For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. 
For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, 
write a function bracketMatch that takes a bracket string as an input 
and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched. 
*/

#include <iostream>
#include <string>
#include <stack>

using namespace std;

// Time     O(n)
// Space    O(1)
int bracketMatch( const string& text ) 
{
  int open = 0, mismatch = 0;
  for (auto b: text)
  {
    if (b == ')')
    {
      if (open == 0) ++mismatch;
      else --open;
    }
    else ++open;
  }
  return mismatch + open;
}

// MY PROMPTS AS INTERVIEWER:
// What is required for a valid string? Number of
// Is there a data structure you think you could use here?

// If you adapt the stack analogy, at any given time you will have:
//      1) close brackets that will never be matched
//      2) open brackets waiting to be matched
// So rather than using a linear amount of memory to store this info
// We can use two counters and const memory

// The way pramp suggest you do it is that you "fix" the string as you go
// Imagine what we are instead doing is fixing the string + counting the number of insertions we make