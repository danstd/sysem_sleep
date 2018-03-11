#Suspend is from https://stackoverflow.com/questions/7517496/suspend-hibernate-pc-with-python
from suspend import suspend
from threading import Timer

#import os
#os.system('C:\\Windows\\System32\\rundll32.exe powrprof.dll,SetSuspendState Hibernate');



print('\n How long until your computer should go to sleep? \n')

while True:
    try:
        hours = eval(input('hours: '))
        minutes = eval(input('\nminutes: '))
        seconds = eval(input('\nseconds: '))
        break

    except NameError:
        print('Please enter a number. \n')

# Convert input into seconds to match the input type for Timer()
timerSum = (hours * 60 * 60) + (minutes * 60) + seconds

# Create a timer object with the number of seconds and the function to be called
t = Timer(timerSum, suspend, ['False'])

t.start()
