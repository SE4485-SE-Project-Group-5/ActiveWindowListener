from datetime import datetime, timedelta

from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

from apis.mongo.mongo_client import log_event, log_processes
from apis.monitoring_details.win32_window_details import active_window_process, all_open_windows

# logging.basicConfig(filename="../window_log.txt", level=logging.DEBUG, format='%(message)s')

MOUSE_MOVE = "MOUSE_MOVE"
MOUSE_CLICK = "MOUSE_CLICK"
MOUSE_SCROLL = "MOUSE_SCROLL"
KEYBOARD_RELEASE = "KEYBOARD_RELEASE"
KEYBOARD_PRESS = "KEYBOARD_PRESS"

event_types = {
    KEYBOARD_PRESS: 0,
    KEYBOARD_RELEASE: 1,
    MOUSE_MOVE: 2,
    MOUSE_CLICK: 3,
    MOUSE_SCROLL: 4,
}

current_event_type = None
prev_event_type = None
active_window_details = None
active_windows = []
last_time = datetime.utcnow()
min_log_frequency = timedelta(seconds=2)


def set_event_type(event_type_input):
    global current_event_type
    global last_time

    # Determine cause of this event
    current_event_type = event_types[event_type_input]
    # Do not log if not enough time since last log has elapsed
    if last_time + min_log_frequency <= datetime.utcnow():
        # Active window details - what is in the foreground
        payload = active_window_process()
        if payload is not None:  # This fails sometimes...
            payload['event_type'] = event_type_input
            log_event(payload)
        # All window details - what is open on the system
        log_processes(all_open_windows())
        # Update last time a log was made
        last_time = datetime.utcnow()


def on_press(key):
    # t = Thread(target=set_event_type, args=(KEYBOARD_PRESS,))
    # t.start()
    set_event_type(KEYBOARD_PRESS)
    # print("ON PRESS:", datetime.utcnow())
    # log_event(active_window_process())
    # logging.info("Key Press: " + str(key))
    # print("Key Press: " + str(key))


def on_release(key):
    # t = Thread(target=set_event_type, args=(KEYBOARD_RELEASE,))
    # t.start()
    set_event_type(KEYBOARD_RELEASE)
    # print("ON RELEASE:", datetime.utcnow())
    # logging.info("Key Press: " + str(key))
    # print("Key Press: " + str(key))


def on_move(x, y):
    pass
    # t = Thread(target=set_event_type, args=(MOUSE_MOVE,))
    # t.start()
    set_event_type(MOUSE_MOVE)
    # print("ON MOVE:", datetime.utcnow())
    # log_event(active_window_process())
    # time.sleep(5)
    # logging.info("Mouse moved to ({0}, {1})".format(x, y))
    # print("Mouse moved to ({0}, {1})".format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        # t = Thread(target=set_event_type, args=(MOUSE_CLICK,))
        # t.start()
        set_event_type(MOUSE_CLICK)
        # print("ON CLICK:", datetime.utcnow())
        # log_event(active_window_process())
        # logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        # print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))


def on_scroll(x, y, dx, dy):
    # t = Thread(target=set_event_type, args=(MOUSE_SCROLL,))
    # t.start()
    set_event_type(MOUSE_SCROLL)
    # print("ON SCROLL:", datetime.utcnow())
    # log_event(active_window_process())
    # logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    # print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


def start_listeners():
    with MouseListener(on_click=on_click, on_scroll=on_scroll, on_move=on_move) as m_listener:
        with KeyboardListener(on_press=on_press, on_release=on_release) as k_listener:
            m_listener.join()
            k_listener.join()


if __name__ == '__main__':
    start_listeners()
