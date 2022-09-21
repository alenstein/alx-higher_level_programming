#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a double pointer to the list
 * @number: number to insert to the list
 *
 * Return: address of the new node, or NULL if it failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *buffer = *head;
	listint_t *current;
	int i;

	current = malloc(sizeof(listint_t));
	if (!current)
		return (NULL);

	current->n = number;

	for (i = 0; i < 4; i++)
		buffer = buffer->next;

	current->next = buffer->next;
	buffer->next = current;

	return (buffer->next);

}
