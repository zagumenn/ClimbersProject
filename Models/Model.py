from Configuration.config import connnection
# Супер класс для таблиц БД
class Model:


    def getCursor(self, query):
        with connnection().cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    # def get(self, table):
    #     query = f"SELECT * FROM {table}", table
    #     self.myGetCursor()
    # метод вывода данных из таблицы

    def get(self, nametable):
        # query = "SELECT * FROM %s" %nametable
        return self.getCursor("SELECT * FROM %s" %nametable)

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

    def getLastRow(self, table):
        with connnection().close() as cursor:
            query = (
                    """SELECT * FROM '%s' 
                    ORDER BY id DESC LIMIT 1"""%table
            )
            return cursor.getCursor(query)


    def getClimbersDateInterval(self, first_date, lost_date):
        query = (
                """SELECT Climbers.name, Ascents.start_time FROM Ascents_Climbers
                JOIN Climbers ON Ascents_Climbers.climber_id = Climbers.id
                JOIN Ascents ON Ascents_Climbers.ascent_id = Ascents.id
                WHERE Ascents.start_time BETWEEN '%s' AND '%s'"""%(first_date, lost_date)
        )
        return self.getCursor(query)

    def getFields(self, nameTable, *fields):
        fields = ','.join(fields)
        print("SELECT %s FROM %s" %(fields,nameTable))
        return self.getCursor("SELECT %s FROM %s" %(fields,nameTable))

    def numberOfAscents(self):
        with connnection().cursor() as cursor:
            query = (
                "SELECT"
                + " Climbers.name, Mountains.name, COUNT(*)"
                + " AS"
                + " count"
                + " FROM"
                + " Ascents_Climbers, Climbers, Ascents, Mountains"
                + " WHERE"
                + " Ascents_Climbers.climber_id = Climbers.id"
                + " AND"
                + " Ascents_Climbers.ascent_id = Ascents.id"
                + " AND"
                + " Ascents.mountain_id = Mountains.id"
                + " GROUP"
                + " BY"
                + " Climbers.name, Mountains.name"
            )
            cursor.execute(query)
            return cursor.fetchall()
        connnection().close()

    def getNumberOfClimbers(self):
        with connnection().cursor() as cursor:
            query = (
                "SELECT "
                + "Mountains.name, COUNT(*)"
                + "AS "
                + "countClimber "
                + "FROM "
                + "Mountains, Ascents, Ascents_Climbers, Climbers "
                + "WHERE "
                + "Mountains.id = Ascents.mountain_id "
                + "AND "
                + "Ascents.id = Ascents_Climbers.ascent_id "
                + "AND "
                + "Ascents_Climbers.climber_id = Climbers.id "
                + "GROUP "
                + "BY "
                + "Mountains.name "
            )
            cursor.execute(query)
            return cursor.fetchall()
        connnection().close()
    def ascentAndClimber(self):
        with (connnection().cursor() as cursor):
            query = """SELECT Ascents.name, Climbers.name
                    FROM Ascents_Climbers, Ascents, Climbers
                    WHERE Ascents_Climbers.ascents_id = Ascents.id
                    AND Ascents_Climbers.climber_id = Climbers.id
                    """
            cursor.execute(query)
            return cursor.fetchall()
        connnection().close()

    def getTable(self, nameTable):
        with connnection().cursor() as cursor:
            cursor.execute("SELECT * FROM %s", nameTable)
            return cursor.fetchall()
        connnection().close()
    def getOneFields(self, nameTable, fields):
        fields = ''.join(fields)
        with connnection().cursor() as cursor:
            cursor.execute("SELECT %s * FROM %s" %(fields, nameTable))
            return cursor.fetchall()
        connnection().close()






