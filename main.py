#!/usr/bin/env python

from pytube import *
import os
import sys
from tkinter import *
#from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter import filedialog as filedialog
from threading import *

try:
	from tkinter import messagebox
except ImportError:
	# Python 2 
	import tkMessageBox as messagebox



def video_information():
	
	'''Pytube test 
	Show the information of video
	'''

	
	# Show the Number of Views of Video
	print("Number of View: ", yt.views)
	
	# Show the length of Video
	print("Length of Video: ", yt.length, "seconds")

	# Show the Description of Video
	print("Description: ", yt.description)

	# Show the Rating of Video
	print("Rating: ", yt.rating)

	# Show the available stream
	#print(yt.streams)

	# Filter only audio
	#print(yt.streams.filter(only_audio=True))
	#yt_audio = yt.streams.filter(only_audio=True)
	#print(yt_audio)
	#yt_audio_mp4 = yt_audio.filter(file_extension='mp4')
	#print(yt_audio_mp4)

	# Fileter only vidoe
	#print(yt.streams.filter(only_vidoe=True))

	'''
	Progressive streams are limited to 720p and contain both audio and video codec files while Dash streams have higher quality but only have video codecs.
	if we want to download a progressive stream, we will get a ready to play video which also has built-in audio.
	'''
	#print(yt.streams.filter(progressive=True))

	# Show highest resolution progressive stream
	#ys = yt.streams.get_highest_resolution()
	#print(ys)

	'''End of Test ''' 

def Widgets():
	
	# Error Message
	global ytdError
	ytdError = Label(root, text="Enter the correct URL to your video", fg="white", font=("jost", 10))
	ytdError.grid(row=6, column=1, columnspan=1, pady=5, padx=5)

	# YTB Link Label
	ytd_link = Label(root, text="YouTube link: ", bg="silver", pady=5, padx=5)
	ytd_link.grid(row=2, column=0, pady=5, padx=5)


	# YTB Link Text
	root.linkText = Entry(root, width=35, textvariable=youtube_link, font="Arial 14")
	root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=1)

	# File Destination Label
	destination_label = Label(root, text="Destination :", bg="silver", pady=5, padx=9)
	destination_label.grid(row=3, column=0, pady=5, padx=5)

	# File Destination
	root.destinationText = Entry(root, width=35, textvariable=download_Path, font="Arial 14")
	root.destinationText.grid(row=3, column=1, columnspan=1, pady=5, padx=5)

	# Browse Button
	browse = Button(root, text="Browse", command=Browse, width=10, bg="blue", relief=GROOVE)
	browse.grid(row=3, column=2, columnspan=2, pady=5, padx=5)

	# ComboBox
	global options
	options=["720p", "Only Audio"]
	#ytdChoice = ttk.Combobox(root, values=options)
	ytdChoice['values'] = options
	ytdChoice.grid(row=4, column=1, pady=5, padx=5)

	# Developer Label
	global developerLabel
	developerLabel = Label(root, text="Author by popyue", font=("jost", 10))
	developerLabel.grid(row=8, column=1, columnspan=1)

	# Download Button
	download = Button(root, text="Download", command=Downloads, width=20, bg="thistle1", pady=10, padx=15, relief=GROOVE, font="Georgia 13")
	download.grid(row=5, column=1, pady=5, padx=5)

	# Progress Bar
	global progressbar
	progressbar = ttk.Progressbar(root, orient="horizontal", length=300)
	progressbar.grid(row=10, column=1, pady=10)

	global prgressLabel
	progressLabel = Label(root, textvariable=percentage, font=("jost", 12))
	progressbar.grid(row=10, column=1, columnspan=1)


def Downloads():

	# Get User-Input YT Link
	link = youtube_link.get()
	# Get File Location 
	download_Folder = download_Path.get()
	
	# Get File Type
	choice = ytdChoice.get()
	print('1:', choice)

	if len(link) >= 1:
		ytdError.config(text="")
		# Get Video
		#yt = YouTube(link, on_progress_callback=progress)
		yt = YouTube(link)

		# Show the Video Title
		title = yt.title
		print("Title: ", yt.title)


		print(choice)
		if choice == options[0]:
			select = yt.streams.get_highest_resolution()
		elif choice == options[1]:
			select = yt.streams.filter(only_audio=True, file_extension='mp4').last()
		else:
			ytdError.config(text="Paste Link Again !!", fg="red")


	# Get Video Size
	global file_size
	file_size = select.filesize # Get File Size


	developerLabel.config(text="{} Video Downloading... {}%".format(title, percentage), font=("jost", 15))
	select.download(download_Folder) # Video Download
	
	# Progress Bar
	'''
	while (percentage != 100):
		progressbar['value'] = percentage
		root.update_idletasks()
	'''
	messagebox.showinfo("Suucessfully Download to :", download_Folder) # Pop up message


def Browse():
	locationError = Label(root, text="location", bg="black", pady=5, padx=5)
	locationError.grid(row=7, column=1, columnspan=1)
	#Folder = getcwd()
	download_DIR = filedialog.askdirectory()
	if len(download_DIR) > 1:
		locationError.config(text=download_DIR, fg="green")
		download_Path.set(download_DIR)
	else:
		locationError.config(text="Please Choose Folder !!", fg="red")
	
'''
def percent(remiain, file_size):
	# Get the percentage of the file that the video has been downloaded
	global percentage
	percentage.set(float(100)*(float(remain) / float(file_size)))
	#print("{:00.0f}% downloaded".format(percentage))
	return percentage

def progress(stream, chunk, file_handle, remaining):
	p = 0 
	while p<100:
		progress = p
		str(p) + '%'
		p = percent(remaining, file_size)
		progressbar['value'] = 
'''

# GUI 
root = Tk()
root.title("YouTube Downloader")
root.geometry("450x350") # Set Window Size
#root.configure(bg='white') # Set up background color
#root.columnconfigure(0,weight=1)

# Create tkinter Variable 
youtube_link = StringVar()
download_Path = StringVar()
percentage = StringVar()
ytdChoice = ttk.Combobox(root)


# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()


'''Sample Video Address
https://www.youtube.com/watch?v=ZgjsUvWFe5c
'''



'''
# Reference 

- [pytube3](https://pypi.org/project/pytube3/)
- [(python) input usage](https://www.runoob.com/python/python-func-input.html)

## Reference Sample Code 

- [(GITHUB)deletedileep YT Download - Progressbar](https://gist.github.com/deletedileep/e8daa73304e8677bddf65d62b22fded9)

## Trouble Shooting

- [(FIXED) Tips On Fixing The “urllib.error.HTTPError: HTTP Error 410: Gone in Pytube” Error](https://ittutoria.net/tips-on-fixing-the-urllib-error-httperror-http-error-410-gone-in-pytube-error/)


'''