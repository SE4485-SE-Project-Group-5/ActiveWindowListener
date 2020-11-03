import apis.google_drive.Google as Google
from getmac import get_mac_address as gma
# import importlib.util
# spec = importlib.util.spec_from_file_location("Google", "C:/Users/Taylor/Desktop/ActiveWindowListener/apis"
#                                                         "/google_drive/Google.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
#foo.Google()

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

# service = foo.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)
service = Google.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)
folder_name = [gma()]


def create_folders():
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    file = service.files().create(body=file_metadata,
                                  fields='id').execute()


create_folders()