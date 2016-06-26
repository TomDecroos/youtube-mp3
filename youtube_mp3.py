'''
Created on 26 Jun 2016

@author: tomde_000
'''
from __future__ import unicode_literals
import youtube_dl
import tkSimpleDialog
import Tkinter
root = Tkinter.Tk()
root.withdraw()

url=tkSimpleDialog.askstring("input url","Enter a youtube url:")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
youtube_dl.YoutubeDL(ydl_opts).download([url])