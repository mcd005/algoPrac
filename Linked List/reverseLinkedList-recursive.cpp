/*
Problem description: https://leetcode.com/problems/reverse-linked-list

We keep recursively calling reverseList() until we reach the end of the list
At this point we save the pointer to this node to be returned as the head of the reversed list once we are done
From here we make
	1) Each next node point to the current node
	2) Each current node point to NULL

For 2 we are basically saying "Point to nothing unless you are told otherwise"
The node is told otherwise when it has a predecessor which says "ok now point to me" (i.e. 1)
This means all the nodes will point to their predecssor, except for the last node, which will point to NULL
Thus the list is 

Time complexity		O(n) 	called n times before reaching base case
Space complexity	O(n)	recursion depth
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next){
            return head;
        }
        ListNode* node = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        
        return node;
    }
};

/*
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head){
            return nullptr;
        }
        return llReverse(nullptr, head);
    }
    
    ListNode* llReverse(ListNode* prev, ListNode* cur){
        ListNode* temp = cur->next;
        cur->next = prev;
        if (temp){
            return llReverse(cur, temp);
        }
        else{
            return cur;
        }
    }
};
*/