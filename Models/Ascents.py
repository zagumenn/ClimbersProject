# Подчинёный класс - класс в котором обрабатывается информация таблицы Acsents
from Models.Model import Model


class Ascents(Model):
    # приватное поле Имя таблицы
    __nameTable = 'Ascents'
    __name = 'name'
    __start_time = 'start_time'
    __finish_time = 'finish_time'
    __mountain_id = 'mountain_id'
    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    # Добавить запись в таблицу
    def add(self):
        name = input("Введите название восхождения: ")
        start_time = input("Введите время начала восхождения: ")
        finish_time = input("Введите время окончания восхождения: ")
        mountain_id = input("Введите id горы: ")

        str = f"{self.__name},{self.__start_time},{self.__finish_time},{self.__mountain_id}"
        super().add(self.__nameTable, str, name,start_time,finish_time,mountain_id )

    # Удалить запись из таблицы запись в таблицу
    def delete(self, id):
        super().delete(self.__nameTable,id)

    # Обновить запись в таблице
    def update(self):
        id = input("Введите id, записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое значение")
        super().update(self.__nameTable,id,field,values)