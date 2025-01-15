#Проверка и обновление статуса заметки
list_status = ['Выполнено','В процессе','Отложено']
status_now = list_status[1] # - Вывод текущего статуса
print(f'Текущий статус заметки: {status_now}')
while True:                                                     # - цикл, который реализует возможность выбора статуса.
    user_stat = (input('Выберите новый статус заметки\n'
                     '(Укажите соответствующую цифру'
                     ' или введите статус в текстовом формате):\n'
                     '1.Выполнено\n'
                     '2.В процессе\n'
                     '3.Отложено \n'
                     'Ваш выбор: ').capitalize())
    if user_stat == '1' or user_stat == 'Выполнено':
        status_now = list_status[0]
        break
    if user_stat == '2' or user_stat == 'В процессе':
        status_now = list_status[1]
        break
    if user_stat == '3' or user_stat == 'Отложено':
        status_now = list_status[2]
        break
    else:
        print('Указан не существующий статус.')
        continue                                        #- цикл позволяет сделать выбор статуса по номеру или ввести самостоятельно, а также указывает, если статус не существует
status = {'Статус заметки':status_now}
print(f'Статус заметки успешно обновлён на: "{status_now}"')








