import time
import psutil
import pygetwindow
import traceback

#4 minutes is selected because it looks like "Away" status is set at 5 minutes, but shows you ~2 minutes away.
#4 minutes seem to work perfectly fine in avoiding that
waitfor = 4 * 60
jiggles = 0
skips = 0
notfound = 0

# Function to switch focus to the specified application
def switch_focus_to_app():
    global jiggles, skips, notfound
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.name().lower() == 'teams.exe' or process.name().lower() == 'ms-teams.exe':
                app_window = pygetwindow.getWindowsWithTitle('Microsoft Teams')
                if app_window:
                    #Jiggle only if window is not already active and maximized (most likely already in focus)
                    if app_window[0].isActive and app_window[0].isMaximized:
                        skips = skips + 1
                        print(f"Jiggle skipped {skips} times")
                    else:
                        #If it's minimized - restore, which will take focus
                        if app_window[0].isMinimized:
                            app_window[0].restore()
                        else:
                            #If not minimized - activate
                            app_window[0].activate()
                        time.sleep(2)
                        app_window[0].minimize()
                        jiggles = jiggles + 1
                        print(f"Jiggled Teams {jiggles} times")
                    return True
        notfound = notfound + 1
        print(f"Teams was not found {notfound} times")
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        traceback.print_exc()
    return False

waitforOrig = waitfor
print(f"Teams Jiggler initiated")
while True:
    # Sleep for 3 minutes after launching the script
    time.sleep(waitfor)

    # Switch focus to the first application
    if switch_focus_to_app():
        waitfor = waitforOrig
    else:
        #If we fail, reduce wait time until we succeed
        waitfor = 30
print(f"Teams Jiggler loop ended")
