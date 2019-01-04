from gspreadTest import openSheet
from sparkpost import SparkPost

sp = SparkPost('insert api key here')

#opening up the sheet so we can get all values in each column
wks = openSheet()

#getting the values
names = wks.col_values(5)
companies = wks.col_values(1)
emails = wks.col_values(6)
statuses = wks.col_values(2)
liasons = wks.col_values(4)

#removing people we've already emailed
names = [names[i] for i in range(len(names)) if statuses[i] == ""]
companies = [companies[i] for i in range(len(companies)) if statuses[i] == ""]
emails = [emails[i] for i in range(len(emails)) if statuses[i] == ""]
liasons = [liasons[i] for i in range(len(liasons)) if statuses[i] == ""]
statuses = [statuses[i] for i in range(len(statuses)) if statuses[i] == ""]


#replaces the prommpts with corresponding values
def replace(html, name, liason, company):
    firstNameLiason = liason.split()[0]
    firstNameContact = name.split()[0]
    html = html.replace("(first name of contact)", firstNameContact)
    html = html.replace("(first name)", firstNameLiason)
    html = html.replace("(company)", company)
    html = html.replace("(full name)", liason)
    return html

#this is where we do the sending does it individually
#easily improved w jsons (I think) but I forgot that i had to do this by thurs 7-26 so yep
def send(names, companies, emails, liasons):
    #html formatted template which will then be modified per email
    templateHtml = "<p>Hi (first name of contact),</p>" \
           "<p>My name is (first name), and I'm an organizer for HackRU - a 24-hour biannual hackathon held at Rutgers New Brunswick. We&rsquo;re currently looking for sponsors for our fourteenth HackRU held on April 21-22, 2018 at the Rutgers Athletic Center on Livingston campus at Rutgers University, and we would love for (company) to support us in hosting a great event. You can find out more about HackRU at www.hackru.org .</p>" \
           "<p>HackRU brings together students of all kinds: programmers, entrepreneurs, designers and more! Over the weekend, students work in small teams to bring their ideas to life using your technologies, and with support from evangelists, fellow students and mentors.</p>" \
           "<p>I&rsquo;m attaching our sponsorship document below, where we list several packages and benefits we can offer. Also, feel free to let me know if you would like to discuss alternative perks to the listed packages (such as snacks or meals).</p>" \
           "<p>Please let me know if you have any questions about HackRU and I hope we can have (company) participate in our event!</p>" \
           "<p>Thank you,<br />" \
           "(full name)<br />" \
           "HackRU Sponsorship Team</p>"

    for i in range(len(names)):
        subj = "HackRU Sponsorship with " + companies[i]

        modifiedHtml = replace(templateHtml, names[i], liasons[i], companies[i])

        #p self explanatory but I need to find a way to account for emails w same company
        response = sp.transmissions.send(
                recipients=[emails[i]],
                html=modifiedHtml,
                from_email='shyam@kishan.com',
                subject=subj,
                attachments=[
                   {
                       "name": "HackRU F18 Sponsorship Document.pdf",
                       "type": "pdf",
                       "filename": "C:/Users/shyam/Documents/F18 Sponsorship Document.pdf"
                   }
                ]
        )


send(names, companies, emails, liasons)
print("EMAILS SENT! MAY HACKRU ENDURE FOR MORE THAN 100 SEMESTERS!")

