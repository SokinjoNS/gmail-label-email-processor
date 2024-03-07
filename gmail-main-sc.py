from gmail_api_auth import authenticate_gmail_api
from gmail_label_manager import get_label_id_by_name
from gmail_message_processor import fetch_emails_by_label
from data_exporter import export_emails_to_csv
from googleapiclient.discovery import build

def extract_email_addresses(messages, service):
    email_addresses = []
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        headers = msg['payload']['headers']
        for header in headers:
            if header['name'] in ['To', 'Cc', 'Bcc']:
                emails = header['value'].split(',')
                for email in emails:
                    email_addresses.append(email.strip())
    return list(set(email_addresses))  # Remove duplicates

def main():
    label_name = "YOUR_LABEL_NAME_HERE"  # Change this to your specific label
    creds = authenticate_gmail_api()
    service = build('gmail', 'v1', credentials=creds)

    label_id = get_label_id_by_name(label_name)
    if not label_id:
        print(f'Label "{label_name}" not found.')
        return

    print(f'Fetching emails for label: {label_name}')
    messages = fetch_emails_by_label(label_name)
    if not messages:
        print('No messages found.')
        return

    email_addresses = extract_email_addresses(messages, service)
    if not email_addresses:
        print('No email addresses found.')
        return

    # Specify the file path where you want to export the emails
    export_file_path = 'email_list.csv'
    export_emails_to_csv(email_addresses, export_file_path)
    print(f'Email addresses exported to {export_file_path}')

if __name__ == '__main__':
    main()
