import time
import subprocess
import os
import webbrowser

os.environ["DISPLAY"] = ":0"


while (True):
    try:

        libcamera_process = subprocess.Popen(
            "libcamera-hello -t 0 -f --shutter 400 --framerate 2 -f --brightness 0.3", shell=True)

        os.system("ps -C chromium-browser -o pid=|xargs kill -9")

        time.sleep(10)

        os.system("ps -C libcamera-hello -o pid=|xargs kill -9")

        time.sleep(3)

        image_process = subprocess.Popen(
            "libcamera-still -o test.jpg  --shutter 400 --brightness 0.3  -n --immediate", shell=True)

        time.sleep(3)

        webbrowser.open('test.jpg', new=0, autoraise=True)

        time.sleep(10)

    except:

        print("Error")
        time.sleep(5)
        continue
