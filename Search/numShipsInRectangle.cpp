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
        return helper(sea, topRight, bottomLeft);
    }

    int helper(Sea &sea, vector<int> &topRight, vector<int> &bottomLeft)
    {
        if (topRight[0] - bottomLeft[0] == 1 && topRight[1] - bottomLeft[1] == 1)
        {
            return sea.hasShips(topRight, bottomLeft); //TODO
        }
        return sea.hasShips(topRight, bottomLeft) *
                (
                countShips(sea, vector<int>{ (topRight[0] - bottomLeft[0]) / 2 , topRight[1]}, vector<int>{bottomLeft[0] ,  (topRight[1] - bottomLeft[1]) / 2 }) + 
                countShips(sea, topRight, vector<int>{(topRight[0] - bottomLeft[0]) / 2 ,  (topRight[1] - bottomLeft[1]) / 2 }) + 
                countShips(sea, vector<int>{(topRight[0] - bottomLeft[0]) / 2 ,  (topRight[1] - bottomLeft[1]) / 2 } , bottomLeft) + 
                countShips(sea, vector<int>{topRight[0], (topRight[1] - bottomLeft[1]) / 2} , vector<int>{(topRight[0] - bottomLeft[0]) / 2, bottomLeft[1]}) 
                );
    }
};

/*
Recursive
If topRight = bottom left + [1, 1] then return 
Else if hasShips for the rectangle is true call countShips({topRight[0]/2, topRight[1]}, {bottomLeft[0], topRight[1] / 2})

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
 
Say we're given a 1x1 rectangle
On a truth table 1-4 ships gives the same output
So how would we distinguish in that case?

You can seach outside of the bounds of the given rectangle
This allows you to bound the problem

Eg if in the 1x1 example you can search at -1, -1 to 0, 0 and find the ship at the origin
So how do you generalise this?
Well you need to search so you can categorically eliminate other points so that you reduce ambiguity looking at internal rectangles

But also need to kind of binary search to look macro at the whole grid

I think roughly what you want to do is binary search down to single squares
That will give you the 1x1 squares that have a least 1 ship at the vertex

If there are at least 10 of those squares you can return 10,
Each ship will result in 4 squares that are marked
But what if squares overlap
*/