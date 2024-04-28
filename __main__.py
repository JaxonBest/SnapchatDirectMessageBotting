import pyautogui as pag
import time
import pynput

positions = []

def run_process():
    print('sending snap')
    while True:
        for pos in positions:
            pag.leftClick(pos.x, pos.y)
            print('pressed at %s' % str(pos))
            time.sleep(0.5)
        time.sleep(0.5)

def on_press(key):
    if (key == pynput.keyboard.Key.shift):
        print(len(positions))
        pos = pag.position()
        positions.append(pos)
        print('Position Captured (%s)' % str(pos))
    
    if (key == pynput.keyboard.Key.esc):
        print('Starting in 5 secs..')
        time.sleep(5)
        run_process()
        return
    


with pynput.keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()