import requests
import re
from bs4 import BeautifulSoup
from src.models.village import Village
import datetime


def to_time_format(time):
    replaced = re.sub("\\w\\s", ':', time)
    timeUnits = replaced[:-1].split(':')
    while len(timeUnits) < 3:
        timeUnits.insert(0, "0")
    return datetime.time(int(timeUnits[0]), int(timeUnits[1]), int(timeUnits[2]))


def setup(init_coords, range, speed, tp, natare):
    toret = {'xyX': init_coords[0], 'xyY': init_coords[1], 'range': range, 'maxDiff': 2, 'minSpielerCitys': 1,
             'maxSpielerCitys': 15, 'minSpielerEW': 0, 'maxSpielerEW': 10000, 'antiNoob': 'on',
             'speed': speed, 'quick': speed, 'tp': tp}
    if natare:
        toret.update({'nataren': 'on'})
    return toret


def post_request(data):
    getter_url = 'https://www.gettertools.com/ts15.hispano.travian.com/42-Search-inactives'
    response = requests.post(getter_url, data)
    return BeautifulSoup(response.text, features="html.parser")


def obtain_table_rows(input_html, natare):
    table = input_html('table')[1]  # Cojo la tabla con los datos (la 0 tiene el formulario de envío)
    table_rows = table('tr')
    villages = set()

    for row in table_rows[1:]:
        cells = row('td')
        # Regex para sacar coordenadas
        coords = re.findall('showOpenTipCity\((-?\d*),(-?\d*),this\)', str(cells[1]))
        coord_x = coords[0][0]
        coord_y = coords[0][1]

        # Obtención del tiempo (ya no necesaria)
        # time_cell = str(cells[9])  # la celda 9 tiene la info del viaje
        # time = time_cell[4:len(time_cell) - 5]
        villages.add(Village(coord_x, coord_y, natare))
    return villages


def get_farm_villages(init_coords, range, natare):
    setup_values = setup(init_coords, range, 7, 5, natare)
    html = post_request(setup_values)
    return obtain_table_rows(html, natare)
