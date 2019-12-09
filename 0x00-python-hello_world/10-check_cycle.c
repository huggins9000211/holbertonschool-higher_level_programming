#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;
    if (list == NULL)
    {
        return (0);
    }
    if (slow->next == NULL)
    {
        return (0);
    }
    while (slow)
    {
        
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
        if (slow == fast)
        {
            return (1);
        }
        
    }
    return (0);
    
}
