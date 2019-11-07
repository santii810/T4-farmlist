from src.models.attack import Attack
from src.utils.calculator import calcular_tiempo
from src.utils.calculator import get_time_difference


def create_attack_list(villages, troops_for_attacks, lid_queue):
    attacks = []
    for i in villages:
        imperat = troops_for_attacks['imperat_natare'] if i.natare else troops_for_attacks["imperat_normal"]
        imperan = troops_for_attacks['imperan_natare'] if i.natare else troops_for_attacks["imperan_normal"]
        diff = get_time_difference(calcular_tiempo(i.dist, 7), calcular_tiempo(i.dist, 14))

        # SIEMPRE Creo ataque con imperatoris
        attack = Attack(i, lid_queue['imperat'].get(), imperat)
        attacks.append(attack)

        # si la diferencia de tiempo es mayor a la fijada tambien meto imperatoris
        if diff > 30:
            attack = Attack(i, lid_queue['imperan'].get(), imperan)
            attacks.append(attack)

    return attacks
