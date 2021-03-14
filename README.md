# Pico Streaming Deck

## To Use:
- Hold down the `bootsel` button and plug in your Pico (to a computer) - this will then show as a Usb storage device, 
- Copy the `.uf2` file onto tis device. It should unmount itself,
- Then go into your ide [(I recommended thonny)](https://www.raspberrypi.org/documentation/pico/getting-started/)
- Then open the .py files, and save them to the board.
- ***OPTIONAL*** - If you want you can rename the `StreamDeck.py` to `code.py` to make it run on boot
- Now you have the streaming deck code.


## Circuit Diagram:
- Create a circuitboard like this.
- Feel free to interchange buttons for mechanical keyboard keys.
- Have fun and make it yours! (Maybe make a case?)
![Pico-StreamDeck Ciruit Diagram](Pico-StreamDeck(Labelled).jpg)


## Explanation:
You can change the code to whatever you want [This will be useful](https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py) but this is what the defaults are:
- The switch moves between desktop environments (`Ctrl+Win+D/Left_Arrow/Right_Arrow`) & flashes the LED's - To see what desktop envrionments you have Press `Win+Tab`
- Button0 (the furthest Left on the diagram) moves to desktop (`Win+D`) & flashes the LED's
- Button1 moves between windows - (`Alt+Tab`)
- Button2 opens the Program Menu (`Win`)
- Button3 turns on streamer mode in Discord (`Ctrl+Shift+F1`) - You will need to set this custom shortcut in Discord for this to work
- Button4 currently does nothing.


## With Thanks To:
[JBDynamics for providing the Pico library for Eagle](https://www.raspberrypi.org/forums/viewtopic.php?t=302397#p1814462)
[Here is a direct download link](https://www.raspberrypi.org/forums/download/file.php?id=44669)



