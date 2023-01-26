#include <unistd.h>

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

void    ft_print_comb(void)
{
    int num1;
    int num2;
    int num3;

    num1 = 0;
    num2 = 0;
    num3 = 0;
    while(num1 < 8)
    {
        num2 = num1 + 1;
        while(num2 < 9)
        {
            num3 = num2 + 1;
            while(num3 <=9)
            {
                ft_putchar(num1 + '0');
                ft_putchar(num2 + '0');
                ft_putchar(num3 + '0');               
                ft_putchar(',');
                ft_putchar(' ');
                num3++;
            }
            num2++;
        }
        num1++;
    }
}

int     main(void)
{
    ft_print_comb();
    return 0;
}
