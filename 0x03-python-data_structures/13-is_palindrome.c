#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - hecks if a singly linked list is a palindrome.
 * @head: pointer to the fisrt element
 * Return:0 if it is not a palindrome, 1 if it is
*/
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
	return (1);
return (pal(head, *head));
}

/**
 * pal - know if it is pal
 * @head: the pointer to adrss of first in list
 * @fin: la fin de la liste
*/

int pal(listint_t **head, listint_t *fin)
{
if (fin == NULL)
	return (1);
if (pal(head, fin->next) && (*head)->n == fin->n)
	{
	*head = (*head)->next;
	return (1);
	}
return (1);
}
