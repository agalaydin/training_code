# разбиваем на фрагменты

def chunk(ishod_list, size):
    return [ishod_list[i:i + size] for i in range(0, len(ishod_list), size)]

ishod_list = ['q', 'w', 'e', 'r', 't', 'y']
print(chunk(ishod_list, 2))
