#Обработка дедлайнов.
import datetime

def today_date():                   #- функция  возвращает сегодняшнюю дату
    time=datetime.datetime.today()
    return time
today_date=today_date().date()
print(f'Текущая дата: {datetime.date.strftime(today_date,'%d.%m.%Y')}') # - вывод настоящей даты в виде строки, в формате д.м.г.

def issue_date(): # - функция реализует пользовательский ввод даты в различных форматах (т.е. реализует исключение ошибок) и ее обработку в тип datetime
    while True:
        try:
            t=input('Введите дату дедлайна (в формате: дд.мм.гг.): ')
            t=datetime.datetime.strptime(t,'%d.%m.%Y')
            return t
        except ValueError:
            try:
                t = datetime.datetime.strptime(t, '%d.%m.%y')
                return t
            except ValueError:
                try:
                    t = datetime.datetime.strptime(t, '%Y.%m.%d')
                    return t
                except ValueError:
                    try:
                        t = datetime.datetime.strptime(t, '%y.%m.%d')
                        return t
                    except ValueError:
                        print ('Введен некорректный формат даты')
                        continue
issue_date=issue_date().date()

def delta_days(): # - функция реализует рассчет количества дней до(после) дедлайна и вывод этой информации  в удобном для него виде
    num_date = (issue_date - today_date).days
    if num_date > 0:
        print(f'До дедлайна осталось: {num_date} дн.')
    elif num_date < 0:
        print(f'Внимание! Дедлайн истёк {-(num_date)} дн.назад')
    elif num_date == 0:
        print('Дедлайн сегодня!')
    return num_date
delta_days=delta_days()

