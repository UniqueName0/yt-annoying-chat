import time
import pynput
from youtubechat import YoutubeLiveChat, get_live_chat_id_for_stream_now
import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as Con
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyscreenshot as ImageGrab


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

livechat_id = get_live_chat_id_for_stream_now("oauth_creds")
chat_obj = YoutubeLiveChat("oauth_creds", [livechat_id])
mouse = Controller()
keyboard = Con()

def respond(msgs, chatid):
    for msg in msgs:
        if str(msg) == "!stop" and msg.authorDetails.isChatModerator == True:
            chat_obj.send_message("stopping", chatid)
            exit()
        if str(msg) == "!move mouse":
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
            mouse.move(10, 10)
        if str(msg) == "!spam jump":
            keyboard.type("w")
            time.sleep(0.1)
            keyboard.type("w")
            time.sleep(0.1)
            keyboard.type("w")
            time.sleep(0.1)
            keyboard.type("w")
            time.sleep(0.1)
            keyboard.type("w")
            time.sleep(0.1)
            keyboard.type("w")
        if str(msg) == "!move left":
            keyboard.press("a")
            time.sleep(1)
            keyboard.release("a")
        if str(msg) == "!move right":
            keyboard.press("d")
            time.sleep(1)
            keyboard.release("d")
        if str(msg) == "!move down":
            keyboard.press("s")
            time.sleep(1)
            keyboard.release("s")
        if str(msg) == "!spam skills":
            keyboard.type("./'")
        if str(msg) == "!spam top skill":
            keyboard.type("'")
        if str(msg) == "!spam middle skill":
            keyboard.type(".")
        if str(msg) == "!spam bottom skill":
            keyboard.type("/")
        if str(msg) == "!spam attack":
            keyboard.press(Key.shift)
            time.sleep(2)
            keyboard.release(Key.shift)
        if str(msg) == "!spam stats":
            keyboard.type("*")
            time.sleep(0.1)
            keyboard.type("*")
            time.sleep(0.1)
            keyboard.type("*")
            time.sleep(0.1)
            keyboard.type("*")
            time.sleep(0.1)
            keyboard.type("*")
            time.sleep(0.1)
            keyboard.type("*")
        if str(msg) == "!close shop":
            mouse.click(Button.right)
        if str(msg) == "!open shop":
            keyboard.type("////////")


try:
    chat_obj.start()
    chat_obj.subscribe_chat_message(respond)
    chat_obj.join()

finally:
    chat_obj.stop()
