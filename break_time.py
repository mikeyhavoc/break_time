# break_time
# michael Williams
# 0.5
# 7/31/2016
# timer to take a break from my computer to go outside and vape.
import time
import webbrowser

# asks how many breaks to do for a day
breaks = input('how many breaks would you like? ')

def break_time(breaks):

    time_for_break = 0
    while(time_for_break < int(breaks)):
        time.sleep( (60 * 1) * 5)
        timer = time.ctime()
        print(timer)
        webbrowser.open('https://www.youtube.com/watch?v=i-Q2oTRLrK8')
        time_for_break = time_for_break + 1

break_time(breaks)
times = time.ctime()
print(times)
