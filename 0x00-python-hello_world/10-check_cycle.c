#include "lists.h"

/**
 * check_cycle - chick if the list is a cycle
 * @list: a pointer to the list
 * Return: 1 if cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *vit = list, *lent = list;

	while (vit != NULL && vit->next)
	{
		lent = lent->next;
		vit = vit->next->next;
		if (lent == vit)
			return (1);
	}
	return (0);
}
