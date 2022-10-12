import unittest
from hw6 import people_doc, find_shelf, list_documents, add_documents, delete_doc
from parameterized import parameterized


class TestFunction(unittest.TestCase):
    @parameterized.expand(
        [
            ('10006', 'Владелец документа Аристарх Павлов'),
            ('2207 876234', 'Владелец документа Василий Гупкин'),
            ('11-2', 'Владелец документа Геннадий Покемонов'),
            ('123456', 'Введен не корректный номер документа')

        ]

    )
    def test_people_doc(self, number_people_doc, result):
        etalon = people_doc(number_people_doc)
        self.assertEqual(etalon, result)

    @parameterized.expand(
        [
            ('2207 876234', 'Документ 2207 876234 находится на 1 полке'),
            ('10006', 'Документ 10006 находится на 2 полке'),
            ('11-2', 'Документ 11-2 находится на 1 полке'),
            ('123456', 'Введен не корректный номер документа')

        ]

    )

    def test_find_shelf(self, number_people_doc, result):
        etalon = find_shelf(number_people_doc)
        self.assertEqual(etalon, result)

    def test_list_documents(self):
        etalon = ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"']
        result = list_documents()
        self.assertEqual(etalon, result)

    def test_add_documents(self):
        etalon = 'Данный документ уже добавлен'
        result = add_documents("insurance", "10006", "Аристарх Павлов", 3)
        self.assertEqual(etalon, result)

    def test_delete_doc(self):
        etalon = 'Документ с таким номером не найден'
        result = delete_doc('10007')
        self.assertEqual(etalon, result)

