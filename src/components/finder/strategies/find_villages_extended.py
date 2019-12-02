from src.utils.set_utils import union
from src.utils.set_utils import remove_dipls
from src.components.troptool import get_farm_villages


def find_villages_ext(initial_coords, radius, dispersion):
    all_villages = find_villages_extended(initial_coords, radius)
    extended_coords = [[initial_coords[0] + dispersion, initial_coords[1]],
                       [initial_coords[0] - dispersion, initial_coords[1]],
                       [initial_coords[0], initial_coords[1] + dispersion],
                       [initial_coords[0], initial_coords[1] - dispersion],
                       [initial_coords[0] - dispersion, initial_coords[1] - dispersion],
                       [initial_coords[0] - dispersion, initial_coords[1] + dispersion],
                       [initial_coords[0] + dispersion, initial_coords[1] - dispersion],
                       [initial_coords[0] + dispersion, initial_coords[1] + dispersion]
                       ]
    for i in extended_coords:
        query = find_villages_extended(i, radius)
        all_villages = union(all_villages, query)

    print(f"all: {len(all_villages)}")
    return sorted(all_villages)


def find_villages_extended(initial_coords, radius):
    normal_villages = get_farm_villages(initial_coords, radius, False)
    natare_villages = get_farm_villages(initial_coords, radius, True)
    natare_villages = remove_dipls(normal_villages, natare_villages)
    return normal_villages.union(natare_villages)
