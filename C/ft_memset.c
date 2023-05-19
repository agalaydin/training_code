#include "libft.h"
#include <stdlib.h>

void	*ft_memset(void *destination, int c, size_t len)
{
	size_t	i;

	i = 0;
	while (i < len)
	{
		((unsigned char *)destination)[i] = c;
		i++;
	}
	return (destination);
}
