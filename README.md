# README
### Librării străine folosite:
psutil, pyautogui, pygetwindow, ctypes, discord.py, subprocess, webbrowser, shutil
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

Pentru a lua timpul de funcționare al sistemului:
<code>
lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
</code>

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

Pentru a împărți un mesaj prea lungi în mai multe mesaje de lungimi potrivite:
<code>
max_lenght = 1990
while len(st) > max_lenght:
	line_lenght = st[:max_lenght].rfind(' ')
        await bot.get_channel(interaction.channel_id).send(st[:line_lenght])
        st = st[line_lenght + 1:]
</code>
