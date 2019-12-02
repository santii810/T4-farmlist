from src.utils.set_utils import union
from src.utils.set_utils import remove_dipls
from src.components.troptool import get_farm_villages


def find_villages_fast(initial_coords, radius):
    normal_villages = get_farm_villages(initial_coords, radius, False)
    natare_villages = get_farm_villages(initial_coords, radius, True)
    natare_villages = remove_dipls(normal_villages, natare_villages)
    return normal_villages.union(natare_villages)
