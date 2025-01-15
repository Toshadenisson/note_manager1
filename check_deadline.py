#Обработка дедлайнов.
import datetime

def today_date():                   #- функция возвращает сегодняшнюю дату
    time = datetime.datetime.today()
    return time
today_date = today_date().date()
print(f'Текущая дата: {datetime.date.strftime(today_date,'%d.%m.%Y')}') # - вывод настоящей даты в виде строки, в формате д.м.г.

def issue_date(): # - функция реализует пользовательский ввод даты в различных форматах (т.е. реализует исключение ошибок) и ее обработку в тип datetime
    while True:
        day = input(f"Укажите дату дедлайна (цифрами):\n"
                " день - ").replace('.','')
        month = input(" месяц - ").replace('.','')
        year = input(" год - 20").replace('.','')
        issue_date_input = (day + '.' + month + '.' + '20'+year)
        try:
            issue_date_input = datetime.datetime.strptime(issue_date_input,'%d.%m.%Y')
            print(datetime.date.strftime(issue_date_input,'%d.%m.%Y'))
            return issue_date_input
        except ValueError:
            print ('Введен некорректный формат даты')
            continue

issue_date = issue_date().date()

def delta_days(): # - функция реализует расчет количества дней до(после) дедлайна и вывод этой информации в удобном для него виде
    num_date = (issue_date - today_date).days
    if num_date > 0:
        print(f'До дедлайна осталось: {num_date} дн.')
    elif num_date < 0:
        print(f'Внимание! Дедлайн истёк {-(num_date)} дн.назад')
    elif num_date == 0:
        print('Дедлайн сегодня!')
    return num_date
delta_days = delta_days()
