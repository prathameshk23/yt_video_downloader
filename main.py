import tkinter
import customtkinter
from pytube import YouTube


def download_video():
    try:
        yt = link.get()
        yt = YouTube(yt, on_progress_callback=on_progress)
        video = yt.streams.get_by_resolution(resolution)
        title.configure(text=yt.title)
        finished.configure(text="Download finished")
        video.download()
    except:
        finished.configure(text="Download failed", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per =  str(int(percentage_of_completion))
    progress.configure(text=per + "%")
    progress.update()

    progress_bar.set(float(percentage_of_completion/100))


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.geometry("720x480")
root.title("YouTube Downloader")

title = customtkinter.CTkLabel(
    root, text="YouTube Downloader", font=("Arial", 20))
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(root, width=345, height=40, textvariable=url)
link.pack()

title = customtkinter.CTkLabel(
    root, text="Enter Resolution", font=("Arial", 20))
title.pack(padx=10, pady=10)

resolution = tkinter.StringVar()
resolv = customtkinter.CTkEntry(
    root, width=345, height=40, textvariable=resolution)
resolv.pack(padx=10, pady=10)

finished = customtkinter.CTkLabel(root, text="")
finished.pack(padx=10, pady=10)

progress = customtkinter.CTkLabel(root, text="0%")
progress.pack()

progress_bar = customtkinter.CTkProgressBar(root, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(
    root, text="Download", command=download_video)
download.pack(padx=10, pady=10)


root.mainloop()
