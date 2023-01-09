#include <unistd.h>

int ft_veryf_char(char *str, char c, int index)
{
    int i;

    i = 0;
    while (i < index)
    {
        if (str[i] == c)
            return (0);
        i++;
    }
    return (1);
}

void    ft_inter(char *s1, char *s2)
{
    int i;
    int j;

    i = 0;
    while(s1[i])
    {
        if (ft_veryf_char(s1, s1[i], i))
        {
            j = 0;
            while (s2[j])
            {
                if (s1[i] == s2[j])
                {
                    write(1, &s1[i], 1);
                    break;
                }
                j++;
            }
        }
        i++;
    }
}



int main(int argc, char *argv[])
{
    if ( argc == 3)
        ft_inter(argv[1], argv[2]);
    write(1, "\n", 1);
    return (0);
}
