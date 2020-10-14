from Google import Create_Service
from getmac import get_mac_address as gma

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)
folder_name = [gma()]

file_metadata = {
    'name': folder_name,
    'mimeType': 'application/vnd.google-apps.folder'
}

file = service.files().create(body=file_metadata,
                              fields='id').execute()
