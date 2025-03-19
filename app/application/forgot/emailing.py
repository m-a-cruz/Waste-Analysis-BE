from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

# Scope for sending emails
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    # Authenticate and get access token
    creds = None
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'TrashTalk-BE/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    return build('gmail', 'v1', credentials=creds)

def send_email(service, sender, recipient, subject, body):
    # Create the email message
    message = MIMEText(body)
    message['to'] = recipient
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send the email
    message = {'raw': raw_message}
    try:
        send_message = service.users().messages().send(
            userId="me", body=message).execute()
        print(f"Message sent: {send_message['id']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Authenticate and send the email
    gmail_service = authenticate_gmail()
    send_email(
        service=gmail_service,
        sender="your_email@gmail.com",
        recipient="recipient_email@gmail.com",
        subject="Hello from Gmail API",
        body="This is a test email sent using the Gmail API."
    )
