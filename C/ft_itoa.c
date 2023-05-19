#include "libft.h"
#include <stdlib.h>

static void	ft_check(int *n, int *sign, int *value)
{
	if (*n == -2147483648)
	{
		*n = *n + 1;
		*sign = -1;
		*value = 1;
		*n = *n * -1;
	}
	else if (*n < 0)
	{
		*sign = -1;
		*n = *n * -1;
		*value = 0;
	}
	else if (*n >= 0)
	{
		*sign = 1;
		*value = 0;
	}
}

static int	ft_length(int n)
{
	int	len;

	len = 0;
	while (n > 9)
	{
		n = n / 10;
		len++;
	}
	len++;
	return (len);
}

static void	ft_write(char *str, int len, int n, int value)
{
	while (n > 9)
	{
		str[len--] = (n % 10) + '0' + value;
		n = n / 10;
		value = 0;
	}
	str[len] = n + '0';
}

char	*ft_itoa(int n)
{
	int		sign;
	int		value;
	int		len;
	char	*str;

	ft_check(&n, &sign, &value);
	len = ft_length(n);
	if (sign == -1)
	{
		str = malloc((len + 2) * sizeof(char));
		if (!str)
			return (0);
		len++;
		str[0] = '-';
	}
	else
	{
		str = malloc((len + 1) * sizeof(char));
		if (!str)
			return (0);
	}
	str[len--] = '\0';
	ft_write(str, len, n, value);
	return (str);
}
