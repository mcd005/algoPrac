// https://leetcode.com/problems/find-median-from-data-stream/
// Version 1 - Two priority queues
// Time complexity      O(nlogn)
// Space complexity     O(n)
// For n addNum operations
class MedianFinder {
private:
    // Two priority queues:
    // One whose top is the greatest element in the bottom half of a sorted array that contains all elements so far
    // The other whose top is the smallest element in the top half of the sorted array that contains all elements so far
    // Where the halfway point is where the median resides
    std::priority_queue<int, vector<int>, less<int>> leftHalf;
    std::priority_queue<int, vector<int>, greater<int>> rightHalf;
    
    void rebalanceQs(std::priority_queue<int, vector<int>, less<int>>& queue1, 
                     std::priority_queue<int, vector<int>, greater<int>>& queue2)
    {
        int q1Size = queue1.size(), q2Size = queue2.size();
        if (q1Size == q2Size) return;
        else if (q1Size >= q2Size + 2)
        {
            queue2.push(queue1.top());
            queue1.pop();
        }
        else if (q2Size >= q1Size + 2)
        {
            queue1.push(queue2.top());
            queue2.pop();
        }
        else return;
    }
    
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        // When an element comes in, if it is smaller than the bigggest in left half insert it in left,
        // otherwise insert in right
        if (!leftHalf.empty() && leftHalf.top() > num)
        {
            leftHalf.push(num);
        }
        else 
        {
            rightHalf.push(num);
        }
        // If this causes a size discrepancy of greater than 2 
        // between the queues move the top of the bigger to the top of other
        // Ci
        rebalanceQs(leftHalf, rightHalf);
    }
    
    double findMedian() {
        // If the queues are the same size we return the mean of the two tops
        if (leftHalf.size() == rightHalf.size())
        {
            return (leftHalf.top() + rightHalf.top()) / 2.0;
        }
        // Otherwise we return the top of the bigger queue
        else if (leftHalf.size() == rightHalf.size() + 1)
        {
            return leftHalf.top();
        }
        else return rightHalf.top();
    }
};


/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */