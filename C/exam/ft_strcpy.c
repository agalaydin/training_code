#include <stdio.h>

char	*ft_strcopy(char *s1, char *s2)
{
	int i;

	i = 0;
	while (s2[i])
	{
		s1[i] = s2[i];
		i++;
	}
	s1[i] = '\0';
	return (s1);
}

int main(void)
{
	char a[] = "Hello";
	char b[] = "Worl";
	
	printf("%s\n", ft_strcopy(a, b));
	return (0);
}
