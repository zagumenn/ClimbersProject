# Подчинёный класс - класс в котором обрабатывается информация таблицы Mountains
from Models.Model import Model


class Mountains(Model):
    # приватное поле Имя таблицы
    __nameTable = 'Mountains'
    __name = 'name'
    __height = 'height'
    __region_id = 'region_id'
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
        region_id = input("Введите id региона: ")
        str = f"{self.__name},{self.__height},{self.__region_id}"
        super().add(self.__nameTable, str, name,height,region_id)

    # Удалить запись из таблицы запись в таблицу
    def delete(self, id):
        super().delete(self.__nameTable,id)

    # Обновить запись в таблице
    def update(self):
        id = input("Введите id, записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое значение")
        super().update(self.__nameTable,id,field,values)