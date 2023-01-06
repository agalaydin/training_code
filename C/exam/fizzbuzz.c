#include <unistd.h>

void putnbr(int nbr)
{
	char c;
	
	if (nbr >= 10)
		putnbr(nbr / 10);
	c = (nbr % 10) + '0';
	write(1, &c, 1);
}

int main(void)
{
	int i;

	i = 1;
	while ( i <= 30)
	{
		if ((i % 3) == 0 && (i % 5) == 0)
			write(1, "fizzbuzz", 8);
		else if ((i % 3) == 0)
			write(1, "fizz", 4);
		else if ((i % 5) == 0)
			write(1, "buzz", 4);
		else
			putnbr(i);
		write(1, "\n", 1);
		i++;
	}

}
