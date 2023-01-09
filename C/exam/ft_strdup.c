#include <stdlib.h>
#include <stdio.h>

int ft_strlen(char *str)
{
    int l;

    l = 0;
    while (str[l])
        l++;
    return (l);
}

char    *ft_strdup(char *str)
{
    int i;
    char *c;

    i = ft_strlen(str);
    c = malloc(sizeof(*str) * (i + 1));
    if (c == NULL)
        return (NULL);
    i = 0;
    while (str[i])
    {
        c[i] = str[i];
        i++;
    }
    c[i] = '\0';
    return (c);
}

int main(void)
{
    char a[] = "Hi";

    printf("%s\n", ft_strdup(a));
    return (0);
}
