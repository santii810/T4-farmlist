from src.components.finder.strategies.find_villages_extended import find_villages_ext
from src.components.finder.strategies.find_villages_fast import find_villages_fast
from src.components.finder.strategies.find_villages_recursive import find_villages_recursive


def find_villages(initial_coords):
    radius = 100
    dispersion = 30
    # all_villages = find_villages_fast(initial_coords, radius)
    all_villages = find_villages_ext(initial_coords, radius, dispersion)
    # all_villages = find_villages_recursive(initial_coords, 100)
    return sorted(all_villages)
