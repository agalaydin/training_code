#include <unistd.h>
#include <stdio.h>

void    ft_repeat_alpha(char *str)
{
    int i;
    int l;
    
    i = 0;
    while (str[i])
    {
        l = 0;
        if (str[i] >= 'A' && str[i] <= 'Z')
            l = str[i] - 64;
        else if (str[i] >= 'a' && str[i] <= 'z')
            l = str[i] - 96;
        else
            l = 1;
        while (l--)
            write(1, &str[i], 1);
        i++;
    }
}
int main(int argc, char *argv[])
{
    if (argc == 2)
        ft_repeat_alpha(argv[1]);
    write(1, "\n", 1);
    return (0);
}
