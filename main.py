import time
from threading import Thread
import logging

from pynput.keyboard import Key, Controller

import win32gui

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

logger = logging.getLogger("AutoSave BG3")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger.info('Starting watch every 2 minutes for the baldurgate')

    keyboard = Controller()

    while True:
        w = win32gui
        window_name = w.GetWindowText(w.GetForegroundWindow())
        logger.info(f'Active Window is : {window_name}')
        if "Baldur's Gate 3" in window_name:
            logger.info('is bg3')
            keyboard.press(Key.f5)
            time.sleep(0.5)
            keyboard.release(Key.f5)

            logger.info('save_done')
        time.sleep(120)

