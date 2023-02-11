#include <stdio.h>

// piscine C

int ft_atoi(const char *str)
{
    int i;
    int num;
    int save;

    i = 0;
    num = 0;
    save = 0;
    while ((str[i] == '\n')
        || (str[i] == '\f')
        || (str[i] == '\v')
        || (str[i] == '\t')
        || (str[i] == '\r')
        || (str[i] == ' '))
            i++;
    while ((str[i] == '-') || (str[i] == '+'))
    {
        if (str[i] == '-')
            save++;
        i++;
    }
    while ((str[i] >= '0') && (str[i] <= '9'))
    {
        num = num * 10 + (str[i] - '0');
        i++;
    }
    if (save % 2 == 1)
        return (-num);
    else
        return (num);
}

int main(void)
{
    char s[] = "  +++---++555hgf";

    printf("%d\n", ft_atoi(s));
    return (0);
}
