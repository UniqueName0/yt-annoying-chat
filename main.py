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
        if str(msg) == "!move mouse" or str(msg) == "!mm":
            mouse.move(100, 100)
        if str(msg) == "!spam jump" or str(msg) == "!sj":
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
            time.sleep(0.2)
            keyboard.type("w")
        if str(msg) == "!move left" or str(msg) == "!ml":
            keyboard.press("a")
            time.sleep(5)
            keyboard.release("a")
        if str(msg) == "!move right" or str(msg) == "!mr":
            keyboard.press("d")
            time.sleep(5)
            keyboard.release("d")
        if str(msg) == "!move down" or str(msg) == "!md":
            keyboard.press("s")
            time.sleep(5)
            keyboard.release("s")
        if str(msg) == "!spam skills" or str(msg) == "!ss":
            keyboard.type("./'")
            keyboard.type("'")
            keyboard.type(".")
        if str(msg) == "!spam top skill" or str(msg) == "!st":
            keyboard.type("'")
        if str(msg) == "!spam middle skill" or str(msg) == "!sm":
            keyboard.type(".")
        if str(msg) == "!spam bottom skill" or str(msg) == "!sb":
            keyboard.type("/")
        if str(msg) == "!spam attack" or str(msg) == "!sa":
            keyboard.press(Key.shift)
            time.sleep(5)
            keyboard.release(Key.shift)
        if str(msg) == "!spam stats" or str(msg) == "!sst":
            keyboard.type("=")
            time.sleep(0.2)
            keyboard.type("=")
            time.sleep(0.2)
            keyboard.type("=")
            time.sleep(0.2)
            keyboard.type("=")
            time.sleep(0.2)
            keyboard.type("=")
            time.sleep(0.2)
            keyboard.type("=")
        if str(msg) == "!close shop" or str(msg) == "!cs":
            mouse.click(Button.right)
        if str(msg) == "!open shop" or str(msg) == "!os":
            keyboard.type("/")


try:
    chat_obj.start()
    chat_obj.subscribe_chat_message(respond)
    chat_obj.join()

finally:
    chat_obj.stop()
