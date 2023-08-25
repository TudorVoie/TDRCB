# TDRCB
 Tudor's Discord Remote Control Bot
 <br>
 Only working on Windows.

# Setup
It's pretty simple
## Bot creation and getting a token
Go to https://discord.com/developers/applications and create a new application. On the 'bot' tab of the application, uncheck 'public bot' so only you can add it and turn on the message intent. Press 'reset token' and copy the given token. Go to OAuth2 and URL Generator and tick the 'bot' scope. Copy the link and add it to your server. Not making this a public bot + adding this into an empty server with just you ensures that no one else will use the bot to do stuff on your computer.

## Downloading and configuring the bot to run on startup
Download the zip archive of this repository and extract it. Copy the 'src' folder in the shell:startup folder. Create a batch file with the following code:
```
@echo off
cd src
python main.py <BOT_PREFIX> <BOT_TOKEN>
```

Or you can just run it manually or use the task scheduler, but the prefix and token must be put this way.
