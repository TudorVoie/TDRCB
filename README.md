# TDRCB
 Tudor's Discord Remote Control Bot
 <br>
<b> Only working on Windows.</b>

## Required PIP Packages
pyinstaller (only needed to compile the code to an exe), discord.py, pyautogui, pygetwindow, psutil

## Bot creation and getting a token
Go to https://discord.com/developers/applications and create a new application. On the 'bot' tab of the application, uncheck 'public bot' so only you can add it and turn on the message intent. Press 'reset token' and copy the given token. Go to OAuth2 and URL Generator and tick the 'bot' scope. Copy the link and add it to your server. Not making this a public bot + adding this into an empty server with just you ensures that no one else will use the bot to do stuff on your computer.

## Downloading, compiling the source code and configuring the bot to run on startup
Download the source code, using the pyinstaller compile it into an exe file with the --onefile --noconsole arguments. Copy the executable a folder you know you won't delete (C:\ for example) then you create a shortcut to it and in the shorcut location, after the executable put a space, then the command prefix, then the bot token. (for example, C:\main.exe ! 1234567890)
