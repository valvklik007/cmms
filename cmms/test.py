from datetime import datetime, timedelta
from openpyxl import Workbook

d = datetime.today().strftime('%Y-%m-%d')
print(d)

# wb = Workbook()
# ws = wb.active
# ws.title = "Schedule"
#
# # Заголовки
# headers = ["", "Станок", "Частота", "Дата начала"]
#
# start_date = datetime.strptime("2025-1-1", '%Y-%m-%d')
# end_date = datetime.strptime("2025-12-31", '%Y-%m-%d')
#
#
# # Добавляем заголовки для всех дней месяца
# date_headers = [(start_date + timedelta(days=i)).strftime("%d-%b") for i in range((end_date - start_date).days + 1)]
# headers.extend(date_headers)
#
# ws.append(headers)
#
# # Заполняем строки
# for record in range(1, 11):
#     row = [
#         record,
#         record,
#         record,
#         record
#     ]
#
#     # Генерируем пустые ячейки для дат
#     # date_cells = [""] * len(date_headers)
#     #
#     # # Логика установки "X" по частоте обслуживания
#     # task_start = record.start_date
#     # for i, date_str in enumerate(date_headers):
#     #     current_date = datetime.strptime(date_str, "%d-%b")
#     #
#     #     if record.frequency == "Everyday":
#     #         date_cells[i] = "X"
#     #     elif record.frequency == "Monthly" and task_start.day == current_date.day:
#     #         date_cells[i] = "X"
#     #     elif record.frequency == "Quarterly" and task_start.day == current_date.day:
#     #         date_cells[i] = "X"
#
#     # row.extend(date_cells)
#     ws.append(row)
#
# # Сохраняем файл
# wb.save("maintenance_schedule.xlsx")
# print("Файл сохранен: maintenance_schedule.xlsx")

# for i in range((end_date - start_date).days + 1):
#     date_headers.append((start_date + timedelta(days=i)).strftime("%d-%b"))

# import datetime
# import random
# import time
# import string
#
# b = string.ascii_lowercase
# c = string.digits

#
# n = ""
# for sim_1 in range(10):
#     n = n + random.choice(b+c)
# print(n)


# print(datetime.datetime.today)
# field = 'sfsdfsdfsdf'
# matcher = 'sdfsdfsdfsdf'
# value = 123
# print( **{'%s__%s' % (field, matcher): value} )
# from dateutil.relativedelta import relativedelta
#
# #
# rep = {
#     'Год': relativedelta(years=+1),
#     'День': relativedelta(days=+1),
#     'Неделя': relativedelta(weeks=+1),
#     'Месяц': relativedelta(months=+1),
# }
# from dateutil.relativedelta import relativedelta
#
# data = datetime.date.today() + relativedelta(months=-11)
# print(data)
# #
# print(data)
