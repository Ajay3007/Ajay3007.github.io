#include<bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node* next;
    Node() : val(0), next(nullptr) {}
    Node(int x) : val(x), next(nullptr) {}
    Node(int x, Node* nextNode) : val(x), next(nextNode) {}
};

void printList(Node* head) {
    Node* temp = head;
    while(temp != nullptr) {
        cout<<temp->val<<" ";
        temp = temp->next;
    }
}

Node* insertAtHead(Node* head, int data) {
    Node* newNode = new Node(data);
    // Node* newNode = new Node(data, head);
    newNode->next = head;
    return newNode;
}

Node* insertAtEnd(Node* head, int data) {
    Node* newNode = new Node(data);
    if(!head) return newNode;
    Node* temp = head;
    while(temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
    return head;
}

Node* insertInMiddle(Node* head, int data) {
    Node* newNode = new Node(data);
    Node* slow = nullptr;
    Node* fast = head;
    while(fast != nullptr && fast->next != nullptr) {
        slow = (slow == nullptr) ? head : slow->next;
        fast = fast->next->next;
    }
    newNode->next = slow->next;
    slow->next = newNode;
    return head;
}

Node* insertAtPosition(Node* head, int pos, int data) {
    if(pos == 1) return insertAtHead(head, data);
    
    Node* newNode = new Node(data);
    Node* curr = head;
    while(curr != nullptr && pos > 2) {
        curr = curr->next;
        pos--;
    }
    if(!curr) return head; // Invalid position
    newNode->next = curr->next;
    curr->next = newNode;
    return head;
}

Node* deleteHead(Node* head) {
    if(!head) return nullptr;
    Node *temp = head;
    head = head->next;
    delete(temp);
    return head;
}

Node* deleteByValue(Node* head, int value) {
    if(!head) return nullptr;
    Node* cur = head;
    Node* pre = nullptr;
    while(cur != nullptr) {
        if(cur->val == value) break;
        pre = cur;
        cur = cur->next;
    }
    if(cur == nullptr) return head;
    if(cur == head) return deleteHead(cur);
    pre->next = cur->next;
    delete(cur);
    return head;
}

Node* deleteAtPosition(Node* head, int pos) {
    if(!head) return nullptr;
    if(pos == 1) return deleteHead(head);
    Node* curr = head;
    while(curr != nullptr && pos > 2) {
        curr = curr->next;
        pos--;
    }
    if(curr == nullptr) return head;
    Node* temp = curr->next;
    curr->next = temp->next;
    delete(temp);
    return head;
}

int main() {
    // node4->node3->node2->node1->NULL
    Node* node1 = new Node(3);
    Node* node2 = new Node(5, node1);
    Node* node3 = new Node(9, node2);
    Node* head = new Node(4, node3);
    Node* temp = head;
    cout<<"Original LL \t: ";
    printList(head);
    
    cout<<endl<<"Insert HEAD \t: ";
    head = insertAtHead(head, 8);
    printList(head);
    
    cout<<endl<<"Insert END \t: ";
    insertAtEnd(head, 11);
    printList(head);
    
    cout<<endl<<"Insert MIDDLE \t: ";
    insertInMiddle(head, 6);
    printList(head);
    
    cout<<endl<<"Insert AT POS \t: ";
    head = insertAtPosition(head, 5, 7); // pos = 1-indexed
    printList(head);
    
    cout<<endl<<"Delete HEAD \t: ";
    head = deleteHead(head);
    printList(head);
    
    cout<<endl<<"Delete VALUE \t: ";
    head = deleteByValue(head, 3);
    printList(head);
    
    cout<<endl<<"Delete AT POS \t: ";
    head = deleteAtPosition(head, 4); // pos = 1-indexed
    printList(head);
    
}