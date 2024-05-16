# TDRCB
 Tudor's Discord Remote Control Bot
<br>
<b> Only working on Windows.</b>

# Installation

## Before that....Bot creation and getting a token
Go [here](https://discord.com/developers/applications) and create a new application. On the 'bot' tab of the application, uncheck 'public bot' so only you can add it and turn on the message intent. Press 'reset token' and copy the given token. Go to OAuth2 and URL Generator and tick the 'bot' scope. Copy the link and add it to your server. Not making this a public bot + adding this into an empty server with just you ensures that no one else will use the bot to do stuff on your computer.

## Actual installation
Download `tdrcb.zip`, extract it and run `setup.exe`, put your token and you're ready! Restart your computer for the program to start.

# Compile it yourself

## Required PIP Packages
pyinstaller (only needed to compile the code to an exe), discord.py, pyautogui, pygetwindow, psutil, Pillow

## Commands:
`pyinstaller --onefile --noconsole main.py`
<br>
`pyinstaller --onefile --noconsole setup.py`
<br>
`pyinstaller --onefile --noconsole launcher.py`
<br>
`cd dist`
<br>
`rename main.py tdrcb.exe`
<br>
then you can run `setup.exe`
