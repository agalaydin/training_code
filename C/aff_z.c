#include <unistd.h>

// piscine C

int main(int argc, char *argv[])
{
	int i;
	
	i = 0;
	if (argc == 2)
		while (argv[1][i])
		{
			if (argv[1][i] == 'z')
			{			
				write(1, "z", 1);
				break;
			}
		i++;
		}
	else
		write(1, "z", 1);

	write(1, "\n", 1);
}
