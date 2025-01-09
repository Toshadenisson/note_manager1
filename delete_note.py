note_list = [{'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'},
             {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}]
print('Текущий список заметок:')
for i in note_list:
    print(f'-------------------------------------------------\n'
          f'{note_list.index(i) + 1}-ая заметка (id: {id(i)}):')
    for k, v in i.items():
        print(k, v)


def delete_note(): #- Функция позволяет удалять заметку (в виде словаря из списка) по имени пользователя или заголовку.
                    # Реализована возможность подтверждения удаления. Вывод информации, если заметка не найдена.
                    # При вводе имени или заголовка реализована независмость от регистра.
    note_list_copy = [{'Имя': 'Марик', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'},
                      {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}]
    input_ = input('Укажите имя пользователя или заголовок заметки, которую хотите удалить: ').capitalize()
    while input_ == '':
        input_ = input(
            'Вы ничего не указали, пожалуйста, укажите имя пользователя или заголовок еще раз: ').capitalize()
        continue
    else:
        while True:
            for i in note_list:
                if input_ == i.get('Имя') or input_ == i.get('Заголовок'):
                    answ_sure = input('Вы уверены, что хотите удалить заметку!? (Да/Нет): ').capitalize()
                    if answ_sure == 'Да':
                        note_list.remove(i)
                    else:
                        return note_list

                continue
            if len(note_list) != len(note_list_copy):
                print('Заметка успешно удалена!')
            elif len(note_list) == len(note_list_copy):
                print('Заметка не найдена!')
            return note_list
delete_note_list = delete_note()


print('Текущий список заметок: ') #- цикл выводит текущий список заметок в удобном виде.
for dict_ in delete_note_list:
    print(f'-------\n'
          f'{note_list.index(dict_) + 1}-ая заметка (id: {id(dict_)}):')
    for key, value in dict_.items():
        print(f'{key}: {value}')