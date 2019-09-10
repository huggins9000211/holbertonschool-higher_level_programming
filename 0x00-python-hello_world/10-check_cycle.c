#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_x *myList;
    listint_t *current;
    unsigned int n; /* number of nodes */

    current = list;
    n = 0;
    while (current != NULL)
    {
        if (n == 0)
        {
            add_nodeList(&myList, current);
        }
        else if (checkMyList(myList, current))
        {
            return (1);
        }

        //printf("%i\n", current->currentt);
        current = current->next;
        n++;
    }
    return (0);
}

int checkMyList(listint_x *head, listint_t *current)
{
    const listint_t *currentz;
    const listint_x *myList;
    myList = head;
    currentz = current;

    while (myList != NULL)
    {
        if (currentz == myList->currentt) {
            return (1);
        }

        myList = myList->next;
    }
    return (0);
    
}