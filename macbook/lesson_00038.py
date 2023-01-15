import datetime

# datetime форматирование

current_datetime = datetime.datetime.now()

print("Сейчас: {:%d.%m.%Y %H:%M}".format(current_datetime))
