import os
import sys
from tkinter import *
import webbrowser
import shutil


def github():
    webbrowser.open_new("https://github.com/tudorvoie/tdrcb")

def devportal():
    webbrowser.open_new("https://discord.com/developers/applications")

root = Tk()
root.title('TDRCB Setup')
root.geometry('450x300')
root.resizable(False, False)


text = Label(root, text = 'TDRCB Setup', font = ('Arial', 20))
text.pack()

text = Label(root, text = 'Please enter your Discord Bot token into the text box below:', font = ('Arial', 12))
text.pack()

text = Label(root, text = 'Make sure there are no spaces before or after the token.', font = ('Arial', 12))
text.pack()

box = Text(root, height = 1, width = 50)
box.pack()

text = Label(root, text = 'After that, press the install button!', font = ('Arial', 12))
text.pack()

def setup():
    pt = os.getenv('USERPROFILE') + r'\TDRCB_DONOTDELETE.token'
    f = open(pt ,'w')
    f.write(box.get("1.0","end-1c"))
    p = os.getenv('APPDATA') + r'\\Microsoft\Windows\Start Menu\Programs\Startup'
    shutil.copy('tdrcb.exe', p)

w = Button(root, text = 'Install!', command = setup)
w.pack()

w = Button(root, text = 'GitHub repository', command = github)
w.pack()

w = Button(root, text = 'Discord Developer Portal', command = devportal)
w.pack()

text = Label(root, text = 'Press the button above to get your bot token', font = ('Arial', 8))
text.pack()

def uninst():
    os.remove(os.getenv('APPDATA') + r'\\Microsoft\Windows\Start Menu\Programs\Startup\tdrcb.exe')
    os.remove(os.getenv('USERPROFILE') + r'\TDRCB_DONOTDELETE.token')

w = Button(root, text = 'Uninstall!', command = uninst)
w.pack()

text = Label(root, text = 'In case you want to uninstall...', font = ('Arial', 8))
text.pack()

root.mainloop()