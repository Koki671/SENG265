/** @file route_manager.c
 *  @brief A small program to analyze airline routes data.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author KokiItagaki V00034442
 *
 */

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

void inccounter(node_t *p, void *arg);
void analysis(node_t *l, input* argument);
input* read_arguments(int argc, char **argv, input * arguments); 
void initial_quary(quest q_opt[]);
node_t* read_yaml(node_t * list_head, quest opt[], input * args);
node_t* slice_linkedlist(node_t * head, int num_el);
#define MAX_LINE_LEN 150

/**
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char *argv[]){
	quest q_opt[3];
	initial_quary(q_opt);
    input * inputs = (input*)malloc(sizeof(input));
    inputs = read_arguments(argc, argv, inputs);

    node_t * result_list = NULL;
    result_list = read_yaml(result_list,q_opt,inputs);

    if(inputs->question == 2){
        analysis(result_list,inputs);
    }else{
	result_list = slice_linkedlist(result_list, inputs->num_out);
	analysis(result_list,inputs);
    }

    

}


/**
*Function reads_arguments
*-------------------------------------------------------------
* @brief Reads command line arguments and stores them in the input struct.
* The input struct contains a file name, a question number, and the number of output values.
* The command line arguments must be provided in the form of "--FIELD=VALUE", where FIELD is
* one of DATA, QUESTION, or N, and VALUE is the corresponding value for that field.
* 
* @param argc The number of command line arguments.
* @param argv An array of strings which contains the command line arguments.
* @param arguments A pointer to the input struct where the values will be stored.
* 
* @return A pointer to the input struct which contains the values read from the command line arguments.
* If the number of command line arguments is not correct, the function will print out an error message
* and exit with failure status.
*/
input* read_arguments(int argc, char **argv, input * arguments){
    char field[15];
    char value[40];
    if (argc == 1 || argc > 4) {
		printf("The number of arguments is not correct\n");
        exit(EXIT_FAILURE);

    } else {
        
        int i = 1;
while (i < argc) {
   
    
    if (sscanf(argv[i], "--%9[^=]=%31[^\n]", field, value) == 2) {
        if (strcmp(field,"DATA") == 0) {
            arguments->file = strdup(value);
        } else if (strcmp(field,"QUESTION") == 0) {
            arguments->question = atoi(value);
        } else if (strcmp(field,"N") == 0) {
            arguments->num_out = atoi(value);
        }
    }
    i++;
}

		printf("\n");
		return arguments;
    }
}

/**
*Function trim
*----------------------------------------------------------------------------
*@brief Removes leading and trailing whitespace from a string.
*This function takes a string as input and returns a new string with any leading and trailing whitespace removed.
*@param str The input string to be trimmed.
*@return A new string with leading and trailing whitespace removed.
*/

char *trim(char *str)
{
    // Trim leading whitespace
    while (isspace((unsigned char)*str)) {
        str++;
    }

    if (*str == '\0') {
        // String contains only whitespace
        return str;
    }

    // Trim trailing whitespace
    char *end = str + strlen(str) - 1;
    while (end > str && isspace((unsigned char)*end)) {
        end--;
    }

    // Null-terminate the trimmed string
    *(end + 1) = '\0';

    return str;
}

