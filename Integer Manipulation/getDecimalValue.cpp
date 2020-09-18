class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int pos = 0;
        vector<int> bitPos; //Bit position of each 1
        while (head){
            if (head->val == 1){
                bitPos.push_back(pos);
            }
            head = head->next;
            pos++;
        }
        
        int result = 0;
        for (auto const& num : bitPos){
            result += pow(2, (pos-num-1));
        }
        return result; 
    }
};