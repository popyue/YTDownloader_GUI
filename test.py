from tkinter import *
import os


filePath = __file__
print('file: ', filePath)

wd = os.getcwd()
print('working directory:', wd)

main = Tk()

main.geometry("450x350") # Set Window Size.
Label(main, text="RED", bg="red", fg="white").pack()
Label(main, text="Green", bg="green", fg="white").pack(fill='x')
Label(main, text="BLUE", bg="blue", fg="white").pack(expand='yes')
Label(main, text="Black", bg="black", fg="white").pack(padx=10)
Label(main, text="Yellow", bg="yellow", fg="white").pack(ipadx=30)
Label(main, text="Orange", bg="orange", fg="white").pack(side='left')
Label(main, text="Purple", bg="purple", fg="white").pack(side='left', padx=20)

main.mainloop()


