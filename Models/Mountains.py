# Подчинёный класс - класс в котором обрабатывается информация таблицы Mountains
from mysql.connector import cursor

from Models.Model import Model


class Mountains(Model):
    # приватное поле Имя таблицы
    __nameTable = 'Mountains'
    __name = 'name'
    __height = 'height'
    __region_id = 'region_id'
    __country = 'country'
    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    # Добавить запись в таблицу
    def add(self):
        name = input("Введите название: ")
        height = input("Введите высоту: ")
        str = f"{self.__name},{self.__height}"
        super().add(self.__nameTable, str, name,height)

    # Удалить запись из таблицы запись в таблицу
    def delete(self, id):
        super().delete(self.__nameTable,id)

    # Обновить запись в таблице
    def update(self):
        id = input("Введите id, записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое значение")
        super().update(self.__nameTable,id,field,values)

    def getOneRow(self, id):
        if super().getOneRow(self.__nameTable, id) != ():
            return super().getOneRow(self.__nameTable, id)[0]
    @property
    def getMountsClimbers(self):
        return super().getMountsClimbers()

