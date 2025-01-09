# Работа с несколькими заметками
import datetime

def multiple_note(): # - Функция, которая позволяет пользователю вводить данные для создания нескольких заметок.
                        # Функция выводит список заметок в удобном для пользователя виде. Соодержит в себе внутренние функции.
                        # Сохраняет заметки ( в виде словарей) в один список.
    note_list = []
    while True:
        def username_(): #-Функция обеспечивает ввод имени пользователя и повторный ввод в случае, если имя не указано
            key = 'Имя пользователя'
            value = input('Укажите имя пользователя: ')
            while value == "":
                value = input('Вы не указали имя пользователя. Пожалуйста, укажите имя пользователя еще раз: ')
            else:
                name_dict = {key: value}
                return name_dict

        def title_():#-Функция обеспечивает ввод заголовка пользователя и повторный ввод в случае, если заголовок не указан
            key = 'Заголовок'
            value = input('Укажите заголовок: ')
            while value == "":
                value = input('Вы не указали заголовок. Пожалуйста, укажите заголовок еще раз: ')
            else:
                title_dict = {key: value}
                return title_dict

        def status_():  #Функция реализует ввод или выбор статуса, а также повторный ввод, если статус не правильный
            list_status = ['Новая', 'В процессе', 'Выполнено']
            while True:
                user_stat = (input('Укажите статус заметки\n'
                                   '(Выберите соответствующую цифру\n'
                                   ' или введите статус в текстовом формате):\n'
                                   '1.Новая\n'
                                   '2.В процессе\n'
                                   '3.Выполнено \n'
                                   'Ваш выбор: ').capitalize())
                if user_stat == '1' or user_stat == 'Новая':
                    status_now = list_status[0]
                    break
                if user_stat == '2' or user_stat == 'В процессе':
                    status_now = list_status[1]
                    break
                if user_stat == '3' or user_stat == 'Выполнено':
                    status_now = list_status[2]
                    break
                else:
                    print('Указан не существующий статус.')
                    continue
            status_dict = {'Статус заметки': status_now}
            return status_dict

        def created_date(): # Функция реализует ввод даты создания заметки в указанном формате, ее перевод в тип .datetime и обратно,
                                # предусматривает ввод настоящей даты, если пользователю необходимо.
            while True:
                try:
                    created_date = input('Введите дату создания заметки (в формате: дд.мм.гг. или\n'
                                         'оставьте поле пустым, если хотите указать сегодняшнюю дату): ')
                    if created_date == '':
                        created_date = datetime.date.today()
                        break
                    else:
                        created_date = datetime.datetime.strptime(created_date, '%d.%m.%Y')
                        break
                except ValueError:
                    print('Указан некорреткный формат даты.')
                    continue
            created_date = datetime.date.strftime(created_date, '%d.%m.%Y')
            created_date_dict = {'Дата создания': created_date}
            return created_date_dict


        def issue_date(): #- позволяет пользователю ввести дедлайн, исключает некорректный формат даты.
            while True:
                try:
                    issue_date = input('Введите дедлайн (в формате: дд.мм.гг.): ')
                    issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%Y')
                    break
                except ValueError:
                    print('Указан некорреткный формат даты.')
                    continue
            issue_date = datetime.date.strftime(issue_date, '%d.%m.%Y')
            issue_date_dict = {'Дедлайн': issue_date}
            return issue_date_dict



        def content_():#-Функция обеспечивает ввод описания заметки и повторный ввод в случае, если описание заметки не указано
            value = input('Укажите описание заметки: ')
            while value == "":
                value = input('Вы не указали описание заметки. Пожалуйста, укажите описание еще раз: ')
            else:
                content_dict = {'Описание заметки': value}
                return content_dict


        note = {**username_(),**title_(),**content_(),**status_(),**created_date(),**issue_date()}
        note_list.append(note)
        if input('Хотите добавить еще одну заметку? (Да/Нет): ').capitalize() == 'Да':
            continue
        else:
            return note_list
multiple_note = multiple_note()
print('Список заметок.') # - Цикл выводит список заметок в удобном для пользователя виде.
for i in multiple_note:
    print(f'{multiple_note.index(i) + 1}-ая заметка:')
    for k,v in i.items():
        print(f'{k}: {v}')
    for k in multiple_note:
        print("--------------------------------------------------------")



