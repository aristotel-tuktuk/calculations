#Задача «Разность времен»
#Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло между двумя моментами времени.
#Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.
#Выведите число секунд между этими моментами времени.
hours1 = int(input())
minutes1 = int(input())
seconds1 = int(input())
hours2 = int(input())
minutes2 = int(input())
seconds2 = int(input())
print((hours2 - hours1) * 3600 + (minutes2 - minutes1) * 60 + (seconds2 - seconds1))