from playsound import playsound
import sys
from time import sleep

# Path to the chime that will play when
# the timer is up.
CHIME_PATH = './media/quite-impressed.mp3'

# Get a list of time from command line
# Each item represent a time to coundown from.
# The unit for each item is minutes.
timer_list = sys.argv[1:]
timer_list = [int(time) for time in timer_list]

# convert times to seconds
timer_list = [60 * time for time in timer_list]

# create timer that rings after x minutes.
for timer in timer_list:
    sleep(timer)

    # Play sound twice because the first time may
    # get cutted off.
    playsound(CHIME_PATH)
    playsound(CHIME_PATH)