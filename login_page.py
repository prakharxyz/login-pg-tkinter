from tkinter import *

root = Tk()

root.title('login')
root.geometry('500x400')

frame = Frame(root, borderwidth='5')
frame.place(x='100', y='80')

Label(frame, text='Login', font='lucida 18 bold', justify=CENTER , padx='15', pady='25').pack(side=TOP, fill='x')

emailEntry = Entry(frame, width='50', justify=CENTER)
emailEntry.pack(side=TOP, fill='x')

root.mainloop()