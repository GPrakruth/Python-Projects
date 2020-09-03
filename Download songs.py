from __future__ import unicode_literals
import youtube_dl
import os
import pandas as pd
import ffmpeg
class Download(object):
    def __init__(self, url):

        self.url = url
        self.save_path = os.path.join(os.path.expanduser('~'), 'Videos')
        self.song()

    def song(self):
        opts = {
            'verbose': True,
            'fixup': 'detect_or_warn',
            'ignore-errors': True,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1411',
            }],
            'extractaudio' : True,
            'prefer_ffmpeg': True,
           # 'progress_hooks': [my_hook],
            'keepvideo': True,
            'outtmpl': self.save_path + '/%(title)s.%(ext)s',
            #'noplaylist' : True
        }
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])
if __name__ == '__main__':
    #url = input("Enter url to song here\n  >>  ")
    #Download(url)
    links = (pd.read_excel("Youtube_links.xlsx",sheet_name="Sheet1"))
    for url  in links.Youtube:
        Download(url)
        print("\n \ndownload is finished for url "+url)


    
