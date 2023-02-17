/** @file route_manager.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process airline routes.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author Koki Itagaki
 *
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define BUFSIZE 1024
#define MAX_LINE_LEN 2000
#define NUM_COLUMNS 13
FILE *open_file(char*);
 FILE *create_file(char*);
 void printflight();






/**
 * open_file - function that opens a file
 * @param {filename} name of the file to be opened
 *
 * @return:return a pointer to the file(FILE*)
 *         or if an error happened while opening the file, return NULL
 * 
 * This function opens the file for reading. If I cannot open the file, the program 
 * prints the error message and terminate the program quickly
 */
FILE* open_file(char* filename) { 
    FILE *ifp = fopen(filename, "r");
    if (ifp == NULL) {
       printf("Error opening file!\n");
       exit(EXIT_FAILURE);
  
      
    }return  ifp;
    }



/**
 * create_file - function that reates a file with the specified name
 *This function opens a file to write and create if it does not exist. 
 * If I cannot open the file, it prints the error message and terminate the program
 * 
 * @param  {filename}  The name of the file to be created
 *
 * @return     Return a pointer to the created file(FILE*)
 *             or return NUlL if an error happened while opening the file
 */
  FILE* create_file(char* filename){

  // Open file for writing
  
  FILE* ofp = fopen(filename, "w+");
  

  // Check if the file was successfully opened
  if (ofp == NULL) {
    printf("Error creating file!\n");
    exit(EXIT_FAILURE);
  }
  return ofp;
    }
/**
 * read_data - reads data from command line arguments and stores it in the provided variables.
 * The function takes the number of command line arguments and the array of command line arguments as inputs. 
 * Then it reads and stores the values of data, airline, source country, source city, destination city, and 
 * destination country based on the number of arguments. The values are stored in the variables passed as parameters.
 * 
 * @argc: number of command line arguments.
 * @argv: array of command line arguments.
 * @data: variable to store data argument.
 * @airline: variable to store airline argument.
 * @srcCountry: variable to store source country argument.
 * @srcCity: variable to store source city argument.
 * @destCity: variable to store destination city argument.
 * @destCountry: variable to store destination country argument.
 * 
 * @return nothing
 
 */ 
 void read_data(int argc, char *argv[], char *data, char *airline, char *srcCountry, char *srcCity, char *destCity, char *destCountry) {
   switch(argc){

    case 4:
      sscanf(argv[1], "--DATA=%[^\n]", data);
      sscanf(argv[2], "--AIRLINE=%[^\n]", airline);
      sscanf(argv[3], "--DEST_COUNTRY=%[^\n]", destCountry);
      break;
    
    case 5:
      sscanf(argv[1], "--DATA=%[^\n]", data);
      sscanf(argv[2], "--SRC_COUNTRY=%[^\n]", srcCountry);
      sscanf(argv[3], "--DEST_CITY=%[^\n]", destCity);
      sscanf(argv[4], "--DEST_COUNTRY= %[^\n]", destCountry);
     break;

   case 6:
      sscanf(argv[1], "--DATA=%[^\n]", data);
      sscanf(argv[2], "--SRC_CITY=%[^\n]", srcCity);
      sscanf(argv[3], "--SRC_COUNTRY=%[^\n]", srcCountry);
      sscanf(argv[4], "--DEST_CITY=%[^\n]", destCity);
      sscanf(argv[5], "--DEST_COUNTRY=%[^\n]", destCountry);
     break;
     
   }
 
 }
 
/**
 * Function: main
 * --------------
 *
 * @brief The main function and entry point of the program. This main program works to get a route of the airplane
 * depends on What a user put into the command line
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */


int main(int argc, char *argv[]){

    char data[MAX_LINE_LEN], airline[MAX_LINE_LEN], srcCountry[MAX_LINE_LEN],srcCity[MAX_LINE_LEN],destCity[MAX_LINE_LEN],destCountry[MAX_LINE_LEN];
    
    read_data(argc, argv, data, airline, srcCountry, srcCity, destCity, destCountry);
    FILE* ifp = open_file("airline-routes-data.csv");
    FILE* ofp = create_file("output.txt");
    printflight(airline, srcCountry, srcCity, destCountry, destCity, argc, ifp, ofp);
    fclose(ofp);
    fclose(ifp);
    return 0;
    } 
 
