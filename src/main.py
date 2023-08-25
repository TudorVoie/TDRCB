import discord
from discord.ext import commands
import sys
import os
import pyautogui

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


bot.run(str(sys.argv[2]))
