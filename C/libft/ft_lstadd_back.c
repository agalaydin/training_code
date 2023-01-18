/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kaarmand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/17 15:03:43 by kaarmand          #+#    #+#             */
/*   Updated: 2021/10/22 13:41:29 by kaarmand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

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
