#include "lists.h"

/**
 * insert_node - insertion than number in a list in order
 * @head: double pointer in the firt elem
 * @number: the value to insert in the list
 * Return: the new one
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *n_n = malloc(sizeof(listint_t));
	if (!n_n)
		return (NULL);
	n_n->n = number;
	n_n->next = NULL;
	if (!nd || n_n->n < nd->n)
	{
		n_n->next = nd;
		return (*head = n_n);
	}
	while (nd)
	{
		if (!nd->next || n_n->n < nd->next->n)
		{
			n_n->next = nd->next;
			nd->next = n_n;
			return (nd);
		}
		nd = nd->next;
	}
	return (NULL);
}
