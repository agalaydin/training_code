/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kaarmand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/17 15:49:47 by kaarmand          #+#    #+#             */
/*   Updated: 2021/10/22 14:24:41 by kaarmand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t			i;
	unsigned int	diff;

	i = 0;
	diff = 0;
	while ((i < n) && !diff && (s1[i] != 0) && (s2[i] != 0))
	{
		diff = (unsigned char)s1[i] - (unsigned char)s2[i];
		i++;
	}
	if (i < n && !diff && (s1[i] == 0 || s2[i] == 0))
		diff = (unsigned char)s1[i] - (unsigned char)s2[i];
	return (diff);
}
