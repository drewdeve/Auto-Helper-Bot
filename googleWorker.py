import gspread
from oauth2client.service_account import ServiceAccountCredentials

from config import creds_file, scope

creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

table_2021 = client.open('2021')
baza_table = client.open('БАЗА').worksheet('база')

tables = []

january_2021 = table_2021.worksheet('january 2021')
tables.append(january_2021)
march_2021 = table_2021.worksheet('March 2021')
tables.append(march_2021)
february_2021 = table_2021.worksheet('February 2021')
tables.append(february_2021)
may_2021 = table_2021.worksheet('May 2021')
tables.append(may_2021)
june_2021 = table_2021.worksheet('June 2021')
tables.append(june_2021)
july_2021 = table_2021.worksheet('July 2021')
tables.append(july_2021)
august_2021 = table_2021.worksheet('August 2021')
tables.append(august_2021)
september_2021 = table_2021.worksheet('September 2021')
tables.append(september_2021)
october_2021 = table_2021.worksheet('Оctober 2021')
tables.append(october_2021)