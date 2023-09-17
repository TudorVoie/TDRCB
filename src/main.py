import discord
from discord.ext import commands
import sys
import os
import pyautogui
import pygetwindow
import psutil
from PIL import Image
import ctypes
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix = str(sys.argv[1]))
bot.launch_time = datetime.utcnow()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    global startdate
    startdate = datetime.now()

@bot.command()
async def test(ctx):
    '''Test Command'''
    await ctx.reply('Test')
    
@bot.command()
async def latency(ctx):
    '''Shows the latency'''
    await ctx.reply('Latency is: ' + str(bot.latency))

@bot.command()
async def shutdown(ctx):
    '''Shutdowns the system'''
    await ctx.reply('Shutting down...')
    os.system('shutdown /s /t 1')
    
@bot.command()
async def restart(ctx):
    '''Restarts the system'''
    await ctx.reply('Restarting...')
    os.system('shutdown /r /t 1')
    
@bot.command()
async def screenshot(ctx):
    '''Screenshot'''
    im2 = pyautogui.screenshot('screenshot.png')
    await ctx.reply(file=discord.File('screenshot.png'))

@bot.command()
async def tasklist(ctx):
    '''Tasklist'''
    wt = pygetwindow.getAllTitles()
    t = '``` \n'
    for x in wt:
        if(x != ''):
            t = t + x + '\n'
    t = t + '```'
    await ctx.reply(t)

@bot.command()
async def res(ctx):
    '''Shows system resources'''
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
    await ctx.reply(embed=embed)

@bot.command()
async def screenshotwindow(ctx, *, title:str):
    '''Screenshots a window'''
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        pyautogui.screenshot ("screenshotwindow.png")
        im = Image.open ("screenshotwindow.png")
        im = im.crop((left, top, right, bottom))
        im.save("screenshotwindow.png")
        await ctx.reply(file=discord.File('screenshotwindow.png'))
    except:
        await ctx.reply(":x: Error getting the window, it might not exist")

@bot.command()
async def minimize(ctx, *, title:str):
    '''Minimize a window'''
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.restore()
        window.minimize()
        await ctx.reply('Done!')
    except:
        await ctx.reply(":x: Error getting the window, it might not exist")
        
@bot.command()
async def maximize(ctx, *, title:str):
    '''Maximize a window'''
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.restore()
        window.maximize()
        await ctx.reply('Done!')
    except:
        await ctx.reply(":x: Error getting the window, it might not exist")

@bot.command()
async def close(ctx, *, title:str):
    '''Closes a window'''
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.close()
        await ctx.reply('Done!')
    except:
        await ctx.reply(":x: Error getting the window, it might not exist")

@bot.command()
async def systemuptime(ctx):
    '''Shows the system uptime'''
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    ctx.reply(f"System uptime: {days} days, {hour:02} hours, {mins:02} minutes and {sec:02} seconds.")

@bot.command()
async def botuptime(ctx):
    '''Shows the bot uptime'''
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m")

@bot.command()
async def bye(ctx):
    '''Closes the bot'''
    bot.close()
    
@bot.command()
async def forcedshutdown(ctx):
    '''Force shutdowns the system'''
    await ctx.reply('Shutting down...')
    os.system('shutdown /s /t 1 /f')
    
@bot.command()
async def forcedrestart(ctx):
    '''Force restarts the system'''
    await ctx.reply('Restarting...')
    os.system('shutdown /r /t 1 /f')
    
@bot.command()
async def shutdowntimer(ctx, time:int, format:str):
    '''Set a timer for shutdown. Usage: [p]shutdowntimer value unit(s/m/h)'''
    if format == "s":
        os.system('shutdown /s /t '+time)
        await ctx.reply('Shutting down in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /s /t '+time*60)
        await ctx.reply('Shutting down in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /s /t '+time*3600)
        await ctx.reply('Shutting down in ' + time + format + '...')
    else:
        await ctx.reply('Error: Cannot schedule shutdown.')
        
@bot.command()
async def restarttimer(ctx, time:int, format:str):
    '''Set a timer for restart. Usage: [p]restarttimer value unit(s/m/h)'''
    if format == "s":
        os.system('shutdown /r /t '+time)
        await ctx.reply('Restarting in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /r /t '+time*60)
        await ctx.reply('Restarting in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /r /t '+time*3600)
        await ctx.reply('Restarting in ' + time + format + '...')
    else:
        await ctx.reply('Error: Cannot schedule restart.')

@bot.command()
async def fshutdowntimer(ctx, time:int, format:str):
    '''Set a timer for forced shutdown. Usage: [p]fshutdowntimer value unit(s/m/h)'''
    if format == "s":
        os.system('shutdown /s /t '+time+' /f')
        await ctx.reply('Shutting down in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /s /t '+time*60+' /f')
        await ctx.reply('Shutting down in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /s /t '+time*3600+' /f')
        await ctx.reply('Shutting down in ' + time + format + '...')
    else:
        await ctx.reply('Error: Cannot schedule forced shutdown.')
 
@bot.command()
async def frestarttimer(ctx, time:int, format:str):
    '''Set a timer for forced restart. Usage: [p]frestarttimer value unit(s/m/h)'''
    if format == "s":
        os.system('shutdown /r /t '+time+' /f')
        await ctx.reply('Restarting in ' + time + format + '...')
    elif format == "m":
        os.system('shutdown /r /t '+time*60+' /f')
        await ctx.reply('Restarting in ' + time + format + '...')
    elif format == "h":
        os.system('shutdown /r /t '+time*3600+' /f')
        await ctx.reply('Restarting in ' + time + format + '...')
    else:
        await ctx.reply('Error: Cannot schedule forced restart.')

@bot.command()
async def aborttimer(ctx):
    '''Abort the timed shutdown / restart'''
    await ctx.reply('Aborting timed shutdown / restart')
    os.system('shutdown /a')
        

bot.run(str(sys.argv[2]))