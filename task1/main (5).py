def elem_insert ():     
    print("Список: ")
    list = [1, 2, 3, 4, 5]
    print(list)

    print("Введіть новий елемент ")
    new_element = int(input())

    print("Введіть елемент зі списку після якого вставити новий елемент")
    target_element = int(input())
    try:
        index = list.index(target_element)
    except ValueError:
        print("Елемент не існує у списку. Введіть елемент зі списку після якого вставити новий елемент")
        target_element = int(input())

    list.insert(index + 1, new_element)
    print(list)

elem_insert()