/**
*Function read_yaml
*-------------------------------------------------------------------
*@brief Reads a YAML data file and populates a linked list with nodes containing the specified query fields.
*@param list_head A pointer to the head of the linked list to populate
*@param opt An array of quest struct that specifies the query fields to extract from the data file
*@param args A pointer to an input struct that specifies the YAML data file to read and the question number
*@return A pointer to the head of the populated linked list
*/
node_t* read_yaml(node_t *list_head, quest opt[], input *args) {
    // Open the data file for reading
    FILE *file = fopen(args->file, "r");
    if (file == NULL) {
        perror("Error: Cannot open the data file");
        return list_head;
    }

    // Initialize variables
    node_t *cur = NULL;
    char line[MAX_LINE_LEN];
    int q = args->question - 1;
    int count = 1;

    // Loop through each line of the file
    while (fgets(line, MAX_LINE_LEN, file) != NULL) {
        // Check if the line is a new YAML document
        if (strncmp(line, "-", 1) == 0 && count == 1) {
            // Allocate memory for a new node
            cur = malloc(sizeof(node_t));
            if (cur == NULL) {
                perror("Error cannot allocate memory for node");
                fclose(file);
                return list_head;
            }

            // Initialize the new node
            cur->statistic = 1;
            cur->next = NULL;
        }

        // Parse the line for the YAML key-value pair
        char arg_buff[3500];
        char val_buff[3500];
        if (sscanf(line, "%*c %[a-z_] : %[^\t\n]", arg_buff, val_buff) != 2) {
            continue;
        }

        // Check the YAML key against the provided query fields
        if (strcmp(opt[q].val1, arg_buff) == 0) {
            // Extract the value for the first query field
            if (val_buff[0] == '\'') {
                char *token = strtok(val_buff, "'");
                if (token != NULL) {
                    cur->val1 = strdup(trim(token));
                }
            } else {
                cur->val1 = strdup(trim(val_buff));
            }
        } else if (strcmp(opt[q].val2, arg_buff) == 0) {
            // Extract the value for the second query field
            cur->val2 = strdup(val_buff);
        } else if (strcmp(opt[q].val3, arg_buff) == 0) {
            // Extract the value for the third query field
            cur->val3 = strdup(val_buff);
        } else if (strcmp(opt[q].val4, arg_buff) == 0) {
            // Extract the value for the fourth query field
            cur->val4 = strdup(val_buff);
        }

        // Check if it's time to insert the current node into the linked list
        if (count % 13 == 0){
            if((args->question == 1 && strcmp(cur->val3, "Canada") == 0) || args->question != 1) {
                // Insert the new node into the linked list
                list_head = order_sort(list_head, cur);
            }else {
                // Free the memory for the current node
                free(cur);
            }

            // Allocate memory for a new node
            cur = malloc(sizeof(node_t));
            if (cur == NULL) {
                perror("Error allocating memory for node");
                fclose(file);
                return list_head;
            }
            cur->statistic = 1;
            cur->next = NULL;
        }
        count++;
    }
    fclose(file);
    return list_head;
}


/**
 * Function slice_linkedlist
 * ---------------------------------------------------------------
 * Slices a linked list by keeping only the first `num_elements` nodes
 * and returning a pointer to the new head node.
 *
 * @param head          Pointer to the head node of the linked list.
 * @param num_elements  Number of nodes to keep in the sliced linked list.
 * @return              Pointer to the head node of the sliced linked list.
 */
node_t* slice_linkedlist(node_t* head, int num_elements) {
    node_t* curr = head;

    for (int i = 1; i < num_elements; i++) {
        curr = curr->next;
    }

    curr->next = NULL;

    return head;
}

/**
*Function initial_quary
*-----------------------------------------------------------------------------
*@brief Initializes the array of option data for the questions.
*This function initializes the quest array with option data that specifies
*the number and names of fields based on the question the user answers.
*@param q_opt An array of quest structs to initialize with option data.
*@return void
*/

void initial_quary(quest q_opt[]) {
    // Define an array of option data to initialize the q_opt array
    const struct {
        int fields;
        char val1[40];
        char val2[40];
        char val3[40];
        char val4[40];
    }
    option_data[] = {
        {2, "airline_name", "airline_icao_unique_code", "to_airport_country", ""},
        {1, "to_airport_country", "", "", ""},
        {4, "to_airport_name", "to_airport_icao_unique_code", "to_airport_city", "to_airport_country"}
    };

    // Initialize q_opt array with the option data
    for (int i = 0; i < 3; i++) {
        q_opt[i].fields = option_data[i].fields;
        strncpy(q_opt[i].val1, option_data[i].val1, sizeof(q_opt[i].val1));
        strncpy(q_opt[i].val2, option_data[i].val2, sizeof(q_opt[i].val2));
        strncpy(q_opt[i].val3, option_data[i].val3, sizeof(q_opt[i].val3));
        strncpy(q_opt[i].val4, option_data[i].val4, sizeof(q_opt[i].val4));
    }
}


// ------------------- GIVEN LIST FUNCTIONS ----------------------
/**
 * @brief Serves as an incremental counter for navigating the list.
 *
 * @param p The pointer of the node to print.
 * @param arg The pointer of the index.
 *
 */
