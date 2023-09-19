import time
import psutil
import pygetwindow

waitfor = 4 * 60
times = 0


# Function to switch focus to the specified application
def switch_focus_to_app(app_exe, app_name):
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            try:
                if process.name().lower() == app_exe:
                    app_window = pygetwindow.getWindowsWithTitle(f"{app_name}")
                    if app_window:
                        app_window[0].restore()
                        # For some reason if there is no sleep or if it's just 1 second the "jiggle" does not register properly sometimes
                        # 2 seconds seem to be enough to stabilize the behavior
                        time.sleep(2)
                        app_window[0].minimize()
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
    if switch_focus_to_app("teams.exe", "Teams"):
        times = times + 1
        print(f"Jiggled Teams {times} times")
    else:
        print(f"Application '{app1_exe}' not found!")
