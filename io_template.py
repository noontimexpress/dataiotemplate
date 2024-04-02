import re
import random

#initialize two random integers and multiply them to get answer
firstint, secondint = random.randint(1,10), random.randint(1,10)
answer = str(firstint*secondint)

#put in ticket with multiline capabilities
ticket_lines = []
print(f"Enter ticket below (type the answer to '{firstint}x{secondint}' on a line by itself to finish): ")
while True:
    line = input()
    if line == answer:
        break
    ticket_lines.append(line)

ticket_words = '\n'.join(ticket_lines)

#split tickets in to list of words
word_list = ticket_words.split()
main_emails, cc_emails, garbage_words, new_garbage_words = [], [], [], []

#add default cc email
cc_emails.append('la_dataio@harborpicturecompany.com')

#search for cc value in ticket
cc_match = re.search(r'\b(?:cc|CC|Cc|cC|CC:)\b', ticket_words)

if cc_match:
    cc_val = cc_match.start()
else:
    cc_val = len(ticket_words)              #if ticket doesn't have cc, then make value length of whole ticket

#find and catagorize @s before and after cc
for entry in word_list:
    if ticket_words.find(entry) < cc_val:
        if "@" in entry:
            main_emails.append(entry)
        else: 
            garbage_words.append(entry)
    else:
        if "@" in entry:
            cc_emails.append(entry)
        else:
            garbage_words.append(entry)

#symbols of patterns we don't want
garbage_symbols = r'[;:<>\[\]"\(\)\{\}:;\']'

#replace with blank for every email entry, and string them back
main_email_clean = [re.sub(garbage_symbols,'',email) for email in main_emails]
main_final = ",".join(main_email_clean)

cc_email_clean = [re.sub(garbage_symbols,'',email) for email in cc_emails]
cc_final = ",".join(cc_email_clean)

#add list of services and option for tense
services = ["Media Shuttle", "Pixelogic Aspera", "Frame.io", "Moxion", "Signiant Jet", "Resillion", "Roundabout Aspera", "Pixelogic Aspera", "Netflix Backlot", "Netflix Content Hub"]
tense = ["We're uploading", "We've uploaded"]

#create numeric list for services to display
readable_services = []
for index, service in enumerate(services):
    service = str(service) + "(" + str(index+1) + ")"
    readable_services.append(service)

#prompt user which service to use
service_user = input("Please enter which service (Default MS): " + ', '.join(readable_services) + ". Otherwise, type in your service here: ")
if service_user.isdigit():
    service_sel = services[int(service_user) - 1]
else:               
    if service_user == '':          #if blank, defaults to first entry
        service_sel = services[0]
    else:           
        service_sel = service_user  #if input is non-integer string, it becomes the answer itself

try:
    tense_user = int(input("Present or past (Default Present): "))
except:
    ValueError                      #if it's blank, becomes tense[0]
    tense_user = 1

tense_sel = tense[tense_user - 1]

template_wording = f"\n\nHello,\n\n{tense_sel} the package below to you via {service_sel}.\n\nKindly confirm receipt and successful download."

print(template_wording)
print("\nemail to: \n" + main_final + "\n")
print("cc to: \n" + cc_final + "\n")


