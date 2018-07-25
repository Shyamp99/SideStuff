import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('AutomatedEmailTest-33fdce510dac.json', scope)
# AutomatedEmailTest-33fdce510dac other json file

gc = gspread.authorize(credentials)

#simply returned a refernce to the opened sheet which will be used in AutomatedEmail.py
def openSheet():
    # If you want to be specific, use a key (which can be extracted from
    # the spreadsheet's url)
    sht1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1evwXsX5kt44szDZlB2_P2pmzwHy6chMTPainh8Um2W4/edit#gid=0')
    wks = sht1.worksheet('Sheet1')
    return wks





#just me testing out stuff
wks = openSheet()
#values_list = wks.col_values(1)
#print(values_list)

names = wks.col_values(1)
companies = wks.col_values(2)
emails = wks.col_values(3)
status = wks.col_values(4)
def rando(names,companies,emails, status):
    names = [names[i] for i in range(len(names)) if status[i] == ""]
    companies = [companies[i] for i in range(len(companies)) if status[i] == ""]
    emails = [emails[i] for i in range(len(emails)) if status[i] == ""]
    status = [status[i] for i in range(len(status)) if status[i] == ""]

rando(names,companies,emails, status)
print(names)
print(companies)
print(emails)
print(status)