#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new;
	t_list	*value;
	t_list	*temp;

	if (!lst || !f)
		return (0);
	new = ft_lstnew(f(lst->content));
	if (!new)
		return (0);
	value = new;
	lst = lst->next;
	while (lst)
	{
		temp = ft_lstnew(f(lst->content));
		if (!temp)
		{
			ft_lstclear(&new, del);
			return (0);
		}
		value->next = temp;
		value = temp;
		lst = lst->next;
	}
	return (new);
}
