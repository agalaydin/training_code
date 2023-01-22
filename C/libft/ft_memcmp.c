/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kaarmand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/17 15:15:59 by kaarmand          #+#    #+#             */
/*   Updated: 2021/10/23 14:30:24 by kaarmand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *arr1, const void *arr2, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n)
	{
		if (((unsigned char *)arr1)[i] != ((unsigned char *)arr2)[i])
			return (((unsigned char *)arr1)[i] - ((unsigned char *)arr2)[i]);
		i++;
	}
	return (0);
}
