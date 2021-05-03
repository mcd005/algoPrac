// Version 2 - Segment Tree
// You can increment the entire arrary by the root of the seg tree
// You can increment the entire left half by the left child of the root and vice versa with the right
// So for each level you increase the number of required increments by the difference between node and it's parents value
// However this doesn't work for  1 2 3 2 1
// if there are an odd number of elements you may have to do a range query that bridges the two halves 
class SegmentTree
{
public:
    SegmentTree(vector<int> &inputArr)
    {
        int n = inputArr.size();
        segTreeArr.resize(calculateSegTreeSize(n), INT_MAX);
        constructTree(inputArr, 0, n - 1, 0);
    }

    void print()
    {
        for (auto el: segTreeArr)
        {
            cout << el << endl;
        }
    }
    
private:
    int calculateSegTreeSize(int inputArrSize)
    {
        inputArrSize--;
        inputArrSize |= inputArrSize >> 1;
        inputArrSize |= inputArrSize >> 2;
        inputArrSize |= inputArrSize >> 4;
        inputArrSize |= inputArrSize >> 8;
        inputArrSize |= inputArrSize >> 16;
        inputArrSize++;
        return inputArrSize * 2 - 1;
    }

    void constructTree(vector<int> &inputArr, int low, int high, int pos)
    {
        if (low == high)
        {
            segTreeArr[pos] = inputArr[low];
            return;
        }
        int mid = (low + high) / 2;
        constructTree(inputArr, low, mid, 2*pos + 1);
        constructTree(inputArr, mid + 1, high, 2*pos + 2);
        segTreeArr[pos] = min(segTreeArr[2*pos + 1], segTreeArr[2*pos + 2]);
    }

    vector<int> segTreeArr;
};

class Solution
{
public:
    int minNumberOperations(vector<int> &target)
    {
        auto segTree = SegmentTree(target);
        segTree.print();
        return 10000;
    }
};

/* 
Implement a segment tree class
    Needs to construct a segment tree given an array and return a node
        Firstly iterate over the arr, turn each element into a node, and put it in the q
        Create an empty node
        Then while there is stuff in the q
            If the empty node has no left add the front of the queue to it's left
            Else if it has no right
    Needs a node struct with memebers
        a value (the min of it's children)
        a start and end
        a left and right
    Needs to be able to search given that root node and a range



Solution is going to be very similiar to stonewall or city skylines right?
    Yes. There what you did was ask: is there already a stone of a smaller height on top of which this can be stacked
    You started out by assuming that every element needed a stone, and then you could subtract stones as you found some could stack
    However it's possible that solution was a greedy one

Stonewall algo
    Put the first element on the stack
    If the next is bigger also put it on the stack

Slices algo
    You start an ask: how many are of height one? and that will give you some number of contigous slices
    The number of contigous slices is the number of increments required
    So the question is how do you get a contigous slice in constant time



How would you do it brute force?
    Walk thorough an ask, does this element need 

It depends on how many local maxima there are.

Also depends of the troughs though

If there is 1 or less then you only need to increment a number of times equal to the value of the maximum

If there are 2 peaks


[0,0,0,0,0]
[1,1,1,1,1]
[1,2,2,2,1]
[1,2,3,2,1]

(initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).

(initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).

[3,1,5,4,2]
 |

stack = 1 2 
incs = 3 + 4 + 3 + 2 + 1 = 13

[0,0,0,0] -> [1,1,1,1]
 
*/