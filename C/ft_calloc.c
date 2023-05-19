#include "libft.h"
#include <stdlib.h>

void	*ft_calloc(size_t num, size_t size)
{
	void	*ptr;

	ptr = malloc(num * size);
	if (ptr == 0)
		return (ptr);
	ft_bzero(ptr, num * size);
	return (ptr);
}
