from src.utils import setup_values
from src.components.finder.village_collector import find_villages
from src.components.attack_manager import create_attack_list
from src.utils.lids_factory import create
from src.components.gsheet import insert_into_sheet


# Retorna una lista de aldeas
villages = find_villages(setup_values.vill14_coords)


lid_queue = create(setup_values.lids)
#Retorna una lista de ataques
# attacks = create_attack_list(villages, setup_values.troops, lid_queue, setup_values.tp)
# for i in attacks:
#     print(i)
# print(len(attacks))
insert_into_sheet(villages)
