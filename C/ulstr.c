#include <unistd.h>

int main(int argc, char *argv[])
{
	int i;
	char *str;

	i = 0;
	if (argc == 2)
	{	str = argv[1];
		while(str[i])
		{
			if (str[i] >= 'a' && str[i] <= 'z')
			{
				str[i] = str[i] - 32;

			}
			else if (str[i] >= 'A' && str[i] <= 'Z')
			{
				str[i] = str[i] + 32;

			}
			write(1, &str[i], 1);
			i++;
		}
	}
	else
		write(1, "\n", 1);
	
}
