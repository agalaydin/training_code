/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kaarmand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/22 10:32:26 by kaarmand          #+#    #+#             */
/*   Updated: 2021/10/23 12:40:17 by kaarmand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *str)
{
	int	i;
	int	sign;
	int num;

	i = 0;
	sign = 0;
	num = 0;
	while (*str == ' ' || *str == '\f' || \
			*str == '\n' || *str == '\r' || \
			*str == '\t' || *str == '\v')
		str++;
	if (str[i] == '-')
		sign = -1;
	if (str[i] == '-' || str[i] == '+')
		i++;
	while ((str[i] >= '0') && (str[i] <= '9'))
	{
		num = num * 10;
		num = num + (str[i] - '0');
		i++;
	}
	if (sign < 0)
		num = -num;
	return (num);
}
