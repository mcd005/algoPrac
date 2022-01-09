/*
FROM PRAMP:

Sentence Reverse
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
*/

// Version 1 - Reverse the whole array
// Word will be mirrored so check each word in turn
// and reverse it again so it is the right way round
// Time complexity      O(n)
// Space complexity     O(1) not including input arr
#include <iostream>
#include <vector>

using namespace std;

vector<char> reverseWords( const vector<char>& arr ) 
{
  vector<char> result(arr);
  int i = 0;
  int n = arr.size();
  
  std::reverse(result.begin(), result.end());
  
  int wordStart = 0;
  i = 0;
  while (i < n)
  {
    if (result[i] == ' ')
    {
      std::reverse(result.begin() + wordStart, result.begin() + i);
      wordStart = i + 1;
    }
    ++i;
  }
  std::reverse(result.begin() + wordStart, result.begin() + i);
  
  return result;
}

// This is here in case we can't use built in reverse
void customReverse(vector<char>& array, int n)
{
    while (i < n - 1 - i)
    {
        char temp = result[i];
        result[i] = result[n - 1 - i]);
        result[n - 1 - i] = temp;
        ++i;
    }
}
