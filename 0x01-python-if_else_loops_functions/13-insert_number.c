#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;

    new = malloc(sizeof(listint_t));
    current = *head;
    if (current == NULL)
    {
        current->n = number;
        return (current);
    }
    
    new->n = number;
    while (current->next!=NULL && current->next->n < number)
    {
        current = current->next;
    }
    new->next = current->next;
    current->next = new;
    return (current);
    
}

