from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import time

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

time_stamp = time.strftime("%H-%M-%S")
time_stamp = "".join((time_stamp, ".json"))

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)
folder_id = '1GcpKEx5oRo4kZJey_092uP0I6SM1ST0N'
file_name = 'mongo.server.log.json'
mime_type = 'application/json'

file_metadata = {
    'name': file_name,
    'parents': [folder_id]
}
media = MediaFileUpload('C:/Users/Taylor/Desktop/ActiveWindowListener/mongo/{0}'.format(file_name),
                        mimetype=mime_type)

service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()