/**
 *This printflight function split the data into 13 columns by connma:",".
 After that, divide the cases into 3 depends on how many arguments I get and write the sentences to the file called ifp.
 *
 * @param  argc         The number of command line arguments.
 * @param  argv         The command line arguments.
 * @param  data         The data information.
 * @param  airline      The airline information.
 * @param  srcCountry   The source country information.
 * @param  srcCity      The source city information.
 * @param  destCity     The destination city information.
 * @param  destCountry  The destination country information.
 */
void printflight(char *airline, char *srcCountry, char *srcCity, char *destCountry, char *destCity, int argc, FILE *ifp, FILE *ofp){
   
    char buf[BUFSIZE];
    char *element;
    char *elements[NUM_COLUMNS];
    int counter = 0;
    int headercounter = 0;
    while(fgets(buf, BUFSIZE, ifp) != NULL) {

        element = strtok(buf, ",");
        for (int i = 0; i < NUM_COLUMNS; i++) {
            elements[i] = element;
            element = strtok(NULL, ",");
        }
   

      switch(argc){
          
        case 4:
            if ((elements[1] != NULL) && (elements[10] != NULL)){
              if ((strcmp(elements[1],airline) == 0) && (strcmp(elements[10], destCountry) == 0) && headercounter == 0 ) {
                fprintf(ofp,"FLIGHTS TO %s BY %s (%s):\n",destCountry,elements[0], airline);
                fprintf(ofp,"FROM: %s, %s, %s TO: %s (%s), %s\n",elements[6],elements[4],elements[5],elements[8],elements[11],elements[9]);
                headercounter++;
                counter ++;
                 }
              else if ((strcmp(elements[1],airline) == 0) && (strcmp(elements[10], destCountry) == 0) && headercounter != 0) {
                
                fprintf(ofp, "FROM: %s, %s, %s TO: %s (%s), %s\n",elements[6],elements[4],elements[5],elements[8],elements[11],elements[9]);
                
                counter ++; 
              }
            }
              break;
              
            
        case 5:
            if((elements[5] != NULL) && (elements[9] != NULL) && (elements[10] != NULL)){
               

              if((strcmp(elements[5],srcCountry) == 0) && (strcmp(elements[9], destCity) == 0) && (strcmp(elements[10], destCountry) == 0 && headercounter == 0)){
              fprintf(ofp,"FLIGHTS FROM %s TO %s, %s:\n",srcCountry,destCity, destCountry);
              fprintf(ofp,"AIRLINE: %s (%s) ORIGIN: %s (%s), %s\n",elements[0],elements[1],elements[3],elements[6],elements[4]);
              counter++;
              headercounter++;
             
              
            } else if((strcmp(elements[5],srcCountry) == 0) && (strcmp(elements[9], destCity) == 0)&& (strcmp(elements[10], destCountry) == 0) && headercounter != 0){
              fprintf(ofp,"AIRLINE: %s (%s) ORIGIN: %s (%s), %s\n",elements[0],elements[1],elements[3],elements[6],elements[4]);
              counter++;
          }
            }
           break;


        case 6:
           if((elements[4] != NULL) && (elements[5] != NULL) && (elements[9] != NULL)&& (elements[10] != NULL)){
            
              if((strcmp(elements[4],srcCity) == 0) && (strcmp(elements[5], srcCountry) == 0)&&(strcmp(elements[9],destCity) == 0) && (strcmp(elements[10], destCountry) == 0 && headercounter == 0)){
              fprintf(ofp,"FLIGHTS FROM %s, %s TO %s, %s:\n",srcCity,srcCountry, destCity,destCountry);
              fprintf(ofp,"AIRLINE: %s (%s) ROUTE: %s-%s\n",elements[0],elements[1],elements[6],elements[11]);
              counter++;
              headercounter++;
            
              }else if((strcmp(elements[4],srcCity) == 0) && (strcmp(elements[5], srcCountry) == 0)&&(strcmp(elements[9],destCity) == 0) && (strcmp(elements[10], destCountry) == 0 && headercounter!= 0)){
              fprintf(ofp,"AIRLINE: %s (%s) ROUTE: %s-%s\n",elements[0],elements[1],elements[6],elements[11]);
              counter++;
              }      
           }
               break;
        }
      }
       if(counter == 0){
        fprintf(ofp, "NO RESULTS FOUND.");
    }
<<<<<<< HEAD
}
=======
  }
  
>>>>>>> 627345ce7f0b82419a260a6d8385c522168f7a4d
