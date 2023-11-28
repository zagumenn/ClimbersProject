# Подчинёный класс - класс в котором обрабатывается информация таблицы Climbers
from Models.Model import Model


class Climbers(Model):
    # приватное поле Имя таблицы
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'
    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    # Добавить запись в таблицу
    def add(self):
        name = input("Введите имя: ")
        address = input("Введите адрес: ")
        str = f"{self.__name},{self.__address}"
        super().add(self.__nameTable, str, name,address)

    # Удалить запись из таблицы запись в таблицу
    def delete(self, id):
        super().delete(self.__nameTable, id)

    # Обновить запись в таблице
    def update(self):
        id = input("Введите id, записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое значение")
        super().update(self.__nameTable, id, field, values)
