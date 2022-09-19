#include "lists.h"

/**
 * check_cycle - function to check if a linked list has a cycle in it
 * @list: pointer to the first element of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *buffer = list;

	while (buffer)
	{
		buffer = buffer->next;

		if (buffer == list)
			return (1);
	}

	return (0);
}
