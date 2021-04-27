#include "lists.h"

/**
 * check_for_cycle
 *
 * @list: pointer to list
 *
 * Return: 0 if founds a cycle, 1 if not
 */

int check_for_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	for ( ; slow && fast && fast->next; )
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
