#include <unistd.h>

void    ft_check_word(char *str, int *i)
{
    str = str + *i;
    while (((*str != ' ') && (*str != '\t')) && *str++)
        (*i)++;
}

void    ft_check_space(char *str, int *i)
{
    str = str + *i;
    while (((*str == ' ') || (*str == '\t')) && *str++)
        (*i)++;
}

void    print_word(char *str, int lenght)
{
    while ( *str && lenght)
    {
        write(1, str, 1);
        str++;
        lenght--;
    }
}

void    ft_last_word(char *str)
{
    int i;
    int start;
    int end;

    i = 0;
    start = 0;
    end = 0;
    ft_check_space(str, &i);
    while (str[i])
    {
        start = i;
        ft_check_word(str, &i);
        end = i;
        ft_check_space(str, &i);
        if (!str[i])
            print_word((str + start), (start - end));
    }
}

int main(int argc, char *argv[])
{
    if (argc == 2)
        ft_last_word(argv[1]);
    write(1, "\n", 1);
    return (0);
}
