import datetime
import random
import time
import string

b = string.ascii_lowercase
c = string.digits


n = ""
for sim_1 in range(10):
    n = n + random.choice(b+c)
print(n)


# print(datetime.datetime.today)
# field = 'sfsdfsdfsdf'
# matcher = 'sdfsdfsdfsdf'
# value = 123
# print( **{'%s__%s' % (field, matcher): value} )
# from dateutil.relativedelta import relativedelta
#
#
# rep = {
#     'Год': relativedelta(years=+1),
#     'День': relativedelta(days=+1),
#     'Неделя': relativedelta(weeks=+1),
#     'Месяц': relativedelta(months=+1),
# }
#
# data = datetime.date.today() + rep['Год']
#
# print(data)
