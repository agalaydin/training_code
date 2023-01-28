#include <unistd.h>

void	maff_alpha(void)
{
	int i;
	int a;

	i = 0;
	while (i <= 25)
	{
		if ((i % 2) == 0)
		{
			a = i + 'a';
			write(1, &a, 1);
			i++;
		}
		else
		{
			a = i + 'A';
			write(1, &a, 1);
			i++;
		}
	}
}

int main(void)
{
	maff_alpha();
} 

