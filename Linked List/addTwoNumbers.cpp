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
    /*
    https://leetcode.com/problems/add-two-numbers/

    This is basically a software implementation of a Ripple Carry Adder (Turing Completeness in action?)
    Each digit is summed bitwise
        If it is greater than 10 it produces a carry
        If a digit has a carry in, it adds it to it sum. This may propagate the carry.
    Either way if there are more digits to summed or the last digits produced a carry:
        Another node in the linked list will be created
        It's value will be set to the sum + Cin of the current digits
        It will be connected to the tail of the linked list that we have so far

    Time complexity         O(n) where n is the length of the longer of the two input linked lists
    Space complexity        O(n + 1)
    */
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //The pointer to the linked list to be returned
        ListNode* output = NULL;
        output = new ListNode();

        //Pointer used to traverse the linked list as we generate it
        ListNode* head = NULL;
        head = output;

        int A = 0, B = 0, sum = 0, Cin = 0, Cout = 0;

        while (l1 || l2 || Cin) {
            if (l1) {
                A = l1->val;
                l1 = l1->next;
            }
            else {
                A = 0;
            }
            if (l2) {
                B = l2->val;
                l2 = l2->next;
            }
            else {
                B = 0;
            }
            sum = (A + B + Cin) % 10;
            Cout = (A + B + Cin) / 10;

            head->val = sum;

            if (l1 || l2 || Cout) {
                ListNode* extra = NULL;
                extra = new ListNode();
                head->next = extra;
                head = head->next;
            }

            Cin = Cout;
        }

        return output;
    }
};

//Alternate Solution, but can't handle massive ints
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return linkedListify(accumulate(l1) + accumulate(l2));
    }
    
    //Helper function to convert the linked list into an int
    int accumulate(ListNode* head){
        long long int sum = 0;
        int powTen = 0;

        while (head){
            sum += head->val * pow(10, powTen);
            head = head->next;
            powTen++;
        }

        return sum;
    }
    
    ListNode* linkedListify(int num){
        //The pointer to the linked this to be returned
        ListNode* output = NULL;
        output  = new ListNode(num % 10);
        //Used to traverse the linked list as we generate it
        ListNode* head = NULL;
        head = output;
        
        while (num > 10){
            num /= 10;
            ListNode* extra = NULL;
            extra = new ListNode(num % 10);
            head->next = extra;
            head = head->next;
        }
        
        return output;
    }
    
};