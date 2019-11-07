from src.utils import setup_values
from src.components.village_collector import find_villages
from src.components.attack_manager import create_attack_list
from src.utils.lids_factory import create

villages = find_villages(setup_values.vill14_coords)
# print(len(villages))
# for i in villages:
#     print(i)

lid_queue = create(setup_values.lids)
attacks = create_attack_list(villages, setup_values.troops, lid_queue, setup_values.tp)
for i in attacks:
    print(i)
print(len(attacks))
