// https://leetcode.com/problems/remove-linked-list-elements/



// Version 2 - recursive
// Imagine the nodes are a line of people who are told anyone with the value is val has to leave the line.

// Given this news each node turns around to it's next node and says:
// "Who am I going to be stood in front of now?"

// In response, the next node is says to it's previous node: 
// "Ok let me check my value: If it's equal to val then you will stood in front of the guy after me, otherwise you'll be stood in front of me"

// This is all apart from the guy at the back of the line, who upon turning around to ask who he'll be stood in front of
// realises there is no-one there, so as before he'll be standing in front of no-one (if he remains in the line at all)
//
// Time complexity      O(n)
// Space complexity     O(n)
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (!head) return head;
        head->next = removeElements(head->next, val);
        return (head->val == val) ? head->next : head;
    }
};

// Version 1 - iterative
// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* output = head;
        
        ListNode* prev = NULL;
        
        while (head){
            if (head->val == val){
                if (prev){
                    prev->next = head->next;
                }
                else{
                    output = head->next;
                }
            }
            else{
                prev = head;
            }
            head = head->next;
        }
        
        return output;
    }
};