// https://leetcode.com/problems/middle-of-the-linked-list/

// Version 2 
// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        // With these we can check if we are at the end for both odd and even length lists
        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};

// Version 2 - use a flag to determine if slow should be moved
// Runs slower (needs 2x the iterations) but is just to show a different approach
// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        bool moveSlow = true;
        while (fast->next){
            if (moveSlow) slow = slow->next;
            fast = fast->next;
            moveSlow = !moveSlow;
        }
        
        return slow;
    }
};