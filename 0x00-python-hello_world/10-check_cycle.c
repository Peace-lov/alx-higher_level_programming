/**
 * check_cycle - iterates through a cycle
 * @list - list to iterate
 *
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sl, *fs;
	if (list == NULL || list->next == NULL)
		return (0);
	sl = list->next;
	fs = list->next->next;
	while (sl && fs && fs->next)
	{
		if (sl == fs)
			return (1);
		sl = slo->next;
		fs = fs->next->next;
	}
	return (0);
}
