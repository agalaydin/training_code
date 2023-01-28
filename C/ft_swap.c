#include <stdio.h>

void	ft_swap(int *a, int *b)
{
	int c;

	c = *a;
	*a = *b;
	*b = c;
}

int main(void)
{
	int x = 1;
	int y = 2;
	ft_swap(&x, &y);
	
	printf("%d\n%d\n", x, y);
}
