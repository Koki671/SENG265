/** @file list.c
 *  @brief Implementation of a linked list.
 *
 * Based on the implementation approach described in "The Practice
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 *
 */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"

/**
Function: order_sort
*-------------------------------------------------------
* @brief This function sorts a linked list of nodes in descending
*order of their statistic value. If the linked list already has
*a node with the same val1 value as the new node, the existing node's 
*statistic value is incremented, and it is moved to its correct position in the list. 
*If there is no node with the same val1 value, the new node is inserted in its
*correct position in the list.
* @param head a pointer to the head of the linked list
* @param new a pointer to the node to be inserted in the list
* @return a pointer to the head of the sorted linked list
*/
node_t * order_sort(node_t* head, node_t* new)
{
    if (!head) {
        new->next = NULL;
        return new;
    }
    // pointers to traverse the list
    node_t * cur;
    node_t * prev = NULL;
    int same = 0;
    for (cur = head; cur != NULL; cur = cur->next){
		
        if (!strcmp(new->val1, cur->val1) && !same) {
            cur->statistic++;
            same = 1;

         // remove the current node from the list
            if (prev != NULL){
                 prev->next = cur->next;
            }else{ return cur; 
            }
            new = cur;
            cur = head;
			prev = NULL;
        }
 // compare the statistics of the new node and the current node to find their correct position
        if (new->statistic < cur->statistic) {
            prev = cur;
        } else if (new->statistic > cur->statistic) {
            break;
        } else if (strcmp(new->val1, cur->val1) > 0) {
            prev = cur;
        } else {
            break;
        }
    }

    // insert the new node at its correct position in the list
    new->next = cur;
    if (prev == NULL) {
        new->next = head;
        return new;
    } else {
        node_t *tmp = prev->next;
        prev->next = new;
        new->next = tmp;
        return head;
    }
}

/**
 * Function:  new_node
 * -------------------
 * @brief  Allows to dynamically allocate memory for a new node to be added to the linked list.
 *
 * This function should confirm that the argument being passed is not NULL (i.e., using the assert library). Then,
 * It dynamically allocates memory for the new node using emalloc(), and assign values to attributes associated with the node (i.e., val and next).
 *
 * @param val The value to be associated with the node.
 *
 * @return node_t* A pointer to the node created.
 *
 */
node_t *new_node(char *val)
{
    assert(val != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    temp->subject = strdup(val);
    temp->next = NULL;

    return temp;
}

/**
 * Function:  add_front
 * --------------------
 * @brief  Allows to add a node at the front of the list.
 *
 * @param list The list where the node will be added (i.e., a pointer to the first element in the list).
 * @param new The node to be added to the list.
 *
 * @return node_t* A pointer to the new head of the list.
 *
 */
node_t *add_front(node_t *list, node_t *new)
{
    new->next = list;
    return new;
}

/**
 * Function:  add_end
 * ------------------
 * @brief  Allows to add a node at the end of the list.
 *
 * @param list The list where the node will be added (i.e., a pointer to the first element in the list).
 * @param new The node to be added to the list.
 *
 * @return node_t* A pointer to the head of the list.
 *
 */
node_t *add_end(node_t *list, node_t *new)
{
    node_t *curr;

    if (list == NULL)
    {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next)
        ;
    curr->next = new;
    new->next = NULL;
    return list;
}

/**
 * Function:  add_inorder
 * ----------------------
 * @brief  Allows to add a new node to the list respecting an order.
 *
 * @param list The list where the node will be added (i.e., a pointer to the first element in the list).
 * @param new The node to be added to the list.
 *
 * @return node_t* A pointer to the node created.
 *
 */
node_t *add_inorder(node_t *list, node_t *new)
{
    node_t *prev = NULL;
    node_t *curr = NULL;

    if (list == NULL)
    {
        return new;
    }

    for (curr = list; curr != NULL; curr = curr->next)
    {
        if (strcmp(new->subject, curr->subject) > 0)
        {
            prev = curr;
        }
        else
        {
            break;
        }
    }

    new->next = curr;

    if (prev == NULL)
    {
        return (new);
    }
    else
    {
        prev->next = new;
        return list;
    }
}

/**
 * Function:  peek_front
 * ---------------------
 * @brief  Allows to get the head node of the list.
 *
 * @param list The list to get the node from.
 *
 * @return node_t* A pointer to the head of the list.
 *
 */
node_t *peek_front(node_t *list)
{
    return list;
}

/**
 * Function:  remove_front
 * -----------------------
 * @brief  Allows removing the head node of the list.
 *
 * @param list The list to remove the node from.
 *
 * @return node_t* A pointer to the head of the list.
 *
 */
node_t *remove_front(node_t *list)
{
    if (list == NULL)
    {
        return NULL;
    }

    return list->next;
}

/**
 * Function: apply
 * --------------
 * @brief  Allows to apply a function to the list.
 *
 * @param list The list (i.e., pointer to head node) where the function will be applied.
 * @param fn The pointer of the function to be applied.
 * @param arg The arguments to be applied.
 *
 */
void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for (; list != NULL; list = list->next)
    {
        (*fn)(list, arg);
    }
}