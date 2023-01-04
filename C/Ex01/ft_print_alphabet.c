#include <unistd.h>

void    ft_putchar(char s)
{
    write(1, &s, 1);
}

void    ft_print_alphabet(void)
{
    char c;

    c = 'a';
    while(c <= 'z')
    {
        ft_putchar(c);
        c++;
    }
}
int     main(void)
{
    ft_print_alphabet();
    return (0);
}