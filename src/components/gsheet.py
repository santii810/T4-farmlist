import gspread
from gspread.models import Cell
from oauth2client.service_account import ServiceAccountCredentials
from src.models.attack import Attack
import pprint


def create_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('T4Utils.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('TravianCodex').get_worksheet(0)
    return sheet


# sheet_records = sheet.get_all_records()
# pp = pprint.PrettyPrinter()
# pp.pprint(sheet_records)


def parse_to_google_format(toInsert):
    cells = []
    for i in range(len(toInsert)):
        for j in range(len(toInsert[i].to_gsheet())):
            cells.append(Cell(i + 1, j + 1, toInsert[i].to_gsheet()[j]))
    return cells


def insert_into_sheet(toInsert):
    sheet = create_sheet()
    cells = parse_to_google_format(toInsert)
    print(cells)
    sheet.update_cells(cells)
