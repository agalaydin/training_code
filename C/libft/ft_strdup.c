/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kaarmand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/17 15:25:00 by kaarmand          #+#    #+#             */
/*   Updated: 2021/10/23 15:26:49 by kaarmand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

char	*ft_strdup(const char *str)
{
	char		*dest;
	size_t		length;

	length = ft_strlen(str) + 1;
	dest = malloc(length);
	if (!dest)
		return (0);
	ft_memcpy(dest, str, length);
	return (dest);
}
