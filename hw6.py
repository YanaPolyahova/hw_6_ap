documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': ['203040']
       }

# Необходимо реализовать использование команды, которые могут реализовать следующие функции:
#
# p– люди – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s– полка – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуацию, когда пользователь будет возбуждать возбуждающий документ .
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a– добавить – команда, которая добавит новый документ в каталог и в список полок, спросив его номер, тип, имя владельца и номер полки, на кого он будет храниться. Корректно обработайте ситуацию, когда пользователь будет добавлять документ на расширяющуюся полку .
# Внимание : p, s, l, a - это посещаемая группа, а не название функции. Функции должны иметь определенное название, передающее ее действие.
# d– удалить – команда, которая спросит номер документа и удалит его из каталога и из перечня полей. Предусмотрите сценарий, когда пользователь вводит продвигающий документ ;

def people_doc(number_doc): #команда p
    #number_doc = input('Введите номер документа: ')
    for document in documents:
        if number_doc in document.values():
            return f'Владелец документа {document["name"]}'
    return 'Введен не корректный номер документа'


def find_shelf(number_doc): #команда s
    #number_doc = input('Введите номер документа: ')
    for keys, values in directories.items():
        if number_doc in values:
            return f'Документ {number_doc} находится на {keys} полке'
    return 'Введен не корректный номер документа'

def list_documents(): #команда l
    list_info = []
    for document in documents:
        list_info.append('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))
    return list_info

def add_documents(type_, number, name, choosen_shelf): #команда a
    new_doc = {}
    new_doc['type'] = type_
    new_doc['number'] = number
    new_doc['name'] = name
    if new_doc not in documents:
        #choosen_shelf = input('На какую полку положить документ (1, 2, 3)? ')
        if choosen_shelf in directories:
            directories[choosen_shelf].append(new_doc['number'])
            documents.append(new_doc)
            return f'Документ добавлен на {choosen_shelf} полку'
        else:
            return 'Введите корректные данные'
    else:
        return 'Данный документ уже добавлен'


def delete_doc(number_doc): #команда d
    #number_doc = input('Введите номер документа: ')
    d = 0
    for document in documents:
        if number_doc in document.values():
            documents.remove(document)
            d = 1
    for directory in directories:
        if number_doc in directories.values():
            directories.remove(directory)
            d = 1
    if d == 1:
        return 'Документ успешно удален'
        return documents

    else:
        return 'Документ с таким номером не найден'

def main_func():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            print(people_doc())
        elif command == 's':
            print(find_shelf())
        elif command == 'l':
            print(list_documents())
        elif command == 'a':
            print(add_documents())
        elif command == 'd':
            print(delete_doc())
        elif command == 'q':
            print('Выход')
            break
        else:
            print('Это не корректная комманда!')
#main_func()

print(people_doc('10006'))
print(find_shelf('12345'))
print(list_documents())
print(add_documents('insurance', '10006', 'Аристарх Павлов', 2))
print(delete_doc('10007'))
