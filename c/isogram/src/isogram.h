#ifndef ISOGRAM_H
#define ISOGRAM_H

#include <stdbool.h>
#include <stdlib.h>

typedef struct node {
    char data;
    struct node* next;
} node_t;


bool is_isogram(const char phrase[]);
void insert_node(char letter);
bool search(char letter);


#endif
