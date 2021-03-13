from StreamDeckFunctions import *

current_switch0_state = True

create_desktop_environments()
while True:
    #button 1 is Alt+Tab
    if btn1.value:
        print("Alt+Tab - Toggled")
        toggle(LED1) #turn ON LED1
        keyboard.press(Keycode.ALT, Keycode.TAB)
        time.sleep(0.25)
        keyboard.release(Keycode.ALT, Keycode.TAB)
        toggle(LED1) #turn OFF LED2
        
    #button 2 is Windows Key
    if btn2.value:
        print("Windows Menu - Toggled")
        toggle(LED2) #turn ON LED2
        keyboard.send(Keycode.WINDOWS)
        time.sleep(0.25)
        toggle(LED2) #turn OFF LED2
        
    #button 3 is Ctrl+Shift+F1 (Discord Streamer Mode)
    if btn3.value:
        print("Discord Streamer Mode - Toggled")
        toggle_discord_streamer_mode()
        time.sleep(0.25)
        
    #button 4 is
    if btn4.value:
        print("button 4 toggled")
        toggle(LED4)
        time.sleep(0.25)
        
    #button 0 is Windows Key + D (Desktop)
    if btn0.value:
        print("Desktop - Toggled")
        toggle_all()
        keyboard.press(Keycode.WINDOWS, Keycode.D)
        time.sleep(0.25)
        keyboard.release(Keycode.WINDOWS, Keycode.D)
        toggle_all()
    
    #if switch has changed position
    if switch0.value != current_switch0_state: 
        if switch1.value: #if switch in the '0' position switch to the primary desktop environment
            print("Environment Set To Primary")
            flash_all()
            keyboard.send(Keycode.CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW)
            current_switch0_state = False
            time.sleep(0.25)
            
        if switch0.value: #if switch in the '1' position switch to the secondary desktop environment
            print("Environment Set To Secondary")
            flash_all()
            keyboard.send(Keycode.CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW)
            current_switch0_state = True
            time.sleep(0.25)
        
        
    time.sleep(0.1)