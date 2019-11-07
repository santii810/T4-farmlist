from src.components.troptool import get_farm_villages


def remove_dipls(reference, removable):
    for i in reference:
        for j in removable:
            if i == j:
                removable.remove(j)
                break
    return removable


def find_villages(initial_coords):
    radius = 20
    normal_villages = get_farm_villages(initial_coords, radius, False)
    natare_villages = get_farm_villages(initial_coords, radius, True)
    natare_villages = remove_dipls(normal_villages, natare_villages)
    all_villages = normal_villages.union(natare_villages)
    print(f"villages: {len(normal_villages)}")
    print(f"natare: {len(natare_villages)}")
    print(f"all: {len(all_villages)}")
    return sorted(all_villages)
