# Program to delete junk email from known bad domains
# This code is a hack of code obtained from: https://github.com/awangga/outlook

import outlook

def readjunkdomains():
    """Reads the file of junk domain or email names into a List. """
    filename = "junkdomains.txt"
    addresses = []
        
    with open(filename) as file_object:
        lines = file_object.readlines()
        
    for line in lines:
        addresses.append(line.lower().rstrip())
 
    return addresses
        
# Read in the junk domain names to be used
domains = readjunkdomains()
# Just an empty list - maybe my bad coding for this variable
emptylst = []

# Code invoking outlook.py which was obtained from this site: https://github.com/awangga/outlook
mail = outlook.Outlook()
mail.login('myemailaccount@hotmail.com','mypassword')
i = 0

jmstatus, msgs = mail.junk()
#print("stat = " + jmstatus + " count = " + str(msgs))
if jmstatus == 'OK' and msgs != ['0']:
    lstIds = mail.allIds()
    if (lstIds != emptylst):
        print("Processing...")
        for id in lstIds:
            mail.getEmail(id)
            mailsender = mail.mailfrom()
            print("Sender = " + mailsender)
            for domain in domains:
                if domain in mailsender:
                    # Delete email immediately
                    mail.mailstore(id, '+FLAGS', '\\Deleted')
                    i += 1
                    print("Email deleted!")
                    break
        print(str(i) + " out of " + str(len(lstIds)) + " Processed")
    else:
        print("allIds returned an empty list")
else:
    print("Junk empty or failed to be read")
 