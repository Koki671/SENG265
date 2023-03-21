typedef int Key;
typedef struct {
    Key k;
    int i;
} Item;
typedef Item* ItemRef;
typedef struct NodeStruct* NodeRef;
typedef struct NodeStruct {
    ItemRef item;
    NodeRef next;
    NodeRef prev;
} Node;
typedef struct {
    NodeRef head;
    NodeRef tail;
    int size;
} DList;
typedef DList* DListRef;
void printListFW(DListRef);

void printListFW(DListRef dlr) {
    NodeRef xp = dlr->head;
    while (xp != NULL) {
        printf("%d ", xp->item->k);
        xp = xp->next;
    } //while
    printf("\n");
} //printListFW