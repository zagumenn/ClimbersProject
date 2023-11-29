import mysql.connector

# Подключение к базе данных
db = mysql.connector.connect(
  host="localhost",
  user="Stanislav",
  password="666666",
  database="climbersproject"
)

cursor = db.cursor()
# 1.) Функция для показа списка групп, осуществлявших восхождение для каждой горы в хронологическом порядке
def show_groups_by_mountain():
    query = "SELECT m.name, a.name FROM mountains m JOIN ascents a ON m.id = a.mountain_id ORDER BY a.start_time"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(f"Гора: {row[0]}, Группа: {row[1]}")

# 2.) Функция для добавления новой вершины
def add_mountain(name, height, country_id, region_id):
    query = "INSERT INTO mountains (name, height, country_id, region_id) VALUES (%s, %s, %s, %s)"
    values = (name, height, country_id, region_id)
    cursor.execute(query, values)
    db.commit()
    print("Новая вершина успешно добавлена")

# 3.) Функция для изменения данных о вершине, если на нее не было восхождения
def update_mountain(mountain_id, name, height, country_id, region_id):
    query = "UPDATE mountains SET name = %s, height = %s, country_id = %s, region_id = %s WHERE id = %s"
    values = (name, height, country_id, region_id, mountain_id)
    cursor.execute(query, values)
    db.commit()
    if cursor.rowcount == 0:
        print("Вершина не найдена или на нее уже было восхождение")
    else:
        print("Данные о вершине успешно обновлены")

# 4.) Функция для показа списка альпинистов, осуществлявших восхождение в указанный интервал дат
def show_climbers_by_date_interval(start_date, end_date):
    query = "SELECT c.name FROM climbers c JOIN ascents_climbers ac ON c.id = ac.climber_id JOIN ascents a ON ac.ascent_id = a.id WHERE a.start_time BETWEEN %s AND %s"
    values = (start_date, end_date)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for row in result:
        print(f"Альпинист: {row[0]}")

# 5.) Функция для добавления нового альпиниста в состав указанной группы
def add_climber_to_group(climber_id, ascent_id):
    query = "INSERT INTO ascents_climbers (ascent_id, climber_id) VALUES (%s, %s)"
    values = (ascent_id, climber_id)
    cursor.execute(query, values)
    db.commit()
    print("Новый альпинист успешно добавлен в группу")

# 6.) Функция для показа информации о количестве восхождений каждого альпиниста на каждую гору
def show_climber_mountain_counts():
    query = "SELECT c.name, m.name, COUNT(*) FROM climbers c JOIN ascents_climbers ac ON c.id = ac.climber_id JOIN ascents a ON ac.ascent_id = a.id JOIN mountains m ON a.mountain_id = m.id GROUP BY c.name, m.name"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(f"Альпинист: {row[0]}, Гора: {row[1]}, Количество восхождений: {row[2]}")

# 7.) Функция для показа списка восхождений (групп), которые осуществлялись в указанный период времени
def show_ascents_by_date_interval(start_time, finish_time):
    query = "SELECT a.name FROM ascents a WHERE a.start_time BETWEEN %s AND %s"
    values = (start_time, finish_time)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for row in result:
        print(f"Восхождение: {row[0]}")

# 8.) Функция для добавления новой группы
def add_group(name, mountain_id, start_time):
    query = "INSERT INTO ascents (name, mountain_id, start_time) VALUES (%s, %s, %s)"
    values = (name, mountain_id, start_time)
    cursor.execute(query, values)
    db.commit()
    print("Новая группа успешно добавлена")

# 9.) Функция для получения информации о количестве альпинистов на каждой горе
def get_climbers_count_by_mountain():
    query = "SELECT m.name, COUNT(*) FROM mountains m JOIN ascents a ON m.id = a.mountain_id JOIN ascents_climbers ac ON a.id = ac.ascent_id GROUP BY m.name"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(f"Гора: {row[0]}, Количество альпинистов: {row[1]}")


show_groups_by_mountain()
add_mountain("Эверест", 8848, 1, 1)
update_mountain(1, "Килиманджаро", 5895, 2, 1)
show_climbers_by_date_interval("2023-01-01", "2023-12-31")
add_climber_to_group(1, 1)
show_climber_mountain_counts()
show_ascents_by_date_interval("2023-01-01", "2023-12-31")
add_group("Группа 1", 1, "2023-01-01")
get_climbers_count_by_mountain()
db.close()
