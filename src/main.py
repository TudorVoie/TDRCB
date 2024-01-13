#TDRCB v1.1

import discord
from discord.ext import commands
from discord import app_commands
import sys
import os
import pyautogui
import pygetwindow
import psutil
from PIL import Image
import ctypes
from datetime import datetime
import subprocess

intents = discord.Intents.all()

bot = commands.Bot(intents=intents, command_prefix = '.', help_command = None)
bot.launch_time = datetime.utcnow()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        s = await bot.tree.sync()
        print(f'Synced {len(s)} commands')
    except Exception as e:
        print(e)
    global startdate
    startdate = datetime.now()

@bot.tree.command(name = 'test', description = 'Test command')
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Test')
    
@bot.tree.command(name = 'latency', description = 'Shows the latency')
async def latency(interaction: discord.Interaction):
    await interaction.response.send_message('Latency is: ' + str(bot.latency))

@bot.tree.command(name = 'shutdown', description = 'Peacefully shutsdown the system')
async def shutdown(interaction: discord.Interaction):
    await interaction.response.send_message('Shutting down...')
    os.system('shutdown /s /t 1')
    
@bot.tree.command(name = 'restart', description = 'Peacefully restarts the system')
async def restart(interaction: discord.Interaction):
    await interaction.response.send_message('Restarting...')
    os.system('shutdown /r /t 1')
    
@bot.tree.command(name = 'screenshot', description = 'Takes a screenshot of the whole screen')
async def screenshot(interaction: discord.Interaction):
    im2 = pyautogui.screenshot('screenshot.png')
    await interaction.response.send_message(file=discord.File('screenshot.png'))

@bot.tree.command(name = 'tasklist', description = 'Shows all the open windows')
async def tasklist(interaction: discord.Interaction):
    wt = pygetwindow.getAllTitles()
    t = '``` \n'
    for x in wt:
        if(x != ''):
            t = t + x + '\n'
    t = t + '```'
    await interaction.response.send_message(t)

@bot.tree.command(name = 'resources', description = 'Shows all the system resources')
async def res(interaction: discord.Interaction):
    kb = float(1024)
    mb = float(kb ** 2)
    gb = float(kb ** 3)

    memTotal = int(psutil.virtual_memory()[0]/gb)
    memFree = int(psutil.virtual_memory()[1]/gb)
    memUsed = int(psutil.virtual_memory()[3]/gb)
    memPercent = int(memUsed/memTotal*100)
    cp = psutil.cpu_percent()
    embed = discord.Embed(title="System Usage")
    embed.add_field(name="CPU Usage", value = str(cp) + '%')
    embed.add_field(name="Memory Total", value = str(memTotal) + 'GB')
    embed.add_field(name="Memory Free", value = str(memFree) + 'GB')
    embed.add_field(name="Memory Used", value = str(memUsed) + 'GB')
    embed.add_field(name="Memory Percent", value = str(memPercent) + '%')
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name = 'windowscreenshot', description = 'Takes a screenshot of a window')
async def screenshotwindow(interaction: discord.Interaction, *, title:str):
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        pyautogui.screenshot ("screenshotwindow.png")
        im = Image.open ("screenshotwindow.png")
        im = im.crop((left, top, right, bottom))
        im.save("screenshotwindow.png")
        await interaction.response.send_message(file=discord.File('screenshotwindow.png'))
    except:
        await interaction.response.send_message(":x: Error getting the window, it might not exist")

@bot.tree.command(name = 'minimize', description = 'Minimizes a window')
async def minimize(interaction: discord.Interaction, *, title:str):
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.restore()
        window.minimize()
        await interaction.response.send_message('Done!')
    except:
        await interaction.response.send_message(":x: Error getting the window, it might not exist")
        
@bot.tree.command(name = 'maximize', description = 'Maximizes a window')
async def maximize(interaction: discord.Interaction, *, title:str):
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.restore()
        window.maximize()
        await interaction.response.send_message('Done!')
    except:
        await interaction.response.send_message(":x: Error getting the window, it might not exist")

@bot.tree.command(name = 'close', description = 'Closes a window')
async def close(interaction: discord.Interaction, *, title:str):
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.close()
        await interaction.response.send_message('Done!')
    except:
        await interaction.response.send_message(":x: Error getting the window, it might not exist")

@bot.tree.command(name = 'systemuptime', description = 'Shows the system uptime')
async def systemuptime(interaction: discord.Interaction):
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    interaction.response.send_message(f"System uptime: {days} days, {hour:02} hours, {mins:02} minutes and {sec:02} seconds.")

@bot.tree.command(name = 'botuptime', description = "Shows the bot's uptime")
async def botuptime(interaction: discord.Interaction):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await interaction.response.send_message(f"{days}d, {hours}h, {minutes}m")

