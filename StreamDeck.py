from StreamDeckFunctions import * #import functions from functions file
#import StreamDeckFunctions
current_switch0_state = True #set this as the primary dekstop environment

#create_desktop_environments() #create a desktop environment

while True: #always:

    #button 0 is Alt+Tab
    if btn0.value: #if button1 pressed then print a message and press ALT+TAB
        #print("Alt+Tab - Toggled") #print message
        keyboard.send(Keycode.ALT, Keycode.TAB) #send the keycodes
        time.sleep(0.25)

    if btn1.value: #Ctrl+Shift+F10 for ptt
        LED1.value = True
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.F10) #send the keycodes
    
        if not btn1.value:
            LED1.value = False
            keyboard.release(Keycode.CONTROL, Keycode.SHIFT, Keycode.F10) #send the keycodes


        
        
    #button 2 is ?
    if btn2.value:
        #print("Discord Deafen - Toggled") #print message
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F11) #send the keycodes
        time.sleep(0.25)
        toggle(LED2) #turn OFF LED2
        
    #button 3 is Ctrl+Shift+F1 (Discord Streamer Mode)
    if btn3.value:
        #print("Mute For Discord - Toggled") #print message
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F12)
        time.sleep(0.25)
        toggle(LED3) #toggle the LED

        
    #button 4 is Push To Talk in Discord (Ctrl+Shift+F3)
    if btn4.value:
        #print("Discord Streamer Mode - Toggled") #print message
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F1)
        time.sleep(0.1)
        toggle(LED4) #toggle the LED
        
    
    #if switch has changed position
    if switch0.value != current_switch0_state: 
        if switch1.value: #if switch in the '0' position switch to the primary desktop environment
            #print("Environment Set To Primary") #print message
            flash_all()
            keyboard.send(Keycode.CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW)
            current_switch0_state = False
            time.sleep(0.25)
            
        if switch0.value: #if switch in the '1' position switch to the secondary desktop environment
            #print("Environment Set To Secondary") #print message
            flash_all()
            keyboard.send(Keycode.CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW)
            current_switch0_state = True
            time.sleep(0.25)        
        
    time.sleep(0.1)
    
    
#make a on-exit script to delete the desktop environments