void inccounter(node_t *p, void *arg)
{
    int *ip = (int *)arg;
    (*ip)++;
}






/**
*Function:swap_nodes
*------------------------------------------------------
*
*@brief Swaps the values of two nodes in a linked list.
*
*@param a: a pointer to the first node to swap.
*@param b: a pointer to the second node to swap.
*@return void.
*/
void swap_nodes(node_t *a, node_t *b)
{
    int temp_statistic = a->statistic;
    char *temp_val1 = a->val1;
    char *temp_val2 = a->val2;
    char *temp_val3 = a->val3;
    char *temp_val4 = a->val4;

    a->statistic = b->statistic;
    a->val1 = b->val1;
    a->val2 = b->val2;
    a->val3 = b->val3;
    a->val4 = b->val4;

    b->statistic = temp_statistic;
    b->val1 = temp_val1;
    b->val2 = temp_val2;
    b->val3 = temp_val3;
    b->val4 = temp_val4;
}



/**
*
*Function: analysis
*----------------------------------------------------------------------------
* @brief Performs analysis on the given linked list based on the input argument and writes the results to a CSV file.
* @param l: a pointer to the head of the linked list
* @param argument: a pointer to the input struct containing information about the analysis to perform
*@return void
*/

void analysis(node_t* l, input* argument){
int swapped;
node_t *ptr1 = l;
node_t *lptr = NULL;
 FILE *fp;
node_t *p = l->prev; 
node_t *max_node = l;
node_t *cur = l->next;
 int i = 1;

 // Open the output CSV file in write mode
fp = fopen("output.csv", "w"); 
if (fp == NULL) {
    printf("Error opening output file\n");
    return;
    }
    // Write headers to the CSV file
fprintf(fp, "subject,statistic\n");

cur = l;
// Perform analysis based on question number
switch(argument->question) {
 // Case 1: Write all data in the list to the CSV file
case 1:
  while (cur != NULL) {
            fprintf(fp, "%s (%s),%d\n",
                cur->val1,
                cur->val2,
                cur->statistic
            );
            cur = cur->next;
        }
        break;


 // Case 2: Sort the list by statistic in ascending order and write the top n subjects to the CSV file
case 2:
    do {
        swapped = 0;
        while (ptr1->next != lptr) {
            if (ptr1->statistic > ptr1->next->statistic) {
                swap_nodes(ptr1, ptr1->next);
                swapped = 1;
            }
            ptr1 = ptr1->next;
        }
        lptr = ptr1;
        ptr1 = l;
        }
    while (swapped);
        if (l != NULL && i <= argument->num_out) {
            fprintf(fp, "%s,%d\n",l->val1,l->statistic);
            i++;
        }
    p = l->next;
    while (p != NULL && i <= argument->num_out) {
        if (p->val1[0] != ',') {
            fprintf(fp, "%s,%d\n",p->val1,p->statistic);
            i++;
        }
    p = p->next;
}
    break;


// Case 3: Find the node with the highest statistic, sort the list by statistic in descending order, and write the top n subjects to the CSV file
    case 3:
    // Find the node with the highest statistic
    while (cur != NULL) {
        if (cur->statistic > max_node->statistic) {
            max_node = cur;
        }
        cur = cur->next;
    }

    // Sort the list in descending order based on statistic
    node_t *new_list = NULL;
    node_t *temp;
    while (l != NULL) {
        temp = l;
        l = l->next;

        if (new_list == NULL || temp->statistic > new_list->statistic) {
            temp->next = new_list;
            new_list = temp;
        } else {
            node_t *cur = new_list;
            while (cur->next != NULL && temp->statistic < cur->next->statistic) {
                cur = cur->next;
            }
            temp->next = cur->next;
            cur->next = temp;
        }
    }

    node_t *p = new_list;
    int count = 0;
    while (p != NULL && count < argument->num_out) {
        fprintf(fp,"\"%s (%s), %s, %s\",%d\n",p->val1, p->val2,p->val3,p->val4,p->statistic);
        p = p->next;
        count++;
    }

    // Free the memory allocated for the new list
    cur = new_list;
    while (cur != NULL) {
        temp = cur->next;
        free(cur);
        cur = temp;
    }
    break;
    }
}

