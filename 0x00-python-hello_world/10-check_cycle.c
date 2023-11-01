#include "lists.h"
/**
 * check_cycle - iterates through a cycle
 * @list - list to iterate
 *
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slo, *fst;
	if (list == NULL || list->next == NULL)
		return (0);
	slo = list->next;
	fst = list->next->next;
	while (slo && fst && fst->next)
	{
		if (slo == fst)
			return (1);
		slo = slo->next;
		fst = fst->next->next;
	}
	return (0);
}
