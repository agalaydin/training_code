from datetime import datetime

date_time_str = '20/10/21 03:59:44'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')

print("The date is", date_time_obj)
