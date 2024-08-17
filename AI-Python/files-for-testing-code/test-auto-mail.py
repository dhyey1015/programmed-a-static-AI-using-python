import imaplib

# Connect to the Gmail IMAP server
imap_server = imaplib.IMAP4_SSL('imap.gmail.com')

# Login to your Gmail account
username = ''
password = ''
imap_server.login(username, password)

# Select the mailbox (inbox in this case)
mailbox = 'INBOX'
imap_server.select(mailbox)

# Search for emails based on a specific criteria (e.g., all unseen emails)
search_criteria = '(UNSEEN)'
status, email_ids = imap_server.search(None, search_criteria)

# Fetch the email data for each email ID
for email_id in email_ids[0].split():
    # Fetch the email data (RFC822 format)
    status, email_data = imap_server.fetch(email_id, '(RFC822)')
    
    # Process the email data
    # Here, you can parse the email using libraries like email or BeautifulSoup
    # For example, you can use the email library to extract the subject, sender, etc.
    email_message = email.message_from_bytes(email_data[0][1])

    # Print the subject and sender of the email
    print("Subject:", email_message['Subject'])
    print("From:", email_message['From'])
    print("---------------------------------")

# Logout from the Gmail account
imap_server.logout()
