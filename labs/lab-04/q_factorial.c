/** @file q_array_rotate.c
 *  @brief Submission program for Lab 04.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author STUDENT_NAME
 *
 */
#include <stdio.h>
#include <stdlib.h>

/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char *argv[])
{/** @file q_array_rotate.c
 *  @brief Submission program for Lab 04.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author STUDENT_NAME
 *
 */
#include <stdio.h>
#include <stdlib.h>




int main(int argc, char *argv[])
{

        // variable to store the final answer
        int factorial = 1;
        if (argc != 2) {
        printf("Error: Please provide a single integer as input.\n");
        return 1;
    }
    int num = atoi(argv[1]);
    if (num < 0) {
        printf("Error: Please provide a non-negative integer.\n");
        return 1;
    }
        for (int i = 1; i <= num; i++) {
        factorial *= i;
    }

    printf("%d\n", factorial);
    return 0;

}
}
