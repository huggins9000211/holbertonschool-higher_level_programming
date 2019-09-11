#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_x *myList;
    listint_t *current;
    unsigned int n; /* number of nodes */

    myList = NULL;
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

        current = current->next;
        n++;
    }
    return (0);
}

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            new->n = number;
            new->next = current;
            current = current->next;
        current->next = new;
    }
    return (new);
}

listint_x *add_nodeList(listint_x **head, listint_t *n)
{
    listint_x *new;

    new = malloc(sizeof(listint_x));
    if (new == NULL)
        return (NULL);

    new->currentt = n;
    new->next = *head;
    *head = new;

    return (new);
}

listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}
