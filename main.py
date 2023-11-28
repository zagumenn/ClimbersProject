from Models.Ascents import Ascents
from Models.Climbers import Climbers
from Models.Model import Model
from Models.Mountains import Mountains
from Models.Regons import Regons

# Методы для таблицы Climbers
# climber = Model()
# print(climber.get('Climbers'))

# climber = Climbers()
# print(climber.get())
# цикл вывода записей таблицы
# for row, list in enumerate(climber.get()):
#     print(row, ': ', list)

# print(climber.getOneField('name'))
#
# for row, list in enumerate(climber.getOneField('name')):
#     print(row,')', list)
#
# climber.add()
# climber.delete(1)

# for row, list in enumerate(climber.get()):
    # print(row, ' - ', list)

# climber.update()

# Методы для таблицы Mountains
mountain = Mountains()
print(mountain.get())

for row, list in enumerate(mountain.get()):
    print(row, ': ', list)

mountain.add()
mountain.delete(1)

for row, list in enumerate(mountain.get()):
    print(row, ' - ', list)

mountain.update()

# Методы для таблицы Ascents
ascent = Ascents()
print(ascent.get())

for row, list in enumerate(ascent.get()):
    print(row, ': ', list)

ascent.add()
ascent.delete(1)

for row, list in enumerate(ascent.get()):
    print(row, ' - ', list)

ascent.update()

# Методы для таблицы Regons
regon = Regons()
print(regon.get())

for row, list in enumerate(regon.get()):
    print(row, ': ', list)

regon.add()
regon.delete(1)

for row, list in enumerate(regon.get()):
    print(row, ' - ', list)

regon.update()