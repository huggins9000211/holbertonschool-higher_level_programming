#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;
    listint_t *temp;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;

    if (*head == NULL)
        *head = new;
    else
    {
        int last;
        while (1)
        {
            if ((current->next)->n > number)
            {

                new->next = current;
                break;
            }
            current = current->next;
        }
             
        current->next = new;  
    }
    return (new);
}

