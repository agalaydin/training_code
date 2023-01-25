/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Makefile.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kaarmand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/15 17:03:42 by kaarmand          #+#    #+#             */
/*   Updated: 2021/10/15 19:44:47 by Artem            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

NAME		= Libft.a

LIST		= main.c ft_isalpha.c ft_isdigit.c ft_isalnum.c ft_isascii.c \
		  	ft_isprint.c ft_strlen.c ft_memset.c ft_bzero.c ft_memcpy.c \
		  	ft_memmove.c ft_strlcpy.c ft_strlcat.c ft_toupper.c ft_tolower.c \
		  	ft_strchr.c ft_strrchr.c ft_strncmp.c ft_memcmp.c ft_strnstr.c \
		  	ft_atoi.c ft_calloc.c ft_strdup.c ft_substr.c ft_strjoin.c \
			ft_strtrim.c ft_split.c ft_itoa.c ft_strmapi.c ft_striteri.c \
			ft_putchar_fd.c ft_putstr_fd.c ft_putendl_fd.c ft_putnbr_fd.c

LIST_BONUS	= ft_lstnew.c ft_lstadd_front.c ft_lstsize.c ft_lstlast.c \
			  ft_lstadd_back.c ft_lstdelone.c ft_lstclear.c ft_lstiter.c \
			  ft_lstmap.c

OBJ			= $(patsubst %.c, %.o, $(LIST))

OBJ_BONUS	= $(patsubst %.c, %.o, $(LIST_BONUS))

D_FILES		=

OPTFLAGS	= -02

FLAGS		= -Wall -Wextra -Werror

all		:	$(NAME)

$(NAME)	:	$(OBJ)
			  ar rcs $(NAME) $?

%.o		:	%.c
			gcc $(FLAGS) $(OPTFLAGS) -c $< -o -$@ -MD

include $(wildcard $(D_FILES))

bonus	:
			@make OBJ = "$(OBJ_BONUS)" all

clean	:
			@rm -f $(OBJ) $(OBJ_BONUS) $(D_FILES)

fclean	:	clean
			@make -f $(NAME)

re		:	fclean all

.PHONY	:	all clean fclean re bonus

