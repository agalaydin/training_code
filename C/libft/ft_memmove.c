#include "libft.h"

void	*ft_memmove(void *dest, const void *source, size_t len)
{
	size_t	i;

	if (!dest && !source)
		return (0);
	i = 0;
	if ((size_t)dest - (size_t)source < len)
	{
		i = len - 1;
		while (i < len)
		{
			((unsigned char *)dest)[i] = ((unsigned char *)source)[i];
			i--;
		}
	}
	else
	{
		while (i < len)
		{
			((unsigned char *)dest)[i] = ((unsigned char *)source)[i];
			i++;
		}
	}
	return (dest);
}
