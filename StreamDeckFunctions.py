#imports
import time
import digitalio
import board

#hid imports
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#declare what interface the usb_hid connectoin is
keyboard = Keyboard(usb_hid.devices)

#set pin variables
btn1_pin = board.GP14
btn2_pin = board.GP13
btn3_pin = board.GP12
btn4_pin = board.GP11
btn0_pin = board.GP10

#set pins
btn1 = digitalio.DigitalInOut(btn1_pin)
btn2 = digitalio.DigitalInOut(btn2_pin)
btn3 = digitalio.DigitalInOut(btn3_pin)
btn4 = digitalio.DigitalInOut(btn4_pin)
btn0 = digitalio.DigitalInOut(btn0_pin)

#set to be inputs
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn3.direction = digitalio.Direction.INPUT
btn4.direction = digitalio.Direction.INPUT
btn0.direction = digitalio.Direction.INPUT

#set to be normally Flase, when pressed == True
btn1.pull = digitalio.Pull.DOWN
btn2.pull = digitalio.Pull.DOWN
btn3.pull = digitalio.Pull.DOWN
btn4.pull = digitalio.Pull.DOWN
btn0.pull = digitalio.Pull.DOWN


switch1_pin = board.GP9
switch0_pin = board.GP8

switch1 = digitalio.DigitalInOut(switch1_pin)
switch0 = digitalio.DigitalInOut(switch0_pin)

switch1.direction = digitalio.Direction.INPUT
switch0.direction = digitalio.Direction.INPUT

switch1.pull = digitalio.Pull.DOWN
switch0.pull = digitalio.Pull.DOWN

#set pin variables
LED1_pin = board.GP16
LED2_pin = board.GP17
LED3_pin = board.GP18
LED4_pin = board.GP19

#set pins
LED1 = digitalio.DigitalInOut(LED1_pin)
LED2 = digitalio.DigitalInOut(LED2_pin)
LED3 = digitalio.DigitalInOut(LED3_pin)
LED4 = digitalio.DigitalInOut(LED4_pin)

#set as outputs
LED1.direction = digitalio.Direction.OUTPUT
LED2.direction = digitalio.Direction.OUTPUT
LED3.direction = digitalio.Direction.OUTPUT
LED4.direction = digitalio.Direction.OUTPUT

    

def Only_LED1ON():
    LED1.value = True
    LED2.value = False
    LED3.value = False
    LED4.value = False
    
def Only_LED2ON():
    LED1.value = False
    LED2.value = True
    LED3.value = False
    LED4.value = False
    
def Only_LED3ON():
    LED1.value = False
    LED2.value = False
    LED3.value = True
    LED4.value = False
    
def Only_LED4ON():
    LED1.value = False
    LED2.value = False
    LED3.value = False
    LED4.value = True

def all_LEDS_off():
    LED1.value = False
    LED2.value = False
    LED3.value = False
    LED4.value = False
    
def toggle_all():
    toggle(LED1)
    toggle(LED2)
    toggle(LED3)
    toggle(LED4)
    
def flash_all():
    toggle(LED1)
    toggle(LED2)
    toggle(LED3)
    toggle(LED4)
    time.sleep(0.5)
    toggle(LED1)
    toggle(LED2)
    toggle(LED3)
    toggle(LED4)

def toggle(input):
    if input.value == True:
        input.value = False
    elif input.value == False:
        input.value = True

def toggle_discord_streamer_mode():
    keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F1)
    time.sleep(0.25)
    toggle(LED3)

def create_desktop_environments():
    keyboard.send(Keycode.CONTROL, Keycode.WINDOWS, Keycode.D) #create new desktop environment
    keyboard.send(Keycode.CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW) #switch back to primary environment