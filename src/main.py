import discord
from discord.ext import commands
import sys
import os
import pyautogui
import pygetwindow
import psutil
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix = str(sys.argv[1]))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

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

bot.run(str(sys.argv[2]))