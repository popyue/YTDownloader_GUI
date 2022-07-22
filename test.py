from tkinter import *
import os


filePath = __file__
print('file: ', filePath)

wd = os.getcwd()
print('working directory:', wd)

main = Tk()

main.mainloop()


