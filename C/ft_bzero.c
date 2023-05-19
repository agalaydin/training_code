#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	unsigned int	i;
	char			*ptr;

	ptr = (char *)s;
	i = 0;
	while (i < n)
	{
		*(ptr + i) = 0;
		i++;
	}
}
