/**
 * // This is Sea's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Sea {
 *   public:
 *     bool hasShips(vector<int> topRight, vector<int> bottomLeft);
 * };
 */

class Solution
{
public:
    int countShips(Sea sea, vector<int> topRight, vector<int> bottomLeft)
    {
    }
};

/*
We're given a rectangle and we have to determine the number of ships inside it
We have a function with which we tells us if there is at least one ship within a specified rectangle

Say we have a rectangles like this:

*-----0
|     |     
|     |
|     |
*-----*

0-----0
|     |     
|     |
|     |
0-----0

How do we distinguish them from each other? For a 1x1 rectangle it is impossible to distinguish
Is it possible for a 1x2?
How about for a 2x2?
Was going to say that if there are 4 adjacent squares that are true then the point at their centre must contain a ship
However, it may be the case that we are looking a back to back ships

I'm imaging there will be some kind of truth table that will hopefully reveal the number
*/