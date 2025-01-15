#Цикл для добавления заголовков
title = []
while True:
    t_1 = input('Введите заголовок. (Для завершения программы введите "стоп" или оставьте поле пустым) ')
    for j in title:
        while t_1 == j:
            t_1 = input('Такой заголовок уже существует, пожалуйста, введите другой заголовок: ')
            continue
    if len(t_1) > 0 and t_1 != 'стоп':
        title.append(t_1)
    else:
        break

print('Заголовки заметки:')
for i in range(len(title)):
    print(f'- {title[i]}')










