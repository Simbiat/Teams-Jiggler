import time
import psutil
import pygetwindow

#4 minutes is selected because it looks like "Away" status is set at 5 minutes, but shows you ~2 minutes away.
#4 minutes seem to work perfectly fine in avoiding that
waitfor = 4 * 60
jiggles = 0
skips = 0

# Function to switch focus to the specified application
def switch_focus_to_app(app_exe, app_name):
    global jiggles, skips
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            try:
                if process.name().lower() == app_exe:
                    app_window = pygetwindow.getWindowsWithTitle(f"{app_name}")
                    if app_window:
                        #Jiggle only if window is not already active and maximized (most likely already in focus)
                        if app_window[0].isActive and app_window[0].isMaximized:
                            skips = skips + 1
                            print(f"Jiggle skipped {skips} times")
                        else:
                            #If it's minimized - restore first
                            if app_window[0].isMinimized:
                                app_window[0].restore()
                            #Activate the window so that we ensure that focus state changes
                            app_window[0].activate()
                            time.sleep(2)
                            app_window[0].minimize()
                            jiggles = jiggles + 1
                            print(f"Jiggled Teams {jiggles} times")
                        return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                print(f"Error while checking process: {e}")
    except psutil.Error as e:
        print(f"Error while iterating processes: {e}")
    return False

print(f"Teams Jiggler initiated")
while True:
    # Sleep for 3 minutes after launching the script
    time.sleep(waitfor)

    # Switch focus to the first application
    if not switch_focus_to_app("teams.exe", "Microsoft Teams"):
        print(f"Application '{app1_exe}' not found!")
print(f"Teams Jiggler loop ended")
