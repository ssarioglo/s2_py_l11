pets = dict()                               #Глобально объявил картотеку питомцев
last = []                                   #а так же счетчик id картотеки питомцев

#Функция подставляет "лет", "год" или "года" в зависимости от окончания цифры. Реализовал через остаток от деления на 10.
def get_suffix(age:int):
    if (age > 10 and age < 20) or (age % 10 == 0) or (age % 10 in (5, 6, 7, 8, 9)):
        return "лет"
    elif (age % 10 == 1):
        return "год"
    else:
        return "года"

#Вывод подробной информации о питомце
def p_get(id):
    if id not in pets.keys():               #Проверяем есть ли полученный id в картотеке
        print ("Такого ID нет в картотеке")
        return

    for i in pets[id].keys():               #Такой вот способ считать имя питомца
        name = i
        break
    ctg = pets[id][name]['Вид']             #Читаем остальные параметры и в итоге выводим
    age = pets[id][name]['Возраст']
    owner = pets[id][name]['Имя владельца']
    print(f"Это {ctg} по кличке \"{name}\". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner}")
    return

#Вывод краткого списка питомцев
def p_list():
    print("Краткий список питомцев:")
    for i in pets.keys():
        for j in pets[i].keys():            #Проходим циклом по корневым ключам и по кличкам
            print(f"{i}: {j}")              #Просто печатаем id: кличку
    return

#Удаление имеющейся записи о питомце
def p_delete(id):
    if id not in pets.keys():               #Проверяем есть ли полученный id в картотеке
        print ("Такого ID нет в картотеке")
        return
    last.pop()                              #Счетчик id картотеки обрезаем
    for i in range(id, len(last)):          #Все последующие записи замещают удаленную
        pets[i]=pets[i+1] 
    del pets[len(last)]                     #А удаляется самая последняя оставшаяся запись (теперь дублирующая предпоследнюю)
    print(f"Запись {id} удалена.")
    return

#Изменение имеющейся записи о питомце
def p_update(id):                           
    if id not in pets.keys():               #Проверяем есть ли полученный id в картотеке
        print ("Такого ID нет в картотеке")
        return    
    p_get(id)

    for i in pets[id].keys():               #Получаем имя питомца
        name = i
        break
    ctg = pets[id][name]['Вид']             #Получаем остальные параметры
    age = pets[id][name]['Возраст']
    owner = pets[id][name]['Имя владельца']

    while True:                             #Здесь вводим нужный измененный параметр и в конце запись под данным id перезаписывается
        print("Какое поле требуется изменить (вид, кличку, возраст, имя владельца, 0 - отмена)? ", end='')
        change = input()
        if change == 'вид':
            print("Введите другой вид питомца: ", end='')
            ctg = input()
            break
        elif (change == 'кличку') or (change == 'кличка'):
            print("Введите другую кличку питомца: ", end='')
            name = input()
            break
        elif change == 'возраст':
            print("Введите другой возраст питомца: ", end='')
            age = int(input())
            break
        elif change == 'имя владельца':
            print("Введите другое имя владельца питомца: ", end='')
            owner = input()
            break
        elif change == '0':
            return
        else:
            print("Неверный ввод")

    pets[id] = {name:{'Вид':ctg, 'Возраст':age, 'Имя владельца':owner}}
    print(f"Запись {id} обновлена.")
    p_get(id)
    return

#Функция добавления записи в картотеку
def create():  
    print("Кличка питомца: ", end = '')
    a=input()
    print("Вид питомца: ", end = '')
    b=input()
    print("Возраст питомца: ", end = '')
    c=int(input())
    print("Имя владельца: ", end = '')
    d=input()
    l = len(last)                                               #Счетчик порядковых номеров в картотеке
    pets[l] = {a:{'Вид':b, 'Возраст':c, 'Имя владельца':d}}     #Записывается новая запись в картотеку
    last.append(l)                                              #Инкремент счетчика
    print("Питомец занесен в картотеку.")
    p_get(l)                                                    #Выводим инфо о питомце, которого добавили


# ОСНОВНАЯ ПРОГРАММА

print()
print("Ветеринарная клиника.")

while True:
    print()
    if 0 in pets.keys():                                        #Если в карточке нет питомцев, список команд доступен не весь
        print("Введите команду для работы с питомцами:")
        print("create - занести нового питомца в картотеку")
        print("read - вывести информацию о питомце")
        print("list - вывести полный краткий список питомцев")
        print("update - внести изменения")
        print("delete - удалить питомца из картотеки")
        print("stop - завершить работу с программой")
    else:
        print("В картотеке пока нет питомцев. Доступные команды:")
        print("create - занести нового питомца в картотеку")
        print("stop - завершить работу с программой")


    command = input()
    if command == 'stop':
        break
    elif command == 'create':   #Функция добавления записи в картотеку
        create()                
    elif command == 'read':     #Вывод подробной информации о питомце
        p_list()
        print("Введите порядковый номер питомца: ", end='')
        p_get(int(input()))     
    elif command == 'list':     #Вывод краткой информации по всем питомцам
        p_list()                
    elif command == 'delete':   #Удаление записи
        p_list()
        print("Введите порядковый номер питомца: ", end='')
        p_delete(int(input()))
    elif command == 'update':   #Изменение записи
        p_list()
        print("Введите порядковый номер питомца: ", end='')
        p_update(int(input()))
    else:
        print("Неверная команда")