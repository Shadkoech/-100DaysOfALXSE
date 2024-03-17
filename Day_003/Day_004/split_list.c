#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node in the linked list
typedef struct Node {
    int value;
    struct Node* next;
} Node;

// Function to divide the linked list into two halves and return a pointer to the second half
Node* divideLinkedList(Node* list) {
    if (list == NULL || list->next == NULL) return NULL; // If the list is empty or has only one node, return NULL

    Node* slow = list;
    Node* fast = list->next;

    // Move fast pointer two steps ahead and slow pointer one step ahead
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    Node* secondHalfStart = slow->next;
    slow->next = NULL; // Break the link between the first and second halves

    return secondHalfStart;
}

// Function to print the linked list
void printLinkedList(Node* head) {
    while (head != NULL) {
        printf("%d ", head->value);
        head = head->next;
    }
    printf("\n");
}

// Main function
int main() {
    // Create the linked list
    Node* head = (Node*)malloc(sizeof(Node));
    head->value = 2;
    Node* current = head;
    for (int i = 3; i <= 20; ++i) {
        current->next = (Node*)malloc(sizeof(Node));
        current->next->value = i;
        current = current->next;
    }
    current->next = NULL;

    // Divide the linked list and print the second half
    Node* secondHalfStart = divideLinkedList(head);
    printLinkedList(secondHalfStart);

    // Free dynamically allocated memory
    while (head != NULL) {
        Node* temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
