import math
import datetime


def calcular_distancia(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


def calcular_tiempo(distancia, velocidad):
    horas = distancia / velocidad
    min = (horas % 1) * 60
    sec = (min % 1) * 60
    return datetime.time(math.trunc(horas), math.trunc(min), math.floor(sec))


def get_time_difference(a, b):
    return abs((a.hour * 60 + a.minute) - (b.hour * 60 + b.minute))
