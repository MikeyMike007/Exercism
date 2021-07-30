#include "isogram.h"
#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

// Global linked list. Didnt manage to solve it with defining the linked list
// locally in the is_isogram function. I guess i need to involve pointer to pointer to be
// able to solve it through that way.
node_t* head = NULL;

// The function is_isogram checks wether a phrase is an isogram.
bool is_isogram(const char phrase[]) {

    // Check if phrase is NULL or empty. In that case we return false.
    if (phrase == NULL)
        return false;

    // Loop until *phrase != '\0'.
    while (*phrase) {
        // Transform *phrase to a lower letter. Need to convert char to an
        // unsigned char since tolower takes an int.
        char letter = tolower((unsigned char)*phrase);
        // is letter in the alphabet?
        if ((letter >= 'a') && ( letter <= 'z')) {
            // if yes, look if the letter is in the linked list.
            if (search(letter) == true) {
                // if letter is in the linked list. Then there is a duplicate
                // which means that the phrase is not an isogram, whic means
                // that the function need to return false. This also means
                // that we need to free memory for the linked list. (Question:
                // is it fine to relase the header and set the header to NULL? -
                // Or do i need to free every node separetly?). 
                free(head);
                head = NULL;
                return false;
            }
            else
                // If the letter is not already in the linked list. lets insert
                // it.
                insert_node(letter);
        }
        // Loop through next character in phrase.
        phrase++;
    }
    // free memory for linked list and set the head to NULL.
    free(head);
    head = NULL;
    return true;
}

void insert_node(char letter) {
    // current_node is used to loop until the end of the linked list so we can
    // set the new node at the last position.
    node_t* current_node;
    // new node is the node we are creating.
    node_t* new_node;
    
    // allocate some memory for the new node.
    new_node = (node_t*)malloc(sizeof(node_t));

    // if the new node is null even after memory allocation, then there is
    // something wrong with memory.
    if (new_node == NULL) {
        printf("Out of memory\n");
        exit(0);
    }
    
    // set the new letter to the data variable in the new node.
    new_node->data = letter;
    // set the next node to null in the new node.
    new_node->next = NULL;

    // check if the head is empty. In this case we are inserting the first node.
    if(head == NULL) {
        // this means that the head points to the created new node.
        head = new_node;
    }
    else {
        // if the list is not empty. Loop until the last node (for which next is
        // null) and insert the new node there.
        current_node = head;
        while(current_node->next != NULL) {
            // Go forward in the list.
            current_node = current_node->next;
        }
        // insert the new node.
        current_node->next = new_node;
    }
}

bool search(char letter) {
    // check if the list is empty. in this case we return false.
    if (head == NULL) {
        return false;
    }
    else {
        // loop though the list and check whether the letter is equal to the data
        // point for each node. As soon as the letter is equal to datapoint,
        // return true.
        node_t* current_node;
        current_node = head;
        while(current_node != NULL) {
            if (letter == current_node->data)
                return true;
            current_node = current_node->next;
        }
    }
    // No match, in this case we return false.
    return false;
}
