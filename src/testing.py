import gspread
from oauth2client.service_account import ServiceAccountCredentials
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


def insert_into_sheet(rows):
    sheet = create_sheet()
    for i in range(len(rows)):
        sheet.insert_row(rows[i], i)
