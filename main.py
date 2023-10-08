import os
from os import system
import threading
import time
from pynput import keyboard
from pathlib import Path

#logging
def log(message):
    f = open(Path(__file__).with_name('logfile.txt'), 'a')
    f.write(f"{time.time()} : {message}\n")
    f.close()

#Thread managing
stop_threads = False

def uiCycle():
    while True:
        build_actionWindow()
        global stop_threads
        if stop_threads:
            break

#console interaction

current_option = 1
entered_id = -1

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def on_press(key):
        global current_option
        global entered_id
        if key == keyboard.Key.up:
            if current_option >= 0:
                current_option-=1
            else:
                current_option=len(row)-1
        if key == keyboard.Key.down:
            if current_option < len(row)-1:
                current_option+=1
            else:
                current_option=0
        if key == keyboard.Key.enter:
            log("user input : enter")
            entered_id = current_option
            global listener
            listener.stop()
            log(f"entered id is : {entered_id}")
        return True
#UI managment
#Build the "UI"


current_animation = []
interaction_Options = {}

selected = ">"
unselected = " "

row = ["play","refill water","feed","pet"]

interaction_Options["play"] = unselected
interaction_Options["refill water"] = unselected
interaction_Options["feed"] = unselected
interaction_Options["pet"] = unselected


def build_actionWindow():
    mendetoryBackspaces = 5

    global c1
    global current_animation

    for c in current_animation:
        print(c)
        leftBackspaces = mendetoryBackspaces - c.count('\n')
        print('\n' * leftBackspaces)
        print("---------------------------------------")

        build_interactionWindow()
        time.sleep(0.4)
        cls()

def build_interactionWindow():
    global interaction_Options
    global row
    global current_option
    for key in interaction_Options:
        interaction_Options[key] = unselected
    interaction_Options[row[current_option]] = selected

    for key in interaction_Options:
         print(f"{interaction_Options[key]} {key}")
    print("---------------------------------------\n")



#Creature handling
class cat:
    name = ''
    health = 100
    hunger = 0
    thirst = 0
    anims={}

    anims['play']=[
        '''
_._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-'
    ''',
    '''
_._     _,-'""`-._
\--.`._,'(       |\`-/|
    `..-' \ )-`( , O O)
          `-    \`_`"'-'
    ''',
        '''
_._     _,-'""`-._
\--.`._,'(       |\`-/|
    `..-' \ )-`( , O O)
          `-    \`_`"'-'
    '''
    ]
    anims['sleep']=[
        '''
 \t\t
 \t\t       
 \t\t|\__/,|   (`\\
 \t\t|_ _  |.--.) )
 \t\t( T   )     /
 \t\t(((^_(((/(((_/
        ''',
'''
 \t\t
 \t\t       Z
 \t\t|\__/,|   (`\\
 \t\t|_ _  |.--.) )
 \t\t( T   )     /
 \t\t(((^_(((/(((_/
        ''',
'''
 \t\t         Z
 \t\t       Z
 \t\t|\__/,|   (`\\
 \t\t|_ _  |.--.) )
 \t\t( T   )     /
 \t\t(((^_(((/(((_/
        '''
    ]
    anims['feed']=[
        '''
                   _ |\_
                   \` ..\\
              __,.-" =__Y=
            ."        )
      _    /   ,    \/\_
     ((____|    )_-\ \_-`========
     `-----'`-----` `--`  =====
        ''',
                '''
                   _ |\_
                   \` ..\\
              __,.-" =__Y=
            ."        ) \\\\
      _    /   ,    \/\_
     ((____|    )_-\ \_-`========
     `-----'`-----` `--`  =====
        ''',
                '''
                   _ |\_
                   \` ..\\
              __,.-" =__Y=
            ."        ) \\\\
      _    /   ,    \/\_ \\\\
     ((____|    )_-\ \_-`========
     `-----'`-----` `--`  =====
        ''',
                '''
                   _ |\_
                   \` ..\\
              __,.-" =__Y=
            ."        ) \\\\
      _    /   ,    \/\_
     ((____|    )_-\ \_-`========
     `-----'`-----` `--`  =====
        '''
    ]
    def __init__(self, name):
        self.name = name

#------------------PROGRAM----------------------------

#resize window size
system('mode con: cols=40 lines=18')


c1 = cat("Sigi")
current_animation = c1.anims['feed']



t1 = threading.Thread(target=uiCycle)
t1.start()


#Statemaschine
while True:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        log("stopped listener")
    
    if entered_id == -1:
        log("Entering idle state")
        #idle
        ...
    elif entered_id == 0:
        log("Entering play state")
        current_animation = c1.anims['play']

        ...
    elif entered_id == 1:
        ...
    elif entered_id == 2:
        ...
    elif entered_id == 3:
        ...
    elif entered_id == 4:
        ...