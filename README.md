I work from home as support specialist, and my workload is mostly dependent on tickets, and if there are no tickets, I generally have free time to do what I want, which often results in Microsoft Teams setting "away" status, even though I am not actually away. This small Python script will restore and then minimize your Teams, if it's launched, and do that every 4 minutes to prevent it from setting "away" status. To prevent "reading" of new messages I intentionally select my own profile in Teams before running this.  

This is an alternative to various mouse jigglers, because they generally do not affect Teams, and different ways to `sendKey`, since those can theoretically break things, if some window steals focus and the key you are sending is meaningful in it. Theoretically you can even run this constantly, if you are fine with the risk of Teams stealing focus.  

While this script can objectively be used to "fake" your activity, this is not its intention and it is recommended for use in similar use-case. If you utilize it for anything else and get caught and potentially punished - this will be on you and only you.

Besides Python itself, it will also require `psutil` and `pygetwindow`, which you can install with `pip install psutil` and `pip install pygetwindow` respectively. Having all of them installed, just run the script, and that's it.
