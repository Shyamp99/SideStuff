import gspread
from oauth2client.service_account import ServiceAccountCredentials
#basically j use this file so AutomatedEmail isn't too crowded


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


