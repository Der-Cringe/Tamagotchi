import os
from os import system
import threading
import time
from pynput import keyboard

stop_threads = False
current_animation = []

current_option = 1

interaction_Options = {}

selected = ">"
unselected = " "

row = ["play","refill water","feed","pet"]

interaction_Options["play"] = unselected
interaction_Options["refill water"] = unselected
interaction_Options["feed"] = unselected
interaction_Options["pet"] = unselected

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def on_press(key):
        global current_option
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

#Build the "UI"
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

    anims['playing']=[
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
    anims['sleeping']=[
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
#Thread managing
def uiCycle():
    while True:
        build_actionWindow()
        global stop_threads
        if stop_threads:
            break

system('mode con: cols=40 lines=18')

c1 = cat("Sigi")
current_animation = c1.anims['feed']



t1 = threading.Thread(target=uiCycle)
t1.start()



with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
while True:
    if current_animation == "play":
        current_animation = c1.anims['play']
    elif current_animation == "feed":
        current_animation = c1.anims['feed']
        if c1.hunger > 0:
            hunger-=5
        if c1.hunger < 0:
            hunger = 0
        time.sleep(2)
        current_animation = "idle"
    elif current_animation == "idle":
        ...