#include "lists.h"

/**
 * get_nodeint_at_index - returns the nth node of a listint_t linked list
 * @head: pointer to the first element of the listint_t list
 * @index: index of the node to return
 *
 * Return: the nth node of a listint_t list, or NULL if node does not exist
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int i;

	for (i = 0; i < index; i++)
	{
		head = head->next;

		if (!head)
			return (NULL);
	}

	return (head);
}

/**
 * list_len - returns the number of elements in a linked list_t list
 * @h: pointer to the list to be printed
 *
 * Return: Number of elements in the list
 */
size_t list_len(const listint_t *h)
{
	size_t count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}

	return (count);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the first element of the list
 *
 * Return: 0 if list is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *buffer = *head;
	size_t len = list_len(buffer);
	size_t index = 0;

	if (!(*head))
		return (1);

	while (index <= (len / 2) - 1)
	{
		int value_1 = get_nodeint_at_index(buffer, index)->n;
		int value_2 = get_nodeint_at_index(buffer, len - 1 - index)->n;

		if (value_1 == value_2)
			index++;
		else
			return (0);
	}
	return (1);
}

