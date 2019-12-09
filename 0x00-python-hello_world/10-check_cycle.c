#include "lists.h"

int check_cycle(listint_t *list)
{
    if (list == NULL)
    {
        return (0);
    }
    
    listint_t *slow = list;
    listint_t *fast = list->next;
    if (slow->next == NULL)
    {
        return (0);
    }
    while (slow)
    {
        if (slow == fast)
        {
            return (1);
        }
        slow = slow->next;
        fast = fast->next;
        if (fast)
        {
            fast = fast->next;
        }
        else
        {
            fast = list;
        }
        
    }
    return (0);
    
}
