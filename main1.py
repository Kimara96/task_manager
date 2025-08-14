#open the file emails.txt in READ mode
file = open ("emails.txt", "r")
#Read and split the data using \n to get a list
emails = file.read().split("\n")
#Loop over the list of emails and print a generated username for each of them i.e username is all characters before the @
for email in emails:
    if "@" in email and email != "":
        username = email.split("@")[0]
        print( username)
        