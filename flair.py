import platform
import time
from http.client import HTTPConnection
from threading import Thread
from getmac import get_mac_address as gma
import requests
import json
import apis.google_drive.Google as Google
import apis.google_drive.Create_Folders as create_folder
import apis.google_drive.Upload_Files as Upload
import webview

from apis.input_methods.mouse_and_keyboard_listener import start_listeners
from app import run_app

error = False
status = False
port = 43968

operating_system = str(platform.system()).lower()

CLIENT_SECRET_FILE = "C:/Users/Taylor/Desktop/ActiveWindowListener/apis/google_drive/credentials.json"
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']
folder_name = [gma()]
query_str = '(mimeType = \'application/vnd.google-apps.folder\') and (name = \'{0}\')'.format(folder_name)
folder_id = Upload.search(query_str)

service = Google.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)


def folder_exists():
    access_token = 'token'
    url = 'https://www.googleapis.com/drive/v3/files'
    headers = {'Authorization': 'Bearer ' + access_token}
    query = {'q': "id='" + folder_id + "' and mimeType='application/vnd.google-apps.folder'"}
    response = requests.get(url, headers=headers, params=query)
    obj = response.json()
    if obj['files']:
        return true
    else:
        return false


def get_user_agent(window):
    result = window.evaluate_js(r"""
        // Return user agent
        'User agent:\n' + navigator.userAgent;
        """)
    print(result)


def is_server_running(url, max_wait):
    global error
    global status
    global port

    time.sleep(0.4)
    start = time.time()
    while True:
        try:
            end = time.time()
            if end - start > max_wait:
                return False
            time.sleep(0.1)
            connection = HTTPConnection(url, port)
            request, response = connection.request(
                "GET", "/"), connection.getresponse()
            if response is not None:
                status = response.status
                return True
        except Exception as e:
            error = e
            print("Server not yet running")


def main():
    global port

    if folder_exists():
        print("Exists")
    else:
        create_folder.create_folders()
        print("DNE")

    url, max_wait = 'localhost', 90  # 15 seconds
    link = "http://" + url + ":" + str(port)
    # Starting Server
    t = Thread(target=start_listeners, args=())
    t.daemon = True
    t.start()
    print("Listeners started")
    server_thread = Thread(target=run_app, args=(url, port))
    server_thread.daemon = True
    server_thread.start()
    # Waiting for server to load content
    if is_server_running(url, max_wait):
        print("Server started")
        # webbrowser.open(link, new=2)
        # while server_thread.is_alive():
        #     time.sleep(0.1)
        window = webview.create_window(
            "Flair App", link, width=1000, height=522)
        # If you want to inspect element just go to localhost url in browser
        webview.start(get_user_agent, window, debug=True)
    else:
        print("Server failed to start with a max wait time of " + str(max_wait))
        if status is not False:
            print("Status was " + str(status))
        if error is not False:
            print("Exception was " + str(error))
    print("Server has exited")


if __name__ == '__main__':
    main()
