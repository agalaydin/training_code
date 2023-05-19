#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*result_lst;

	if (*lst)
	{
		while (*lst)
		{
			result_lst = (*lst)->next;
			ft_lstdelone(*lst, del);
			*lst = result_lst;
		}
		*lst = 0;
	}
}
