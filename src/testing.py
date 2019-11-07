import queue
from src.utils import setup_values
from src.components.village_collector import find_villages
from src.utils.calculator import calcular_tiempo

villages = find_villages(setup_values.vill14_coords)
print(len(villages))
for i in villages:
    print(f"{i} --- {calcular_tiempo(i.dist, 7, 5)}")
