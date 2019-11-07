import math
import datetime


def calcular_distancia(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


def calcular_tiempo(distancia, velocidad, pt):
    pt_table = [1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]

    if distancia < 20:
        horas = distancia / velocidad
    else:
        tiempo_inicial = 20 / velocidad
        distancia = distancia - 20
        tiempo_plaza_torneos = distancia / (velocidad * pt_table[pt - 1])
        horas = tiempo_inicial + tiempo_plaza_torneos

    min = (horas % 1) * 60
    sec = (min % 1) * 60
    return datetime.time(math.trunc(horas), math.trunc(min), math.floor(sec))


def get_time_difference(a, b):
    return abs((a.hour * 60 + a.minute) - (b.hour * 60 + b.minute))
