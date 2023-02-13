from bad_apple import frames
from playsound import playsound
import os
import time
import threading

audio_file = os.path.join(os.getcwd(), 'assets', 'bad_apple.wav')
delay = 0.01549  # 1000 / 60 -> 16.66 ms -> 0.01666 sec -> 0.01549 sec (sync)

threading.Thread(
    target=playsound,
    args=(audio_file,),
    daemon=True
).start()

for frame in frames:
    print(frame, end='')
    time.sleep(delay)
