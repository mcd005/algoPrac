 /*
Problem description: https://leetcode.com/problems/reverse-linked-list/
 
For each node we save the next node as a temporary variable
Then we have the current node point to the previous node, which was saved from the last iteration
	(In the case of the first node the previous node is null)
Once the direction of the current nodes pointer has been reversed
	We make the current node the previous node
	And we make the next node (saved in temp) the current node
 This continues until the end of the list, when we return the poitner of the tail, which is now the head of the reversed linked list
 
 Time complexity		O(n)
 Space complexity		O(1)
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
        ListNode* prev = NULL;
        
        while (head){
            ListNode* temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        
        return prev;
    }
};