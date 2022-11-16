from pytube import YouTube
from tkinter import *

root = Tk()

root.title("Youtube Video Downloader")
root.geometry("500x500")


def click():
    yurl = url_input.get()
    yt = YouTube(yurl)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


url = Label(root, text="Url")
url.place(x=40, y=60)

url_input = Entry(root,width=50)
url_input.place(x=110, y=60)

button = Button(root, text="Download", command=click)
button.place(x=225, y=250)


root.mainloop()




# yt = YouTube('https://www.youtube.com/watch?v=VRuoR--LdqQ&list=RDVRuoR--LdqQ&start_radio=1&ab_channel=williamVEVO')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


