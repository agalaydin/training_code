#include <unistd.h>

int main(void)
{
	int i;
	char a;

	i = 25;
	while (i >= 0)
	{
		if ((i % 2) == 0)
		{
			a = i + 'A';
			write(1, &a, 1);
			i--;
		}
		else
		{
			a = i + 'a';
			write(1, &a, 1);
			i--;
		}
	}
}
