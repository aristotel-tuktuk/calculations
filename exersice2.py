#Задача «МКАД»
#Длина Московской кольцевой автомобильной дороги —109 километров. Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час. На какой отметке он остановится через t часов?
#Программа получает на вход значение v и t. Если v>0, то Вася движется в положительном направлении по МКАД, если же значение v<0, то в отрицательном.
v = int(input())
t = int(input())
print((v * t) % 109)
