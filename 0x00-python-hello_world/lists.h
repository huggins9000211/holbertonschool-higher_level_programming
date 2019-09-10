#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

typedef struct listint_y
{
    listint_t *currentt;
    struct listint_y *next;
} listint_x;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

listint_x *add_nodeList(listint_x **head, listint_t *n);
void free_listList(listint_x *head);
int checkMyList(listint_x *head, listint_t *current);
#endif
