# from __future__ import print_function
# import os.path
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

# # Scope for modifying and deleting emails

# SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# def authenticate_gmail():
#     """Authenticate and return Gmail API service object."""
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=8080, access_type='offline', prompt='consent')

#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#     return build('gmail', 'v1', credentials=creds)

# def delete_promotions():
#     service = authenticate_gmail()

#     # Search query for promotions category
#     query = 'category:promotions'

#     # Get the list of messages
#     results = service.users().messages().list(userId='me', q=query).execute()
#     messages = results.get('messages', [])

#     if not messages:
#         print("No promotions emails found.")
#         return

#     # Extract IDs
#     message_ids = [msg['id'] for msg in messages]
#     if not message_ids:
#         print("No promotions emails found.")
#         return
#     else:
#         print(message_ids[0:5])  # Print first 5 IDs for verification
#         print(f"Found {len(message_ids)} promotions emails.")

#     # Batch delete
#     service.users().messages().batchDelete(
#         userId='me',
#         body={'ids': message_ids}
#     ).execute()

#     print(f"Deleted {len(message_ids)} promotions emails.")

# if __name__ == '__main__':
#     delete_promotions()




from __future__ import print_function
import os.path
import pickle
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scope — modify Gmail
SCOPES = ["https://mail.google.com/"]

def authenticate_gmail():
    creds = None
    # Token file stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If no valid creds, prompt login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)  # Web redirect
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def delete_promotions():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    # Search for promotional emails
    results = service.users().messages().list(userId='me', q='category:social').execute()
    messages = results.get('messages', [])

    if not messages:
        print("No promotional emails found.")
        return

    for msg in messages:
        try:
            service.users().messages().delete(userId='me', id=msg['id']).execute()
            print(f"Deleted email ID: {msg['id']}")
        except Exception as e:
            print(f"Error deleting {msg['id']}: {e}")

if __name__ == '__main__':
    # Remove token.json before first run if scopes changed
    for i in range(50):
        delete_promotions()
