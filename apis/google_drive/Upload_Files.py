from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from getmac import get_mac_address as gma
import time

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

time_stamp = time.strftime("%H-%M-%S")
time_stamp = "".join((time_stamp, ".json"))

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)


def search(query):
    page_token = None
    while True:
        response = service.files().list(
            q=query,
            spaces=API_NAME,
            fields='nextPageToken, files(id, name)',
            pageToken=page_token
        ).execute()

        for file in response.get('files', []):
            return file.get('id')

        page_token = response.get('nextPageToken', None)

        if page_token is None:
            break


def upload():
    folder_name = gma()
    query_str = '(mimeType = \'application/vnd.google-apps.folder\') and (name = \'{0}\')'.format(folder_name)
    folder_id = search(query_str)
    file_names = ['mongo.server.log.json']
    mime_types = ['application/json']

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

    media = MediaFileUpload('C:/Users/Taylor/Desktop/ActiveWindowListener/mongo/{0}'.format(file_name),
                            mimetype=mime_type)

    return service.files().create(
        body=file_metadata,
        media_body=media,
        fields='name'
    ).execute()


upload()
