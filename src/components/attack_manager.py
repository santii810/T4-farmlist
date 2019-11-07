from src.models.attack import Attack
from src.utils.calculator import calcular_tiempo
from src.utils.calculator import get_time_difference


def count_troops(a, b):
    for i in range(6):
        a[i] = a[i] + b[i]
    return a


def create_attack_list(villages, troops_for_attacks, lid_queue, tp):
    attacks = []
    total_troops = [0, 0, 0, 0, 0, 0]
    for i in villages:
        imperat = troops_for_attacks['imperat_natare'] if i.natare else troops_for_attacks["imperat_normal"]
        imperan = troops_for_attacks['imperan_natare'] if i.natare else troops_for_attacks["imperan_normal"]
        diff = get_time_difference(calcular_tiempo(i.dist, 7, tp), calcular_tiempo(i.dist, 14, tp))

        # SIEMPRE Creo ataque con imperatoris
        if (lid_queue['imperat'].qsize() > 0):
            attacks.append(Attack(i, lid_queue['imperat'].get(), imperat))
            total_troops = count_troops(total_troops, imperat)

        # si la diferencia de tiempo es mayor a la fijada tambien meto imperatoris
        if diff > 30:
            if (lid_queue['imperan'].qsize() > 0):
                attacks.append(Attack(i, lid_queue['imperan'].get(), imperan))
                total_troops = count_troops(total_troops, imperan)
    print(total_troops)
    return attacks
