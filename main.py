import os
from os import system
import threading
import time
from pynput import keyboard
from pathlib import Path

#logging
#since multi-threading with multiple gameloop is difficult to handle, a log is written for debugging purposes
def log(message):
    f = open(Path(__file__).with_name('logfile.txt'), 'a')
    f.write(f"Timestamp({time.time()})=>{message}\n")
    f.close()

#Thread managing
stop_threads = False
#this thread is responsible for the trading of the ui display.
# The ui of the creature and that of the action window are built in different functions

def uiCycle():
    while True:
        build_actionWindow()
        manage_values()
        global stop_threads
        if stop_threads:
            break


#background management
def manage_values():
    global c1
    ...



#console interaction

current_option = 1 #current_option contains the current id to which the arrow: > points.
entered_id = -1#entered_id is overwritten with the current_option when enter is pressed

#to always display an updated variant, the console must be cleared beforehand
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

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
    build_statusWindow()

def calc_line(value):
    dotValue = int(value/10)
    return dotValue

def build_statusWindow():
    global c1
    if calc_line(c1.health) < 5:
        print(f"\tHealth:{colors.fg.orange}{'-'*calc_line(c1.health)}{' '*(10-calc_line(c1.health))}{colors.reset}{c1.health}%\n")    
    else:
        print(f"\tHealth:{colors.fg.green}{'-'*calc_line(c1.health)}{' '*(10-calc_line(c1.health))}{colors.reset}{c1.health}%\n")    

    if calc_line(c1.hunger) > 5:
        print(f"\tHunger:{colors.fg.orange}{'-'*calc_line(c1.hunger)}{' '*(10-calc_line(c1.hunger))}{colors.reset}{c1.hunger}%\n")    
    else:
        print(f"\tHunger:{colors.fg.green}{'-'*calc_line(c1.hunger)}{' '*(10-calc_line(c1.hunger))}{colors.reset}{c1.hunger}%\n")    
 
    if calc_line(c1.thirst) > 5:
        print(f"\tThirst:{colors.fg.orange}{'-'*calc_line(c1.thirst)}{' '*(10-calc_line(c1.thirst))}{colors.reset}{c1.thirst}%\n")    
    else:
        print(f"\tThirst:{colors.fg.green}{'-'*calc_line(c1.thirst)}{' '*(10-calc_line(c1.thirst))}{colors.reset}{c1.thirst}%\n")    
 
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

      |\      _,,,---,,_
      /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) 
''',
        '''

      |\      _,,,---,,_
   z  /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) 
''',
        '''

 Z    |\      _,,,---,,_
   z  /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) 
''',
        '''
Z        
 Z    |\      _,,,---,,_
   z  /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) 
''',
    ]
    anims['feed']=[
        '''
                   _ |\_
                   \` - -\\
              __,.-" =__Y=
            ."        )
      _    /   ,    \/\_
     ((____|    )_-\ \_-`========
     `-----'`-----` `--`  =====
        ''',
                '''
                   _ |\_
                   \` - -\\
              __,.-" =__Y=
            ."        ) \\\\
      _    /   ,    \/\_
     ((____|    )_-\ \_-`========
     `-----'`-----` `--`  =====
        ''',
                '''
                   _ |\_
                   \` - -\\
              __,.-" =__Y=
            ."        ) \\\\
      _    /   ,    \/\_ \\\\
     ((____|    )_-\ \_-`========
     `-----'`-----` `--`  =====
        ''',
                '''
                   _ |\_
                   \` - -\\
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
my_file = Path("logfile.txt")
if my_file.is_file():
    os.remove("logfile.txt")
#resize window size
system('mode con: cols=40 lines=25')


c1 = cat("Sigi")
current_animation = c1.anims['sleep']



t1 = threading.Thread(target=uiCycle)
t1.start()


#Statemaschine
while True:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        log("stopped listener")
    
    if entered_id == -1:
        log("Entering idle state")
        current_animation = c1.anims['sleep']
        #idle
        ...
    elif entered_id == 0:
        log("Entering play state")
        current_animation = c1.anims['play']
        time.sleep(3)
        entered_id = -1
        ...
    elif entered_id == 1:
        current_animation = c1.anims['feed']
        ...
    elif entered_id == 2:
        ...
    elif entered_id == 3:
        ...
    elif entered_id == 4:
        ...