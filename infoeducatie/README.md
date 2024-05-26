# README TDRCB
https://github.com/TudorVoie/TDRCB

Folderul src conține tot codul. De îndată ce librăriile necesare sunt instalate, se va folosi pyinstaller cu parametrii --onefile și --noconsole pe fiecare fișier .py. Executabila main.exe va trebui redenumită în tdrcb.exe

### Librării străine folosite:
psutil, pyautogui, pygetwindow, discord.py, Pillow, pyinstaller
### Cod străin folosit:
#### In main.py:
Pentru facerea unei capturi de ecran a unei ferestre (a fost modificat puțin de mine):
<code>
window = pygetwindow.getWindowsWithTitle(title)[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        pyautogui.screenshot (os.getenv('USERPROFILE') + r'\screenshotwindow.png')
        im = Image.open (os.getenv('USERPROFILE') + r'\screenshotwindow.png')
        im = im.crop((left, top, right, bottom))
</code>
sursa: https://www.youtube.com/watch?v=OlEEv7lLbW0

Pentru a lua timpul de funcționare al sistemului:
<code>
lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
</code>
sursa: https://www.geeksforgeeks.org/getting-the-time-since-os-startup-using-python/

Pentru a calcula timpul trecut de la pornirea bot-ului:
<code>
delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await interaction.response.send_message(f"{days}d, {hours}h, {minutes}m")
</code>,
<code>
global startdate
startdate = datetime.now()
</code> și
<code>
bot.launch_time = datetime.utcnow()
</code>
sursa: https://stackoverflow.com/a/63749960

Pentru a colecta statistici despre utilizarea sistemului:
<code>
kb = float(1024)
mb = float(kb ** 2)
gb = float(kb ** 3)
memTotal = int(psutil.virtual_memory()[0]/gb)
memFree = int(psutil.virtual_memory()[1]/gb)
memUsed = int(psutil.virtual_memory()[3]/gb)
memPercent = int(memUsed/memTotal*100)
cp = psutil.cpu_percent()
</code>
sursa: https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/

Pentru a împărți un mesaj prea lungi în mai multe mesaje de lungimi potrivite (cod modificat putin):
<code>
max_lenght = 1990
while len(st) > max_lenght:
	line_lenght = st[:max_lenght].rfind(' ')
        await bot.get_channel(interaction.channel_id).send(st[:line_lenght])
        st = st[line_lenght + 1:]
</code>
sursa: https://stackoverflow.com/a/57023374
