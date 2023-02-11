#include <unistd.h>

// piscine C

int ft_space(char y)
{
    if (y == '\t' || y == '\n' || y == '\v' || y == '\f' || y == ' ')
        return (1);
    return (0);
}

void    ft_first_word(char *str)
{
    int i;

    i = 0;
    while (ft_space(*str))
        str++;
    while (*str && !(ft_space(*str)))
        write(1, str++, 1);
}


int main(int argc, char *argv[])
{
    if (argc == 2)
        ft_first_word(argv[1]);
    write(1, "\n", 1);
    return (0);
}

