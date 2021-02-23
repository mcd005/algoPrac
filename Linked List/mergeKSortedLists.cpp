// Version 3 - Priority queue
class Compare {
public:
    //Helper funciton used to sort nodes being inserted into
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
            current->next=top;
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
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        map<int, int> counts;
        
        int n = lists.size();
        for (int i = 0; i < n; ++i){
            ListNode* p = lists[i];
            while (p){
                ++counts[p->val];
                p = p->next;
            }
        }
        
        ListNode* output = new ListNode();
        ListNode* head = output;
        for (auto el: counts){
            for (int i = 0; i < el.second; ++i){
                head->next = new ListNode(el.first);
                head = head->next;
            }
        }
        
        head = output;
        output = output->next;
        delete head;
        
        return output;
    }
};

// Version 1 - Merge each list with the next in line
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
        
        if (head2 && head2->val < head1->val){
            ListNode* to_swap = head2;
            head2 = head1;
            head1 = to_swap;
        }
        
        ListNode* merged = head1;
        while (head1->next && head2){
            if (head1->next->val <= head2->val){
                head1 = head1->next;
            }
            else {
                ListNode* tmp1 = head1->next;
                ListNode* tmp2 = head2->next;
                head1->next = head2;
                head2->next = tmp1;
                head2 = tmp2;
            }
        }
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