orders = []
f = open('orders.txt', 'w')
f.close()
with open('orders.txt', 'r') as f:
    for order in f:
        orders.append(order.replace('\n', ''))
i = 1
while True:
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input('Введите название: ')
        orders.append(f'{i}. {name}')
        i += 1
    elif choise == '2':
        print('Покупки:')
        for order in orders:
            print(order)
    elif choise == '3':
        with open('orders.txt', 'w') as f:
            for order in orders:
                f.write(f'{order}\n')
        break
    else:
        print('Не говори так!')
    print()