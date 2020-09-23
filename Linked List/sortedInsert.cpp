/*
https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/

Traverse the list until:
	You either find a value that is bigger than the data to be inserted, at which point an insertion happens
		If this value is at the head then insert the node and make it the new head
	Or you reach the end of the list, and attach the new node on to the end

Time complexity 	O(n)
Space complexity	O(1)
*/

DoublyLinkedListNode* sortedInsert(DoublyLinkedListNode* head, int data) {
    DoublyLinkedListNode* output = head;

    DoublyLinkedListNode* insert = new DoublyLinkedListNode(data);

    while ((data > head->data) && (head->next)){
            head = head->next;
    }
    
    if (!head->prev){
        insert->prev = nullptr;
        insert->next = head;
        output = insert;
    }
    else if (data <= head->data){
        insert->prev = head->prev;
        head->prev->next = insert;
        head->prev = insert;
        insert->next = head;
    }
    else if (!head->next){
        head->next = insert;
        insert->prev = head;
    }
    
    return output;
}