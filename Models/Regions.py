# Подчинёный класс - класс в котором обрабатывается информация таблицы Regons
from Models.Model import Model


class Regions(Model):
    # приватное поле Имя таблицы
    __nameTable = 'Regons'
    __country = 'country'
    __region = 'region'
    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    # Добавить запись в таблицу
    def add(self):
        country= input("Введите страну: ")
        region = input("Введите регион: ")
        str = f"{self.__country},{self.__region}"
        super().add(self.__nameTable, str, country,region)

    # Удалить запись из таблицы запись в таблицу
    def delete(self, id):
        super().delete(self.__nameTable,id)

    # Обновить запись в таблице
    def update(self):
        id = input("Введите id, записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое значение")
        super().update(self.__nameTable,id,field,values)

    def getOneRow(self,id):
        if super().getOneRow(self.__nameTable,id) != ():
            return super().getOneRow(self.__nameTable,id)[0]