@bot.tree.command(name = 'bye', description = 'Stops the bot')
async def bye(interaction: discord.Interaction):
    await interaction.response.send_message('Bye bye :wave:')
    await bot.close()
    
@bot.tree.command(name = 'forcedshutdown', description = 'Forced shutsdown the system')
async def forcedshutdown(interaction: discord.Interaction):
    await interaction.response.send_message('Shutting down...')
    os.system('shutdown /s /t 1 /f')
    
@bot.tree.command(name = 'forcedrestart', description = 'Forced restarts the system')
async def forcedrestart(interaction: discord.Interaction):
    await interaction.response.send_message('Restarting...')
    os.system('shutdown /r /t 1 /f')
    
@bot.tree.command(name = 'shutdowntimer', description = 'Set a timer for shutdown. Usage: /shutdowntimer value unit(s/m/h)')
async def shutdowntimer(interaction: discord.Interaction, time:int, format:str):
    if format == "s":
        os.system('shutdown /s /t '+time)
        await interaction.response.send_message('Shutting down in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /s /t '+time*60)
        await interaction.response.send_message('Shutting down in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /s /t '+time*3600)
        await interaction.response.send_message('Shutting down in ' + time + format + '...')
    else:
        await interaction.response.send_message('Error: Cannot schedule shutdown.')
        
@bot.tree.command(name = 'restarttimer', description = 'Set a timer for restart. Usage: /restarttimer value unit(s/m/h)')
async def restarttimer(interaction: discord.Interaction, time:int, format:str):
    if format == "s":
        os.system('shutdown /r /t '+time)
        await interaction.response.send_message('Restarting in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /r /t '+time*60)
        await interaction.response.send_message('Restarting in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /r /t '+time*3600)
        await interaction.response.send_message('Restarting in ' + time + format + '...')
    else:
        await interaction.response.send_message('Error: Cannot schedule restart.')

@bot.tree.command(name = 'fshutdowntimer', description = 'Sets a forced shutdown timer Usage: /fshutdowntimer value unit(s/m/h)')
async def fshutdowntimer(interaction: discord.Interaction, time:int, format:str):
    if format == "s":
        os.system('shutdown /s /t '+time+' /f')
        await interaction.response.send_message('Shutting down in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /s /t '+time*60+' /f')
        await interaction.response.send_message('Shutting down in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /s /t '+time*3600+' /f')
        await interaction.response.send_message('Shutting down in ' + time + format + '...')
    else:
        await interaction.response.send_message('Error: Cannot schedule forced shutdown.')
 
@bot.tree.command(name = 'frestarttimer', description = 'Sets a forced restart timer. Usage: /frestarttimer value unit(s/m/h)')
async def frestarttimer(interaction: discord.Interaction, time:int, format:str):
    if format == "s":
        os.system('shutdown /r /t '+time+' /f')
        await interaction.response.send_message('Restarting in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /r /t '+time*60+' /f')
        await interaction.response.send_message('Restarting in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /r /t '+time*3600+' /f')
        await interaction.response.send_message('Restarting in ' + time + format + '...')
    else:
        await interaction.response.send_message('Error: Cannot schedule forced restart.')

@bot.tree.command(name = 'aborttimer', description = 'Aborts the timer')
async def aborttimer(interaction: discord.Interaction):
    await interaction.response.send_message('Aborting timed shutdown / restart')
    os.system('shutdown /a')
        
@bot.tree.command(name = 'cmd', description = 'Runs a cmd command')
async def commandprompt(interaction: discord.Interaction, *, s: str):
    p = subprocess.run(s, shell = True, capture_output = True, text = True)
    if(len(p.stdout + p.stderr) > 1999):
        await interaction.response.send_message('Result of command ```'+ s + '```')
        st = p.stdout + '\n' + p.stderr
        max_lenght = 1990
        while len(st) > max_lenght:
            line_lenght = st[:max_lenght].rfind(' ')
            await bot.get_channel(interaction.channel_id).send(st[:line_lenght])
            st = st[line_lenght + 1:]
        await bot.get_channel(interaction.channel_id).send(st)
    else:
        await interaction.response.send_message('```' + p.stdout + '\n' + p.stderr + '```')

@bot.tree.command(name = 'logoff', description = 'Loggs off Windows')
async def logoff(interaction: discord.Interaction):
    await interaction.response.send_message('Logging off...')
    os.system('logoff')

@bot.tree.command(name = 'msgbox', description = 'Shows a message box.')
async def msgbox(interaction: discord.Interaction, *, msg:str):
    subprocess.run(f'msg * {msg}', shell = True)
    await interaction.response.send_message('Message box appeared.')

bot.run(str(sys.argv[2]))