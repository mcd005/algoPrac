/*
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

Standard linked list problem with edge case of insertion at head accounted for

Time complexity 	O(n) where n is position at which the node will be insered
Space complexity 	O(1) not including the space currently occupied by the linked list
*/

SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* head, int data, int position) {

    SinglyLinkedListNode* insert = new SinglyLinkedListNode(data); //Create new node to be inserted

    if (position == 0){
        insert->next = head;
        return insert;
    }

    SinglyLinkedListNode* output = head; //Save the pointer to the head so it can be output

    for (int i = 0;  i < position - 1; i++){ //iterate to the node before the insertion point
        head = head->next;
    }

    SinglyLinkedListNode* temp = head->next;

    head->next = insert;
    insert->next = temp;

    return output;
}