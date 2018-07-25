
from gspreadTest import openSheet
from sparkpost import SparkPost

sp = SparkPost('fee6850f75862cdd3998eeb0a0d5306e66294743')

#opening up the sheet so we can get all values in each column
wks = openSheet()

#getting the values
names = wks.col_values(1)
companies = wks.col_values(2)
emails = wks.col_values(3)
statuses = wks.col_values(4)
liasons = wks.col_values(5)

#removing people we've already emailed
names = [names[i] for i in range(len(names)) if statuses[i] == ""]
companies = [companies[i] for i in range(len(companies)) if statuses[i] == ""]
emails = [emails[i] for i in range(len(emails)) if statuses[i] == ""]
statuses = [statuses[i] for i in range(len(statuses)) if statuses[i] == ""]
liasonss = [liasons[i] for i in range(len(liasons)) if statuses[i] == ""]

#whis is where we do the sending
def send(names, companies, emails, statuses, liasons):
    #sends out each email individually
    #need to find a way to account for emails w same copmany
    for i in range(names):
        subj = "HackRU Sponsoship with " + companies[i]
        response = sp.transmissions.send(
                use_sandbox=True,
                recipients=[emails[i]],
                html='<p>Hello world</p>',
                from_email='shyam@kishan.com',
                subject=subj
            )
print(response)
