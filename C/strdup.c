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
