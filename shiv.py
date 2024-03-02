import os

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'

FOLDER_MAPPING = {
    "C:\\Users\\falcon\\Desktop\\S-Rover\\source\\annulus_ring_strips": "1XAztJV-V2-3ZG9OLceJm3Q53xLj22IdY",
    "C:\\Users\\falcon\\Desktop\\S-Rover\\source\\color_maps": "1kcNgA5bqmnlwOvYy-ljsYRdVl9MFCjJA",
    "C:\\Users\\falcon\\Desktop\\S-Rover\\source\\mapped_annulus": "1Qepap7ch6bX0RDAcl6RaoEHM66H6toXg",
    "C:\\Users\\falcon\\Desktop\\S-Rover\\source\\maps": "17oLJ6_A4pBiurB0jR11NZXxv9bDIwkWL",
    "C:\\Users\\falcon\\Desktop\\S-Rover\\source\\rectangular_strips": "18TAgAJptoQNfGM3GBbO65xU6YwpWXcFH"
}

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_files(local_folder, drive_folder_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    if os.path.isdir(local_folder):
        for filename in os.listdir(local_folder):
            file_full_path = os.path.join(local_folder, filename)
            if os.path.isfile(file_full_path):
                file_metadata = {
                    'name': filename,
                    'parents': [drive_folder_id]
                }
                media = MediaFileUpload(file_full_path)
                file = service.files().create(
                    body=file_metadata,
                    media_body=media
                ).execute()
                print(f'Uploaded {filename}')
    else:
        print(f'{local_folder} is not a directory')

for local_folder, drive_folder_id in FOLDER_MAPPING.items():
    upload_files(local_folder, drive_folder_id)
