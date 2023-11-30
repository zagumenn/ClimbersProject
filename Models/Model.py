from Configuration.config import connnection
# Супер класс для таблиц БД
class Model:

    # метод вывода данных из таблицы
    def get(self, table):
        with connnection().cursor() as cursor:
            select_all_rows = f"SELECT * FROM {table}"
            cursor.execute(select_all_rows)
            return cursor.fetchall()
        connnection().close()

    def getOneField(self, table, field):
        with connnection().cursor() as cursor:
            select_one_field = f"SELECT {field} FROM {table}"
            cursor.execute(select_one_field)
            return cursor.fetchall()
        connnection().close()
#       Добавить запись в таблицу
    def add(self, table, str, *values):
        with connnection().cursor() as cursor:
            print(f"INSERT INTO {table} ({str}) VALUES {values}")
            query = f"INSERT INTO {table} ({str}) VALUES {values}"
            cursor.execute(query)
        connnection().close()
        print(f"Новая запись в таблицу {table} добавлена")

#       Удаление записи
    def delete(self,table, id):
        with connnection().cursor() as cursor:
            query_delete = f"DELETE FROM {table} WHERE id = {id}"
            cursor.execute(query_delete)
        connnection().close()
        print("Запись удалена")

    def update(self, table, id, field, values):
        with connnection().cursor() as cursor:
            # print(f"UPDATE {table} set {field} = '{values}' where id = {id} ")
            query_update = f"UPDATE {table} SET {field} = '{values}' WHERE id = {id} "
            cursor.execute(query_update)
            connnection().commit()
        connnection().close()
        print("Запись обновлена")

    def getOneRow(self,table,id):
        with connnection().cursor() as cursor:
            query = f"SELECT * FROM {table} WHERE id = {id}"
            cursor.execute(query)
            return cursor.fetchall()
        connnection().close()

    def getMountsClimbers(self):
        with connnection().cursor() as cursor:
            query = ("select Climbers.name, Ascents.start_time, "
            + "(SELECT name from Mountains where id = Ascents.mountain_id) AS Mountains"
            + " from Ascents_Climbers"
            + " JOIN Ascents"
            + " ON Ascents_Climbers.ascent_id = Ascent_id"
            + " JOIN Climbers"
            + " ON Ascents_Climbers.climber_id = Climbers.id"
            + " ORDER BY Ascents.start_time")
            cursor.execute(query)
            return cursor.fetchall()
        connnection().close()




