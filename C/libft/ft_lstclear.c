/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kaarmand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/17 15:04:50 by kaarmand          #+#    #+#             */
/*   Updated: 2021/10/22 13:44:19 by kaarmand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

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
