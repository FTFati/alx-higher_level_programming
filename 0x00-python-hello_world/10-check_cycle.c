#include "lists.h"

/**
 * check_cycle - check for loop in Linked list
 * @list: head of linked list
 * Return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *List1, *List2;

	if (list == NULL || list->next == NULL)
		return (0);
	List1 = list;
	List2 = List1->next;

	while (List1 != NULL && List2->next != NULL
		&& List2->next->next != NULL)
	{
		if (List1 == List2)
			return (1);
		List1 = List1->next;
		List2 = List2->next->next;
	}
	return (0);
}
