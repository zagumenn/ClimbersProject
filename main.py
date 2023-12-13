from Models.Ascents import Ascents
from Models.AscentsClimbers import AscentsClimbers
from Models.Climbers import Climbers
from Models.Model import Model
from Models.Mountains import Mountains
from Models.Regions import Regions

test = Model()
# print(test.ascentAndClimber())
# clim = Climbers()
# print(clim.get())
ascent = Ascents()
print(ascent.get())
print(ascent.getClimbersDateInterval('2023-10-06', '2024-12-01'))
print(test.getFields('Ascents', 'id', 'name', 'start_time'))
