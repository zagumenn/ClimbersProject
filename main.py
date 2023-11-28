from Models.Climbers import Climbers
from Models.Model import Model
from Models.Mountains import Mountains

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
mountain = Mountains()
print(mountain.get())

for row, list in enumerate(mountain.get()):
    print(row, ': ', list)

mountain.add()
mountain.delete(1)

for row, list in enumerate(mountain.get()):
    print(row, ' - ', list)

mountain.update()