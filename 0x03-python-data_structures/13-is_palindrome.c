#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - functio that checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}
	prev_slow->next = NULL;
	listint_t *prev = NULL;
	listint_t *current = slow;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	second_half = prev;

	listint_t *first_half = *head;

	while (first_half != NULL && second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
