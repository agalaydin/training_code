#include "libft.h"
#include <stdlib.h>

char	*ft_strjoin(char const *s1, char const *s2)
{
	char			*new_s;
	unsigned int	i;
	unsigned int	j;

	if (!s1 || !s2)
		return (0);
	new_s = (char *)malloc(sizeof(*new_s) * \
			(ft_strlen(s1) + ft_strlen(s2) + 1));
	if (!new_s)
		return (0);
	i = 0;
	j = 0;
	while (s1[i] != 0)
	{
		new_s[i] = s1[i];
		i++;
	}
	while (s2[j] != 0)
	{
		new_s[i] = s2[j];
		i++;
		j++;
	}
	new_s[i] = 0;
	return (new_s);
}
