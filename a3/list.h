/** @file listy.h
 *  @brief Function prototypes for the linked list.
 */
#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_

#define MAX_WORD_LEN 50



/**
 * @brief A struct which shows nodes in a linked list
 */
typedef struct node_t{
    char *val1;
    char *val2;
    char *val3;
    char *val4;
    char *subject;
    int statistic;
    struct node_t *next;
    struct node_t *prev;
}node_t;

/*
* @brief A struct that shows the inputs from the console 
*/
typedef struct input{
    char* file;
    int question;
    int num_out;
}input;

/*
* @brief A structure that represents the necessary input fields
* for a given question
*/
typedef struct quest{
	int fields;
	char val1[40];
	char val2[40];
	char val3[40];
	char val4[40];
}quest;

/**
 * Function protypes associated with a linked list.
 */
node_t * order_sort(node_t* head,node_t* new);
node_t *new_node(char *val);
node_t *add_front(node_t *, node_t *);
node_t *add_end(node_t *, node_t *);
node_t *add_inorder(node_t *, node_t *);
node_t *peek_front(node_t *);
node_t *remove_front(node_t *);
void apply(node_t *, void (*fn)(node_t *, void *), void *arg);

#endif