// https://leetcode.com/problems/merge-k-sorted-lists/
// TODO Time complexities not quite right here
// Version 3 - Priority queue
// Time complexity      O(nlogn + nmlogn)
// Space complexity     O(n*m)
// Fastest solution in ms
class Compare {
public:
    // Helper funciton used to sort nodes being inserted into
    // the priority queue
    bool operator() (ListNode* a, ListNode* b) {
        return a->val >= b->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Build a sorted q of vectors of nodes
        std::priority_queue<ListNode*, std::vector<ListNode*>, Compare> pq;
        for (ListNode* list : lists) {
            if (list != nullptr) {
                pq.push(list);
            }
        }

        // Dummy head which we will discard at the end
        // this is because we can't start with a real head and discard
        // the tail
        ListNode dummy_head;
        ListNode* current = &dummy_head;
        while (!pq.empty()) {
            ListNode* top = pq.top();
            current->next = top;
            pq.pop();
            // If there are nodes left over from the list we just
            // have just grabbed from, put those nodes back in the q
            if (top->next != nullptr) {
                pq.push(top->next);
            }
            current = current->next;
            
        }
        return dummy_head.next;
    }
};

// Version 2 - Count sort
// Time complexity      O(n*m)
// Space complexity     O(n*m)
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        unordered_map<int, int> counts;
        
        int n = lists.size();
        for (int i = 0; i < n; ++i){
            // Iterate through all nodes in each list
            // counting values
            ListNode* p = lists[i];
            while (p){
                ++counts[p->val];
                p = p->next;
            }
        }
        
        // Create a dummy head
        ListNode* output = new ListNode();
        ListNode* head = output;
        // Iterate through our count sort array and construct the
        // merged list
        for (auto el: counts){
            for (int i = 0; i < el.second; ++i){
                head->next = new ListNode(el.first);
                head = head->next;
            }
        }
        
        // Move our head pointer back to dummy head
        head = output;
        // Advance it to the first node (i.e. non-dummy heady)
        output = output->next;
        // Get rid of dummy head
        delete head;
        
        return output;
    }
};

// Version 1 - Merge each list with the next in line
// Bit slow though because we double check nodes and insert
// only one node at a time. Need some sorting
// Time complexity      O(n*m)
// Space complexity     O(1)
// For n lists of m nodes
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        if (n == 0) return NULL;
        
        ListNode* output = lists[0];
        
        for (int i = 1; i < n; ++i){
            output = merge(output, lists[i]);
        }
        
        return output;
    }
    
    ListNode* merge(ListNode* head1, ListNode* head2){
        if (!head1) return head2;
        
        // We do this so we can assume from this point that the 
        // head has list 1 always has a lower value than the head of list 2
        if (head2 && head2->val < head1->val){
            ListNode* to_swap = head2;
            head2 = head1;
            head1 = to_swap;
        }
        
        // The new list 1 will be the list we merge into
        ListNode* merged = head1;
        while (head1->next && head2){
            // Iterate through list1 until head2's value is less than
            // head1's neighbour (i.e. until we know we need to insert)
            if (head1->next->val <= head2->val){
                head1 = head1->next;
            }
            // Once we find such a node
            else {
                ListNode* tmp1 = head1->next;
                ListNode* tmp2 = head2->next;
                // Insert it into list1
                head1->next = head2;
                // Reattach the severed suffix of list 1
                head2->next = tmp1;
                // Move head2 along
                head2 = tmp2;
            }
        }
        // If there are nodes of list2 left over attach them
        if (!head1->next) head1->next = head2;
        
        return merged;
    }
};
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