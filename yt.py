from pytube import YouTube
from sys import argv
import os

done = False
while(not done):
    title = input("Video Link: ")
    vid = YouTube(title)
    print(f"\nVideo Name: {vid.title}")
    print(f"Author: {vid.author}")
    print(f"Publish Date: {vid.publish_date}\n")
    dl = input("Download? (y/n): ")
    if(dl == "y"):
        stream = vid.streams.get_highest_resolution()
        name = os.getlogin()
        stream.download(f'C:/Users/{name}/YouTube Downloads/{vid.author}')
        print(f"\nDownloaded to: Users/{name}/YouTube Downloads/{vid.author}\n")

    more = input("Download more? (y/n): ")
    if more != "y":
        done = True