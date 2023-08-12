#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*result_lst;

	if (new)
	{
		if (!*lst)
		{
			*lst = new;
			return ;
		}
		result_lst = ft_lstlast(*lst);
		result_lst->next = new;
	}
}
