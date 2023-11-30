from Models.Ascents import Ascents
from Models.Climbers import Climbers

from Models.Model import Model
from Models.Mountains import Mountains
from Models.Regions import Regions

# Методы для таблицы Climbers
#
# climber = Climbers()
# print(climber.get())
# # цикл вывода записей таблицы
# for row, list in enumerate(climber.get()):
#     print(row, ': ', list)
#
# print(climber.getOneField('name'))
#
# for row, list in enumerate(climber.getOneField('name')):
#     print(row,')', list)
#
# climber.add()
# climber.delete(1)
#
# for row, list in enumerate(climber.get()):
#     print(row, ' - ', list)
#
# climber.update()

# Методы для таблицы Mountains

# mountain.add()
# mountain.delete(1)
#
# for row, list in enumerate(mountain.get()):
#     print(row, ' - ', list)

#mountain.update()

# Методы для таблицы Ascents
#ascent = Ascents()
# print(ascent.get())
#
# for row, list in enumerate(ascent.get()):
#     print(row, ': ', list)
#
# ascent.add()
# ascent.delete(1)
#
# for row, list in enumerate(ascent.get()):
#     print(row, ' - ', list)
#
# ascent.update()
#
# Методы для таблицы Regions
region = Regions()

print(region.getOneRow(2)['region'])

for row, col in enumerate(region.getOneRow(2)):
    print(row, col)
for row, col in enumerate(region.get()):
    row+=1
    print(row, col['id'], col['country'], col['region'])


# Методы для таблицы Mountains
mountain = Mountains()
for row, list in enumerate(mountain.get()):
  row+=1
  if region.getOneRow(list['region_id']) != None:
      print(row, list['name'], list['height'],region.getOneRow(list['region_id'])['region'],region.getOneRow(list['region_id'])['country'] )
  else:
      print(row, list['name'], list['height'], "'Страна и регион не указаны'")

ascent = Ascents()
for row, list in enumerate(ascent.get()):
    row += 1
    if region.getOneRow(list['mountain_id']) != None:
        print(row, list['name'],  list['start_time'],  list['finish_time'],mountain.getOneRow(list['mountain_id'])['name'],mountain.getOneRow(list['mountain_id'])['height'])
    else:
        print(row, list['name'],  list['start_time'], list['finish_time'], "'Название и высота не указаны'")

print(mountain.getMountsClimbers)
for row, column in enumerate(mountain.getMountsClimbers):
    date = column['start_time'].strftime("%d-%b-%Y")
    print(f"{row}) Альпинист: {column['name']}, покорил гору {column['Mountains']}, начало восхождения {date} ")
mountain.add()
