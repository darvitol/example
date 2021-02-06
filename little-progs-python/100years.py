import time
import datetime

from day import now

name = input("Введите имя: ")
age = int(input("Сколько Вам лет? "))

'''
res = 100 - age
today_day = datetime.datetime.today()
today_day_int = time.strftime("%Y")
in100 = int(today_day_int) + res
print ("Вам будет 100 лет в ", in100, 'году')
'''

year = str((now.year - age) + 100)
print(year)