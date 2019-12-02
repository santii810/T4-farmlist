from src.utils.set_utils import union
from src.utils.set_utils import remove_dipls
from src.components.troptool import get_farm_villages


def generate_new_coords(coord, param):
    if param == 'N':
        coord[1] = coord[1] + 20
    if param == 'S':
        coord[1] = coord[1] - 20
    if param == 'E':
        coord[1] = coord[0] + 20
    if param == 'O':
        coord[1] = coord[0] - 20


def find_village_direction(coord, param, all_villages, already_found_coords):
    generate_new_coords(coord, param)
    print(str(already_found_coords))
    if abs(coord[0]) > 100 or abs(coord[1]) > 100:
        print("alcanzados limites de mapa" + str(coord))
        return True
    if coord in already_found_coords:
        print("coordenadas ya en lista" + str(coord))
        find_village_direction(coord, param, all_villages, already_found_coords)
    print("no hago nada" + str(coord))
    already_found_coords.append(coord)


def find_villages_recursive(initial_coords, needed):
    radius = 30

    all_villages = find_villages(initial_coords, radius)
    already_found_coords = [[initial_coords[0], initial_coords[1]]]
    for i in range(3):
        find_village_direction(initial_coords, 'N', all_villages, already_found_coords)
        find_village_direction(initial_coords, 'S', all_villages, already_found_coords)
        find_village_direction(initial_coords, 'E', all_villages, already_found_coords)
        find_village_direction(initial_coords, 'W', all_villages, already_found_coords)

    print(f"all: {len(all_villages)}")
    return sorted(all_villages)


def find_villages(initial_coords, radius):
    normal_villages = get_farm_villages(initial_coords, radius, False)
    natare_villages = get_farm_villages(initial_coords, radius, True)
    natare_villages = remove_dipls(normal_villages, natare_villages)
    return normal_villages.union(natare_villages)
