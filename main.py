import time
import logging

from pynput.keyboard import Key, Controller

import win32gui

###
# Setting Statics Values
###
_TIMER_WAIT = 120
_KEY_RELEASE_WAIT_TIME = 0.5
_BG3_NAME_PATTERN = "Baldur's Gate 3"


###
# Setting logger
###
logger = logging.getLogger("AutoSave BG3")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Running the main code.
if __name__ == '__main__':
    logger.info('Starting watch every 2 minutes for the Baldur Gate')

    # Creating keyboard for sending key presses.
    keyboard = Controller()

    while True:
        w = win32gui
        # we get the active window name so  we can know if we are actively playing;
        # so we dont send f5 to random windows.
        window_name = w.GetWindowText(w.GetForegroundWindow())

        # could be done with regex; but since the name is straightfoward might has keep it simple.
        if _BG3_NAME_PATTERN in window_name:
            logger.info(f"Active Window is : '{window_name}'. Is bg3 so sending F5")
            keyboard.press(Key.f5)
            # we have to wait 500ms or so for the pres/release to be catched properly by the game
            # if we press/release between 2 frames
            time.sleep(_KEY_RELEASE_WAIT_TIME)
            keyboard.release(Key.f5)

            logger.info('Save done!')
        else:
            logger.info(f"Active Window is : '{window_name}'. Is Not BG3 so skipping sending key")
        # we wait some time before saving again.
        time.sleep(_TIMER_WAIT)

