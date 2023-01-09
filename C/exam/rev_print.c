#include <unistd.h>

int ft_strlen(char *s)
{
    int i;

    i = 0;
    while (s[i])
        i++;
    return (i);
}

void    ft_rev_print(char *str)
{
    int i;
    int j;

    j = 0;
    i = ft_strlen(str) - 1;
    while (i >= j)
    {
        write(1, &str[i], 1);
        i--;
    }
}


int main(int argc, char *argv[])
{
    if (argc == 2)
        ft_rev_print(argv[1]);
    write(1, "\n", 1);
    return (0);
}
