
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x500')
        self.title('Login page')
        self.primaryColor = '#F5FFFA'
        self.secondaryColor = '#151B54'
        self.emailId = StringVar()
        self.password = StringVar()
        self.resizable(False,False)
        # self.canvas1 = Canvas(self)
        # self.canvas1.pack()


    def createFrame(self):
        self.f = Frame(self, height='300', width='400', bg=self.primaryColor,highlightthickness=1, relief='raised', bd=2)
        self.f.config(highlightbackground = self.secondaryColor, highlightcolor= self.secondaryColor)
        self.f.place(x='190', y='110', width='350', height='275')

    def createHeading(self, ltext, lfont):
        self.label = Label(self.f, text=ltext, font= lfont, padx= 15, pady= 25, bg=self.primaryColor, fg=self.secondaryColor)
        self.label.place(x='125', y='10')

    def createLabel(self, ltext, lfont, xx, yy):
        self.label = Label(self.f, text=ltext, font= lfont, padx= 2, pady= 2, bg=self.primaryColor, fg=self.secondaryColor)
        self.label.place(x=xx, y=yy)

    def createField(self, xx, yy):
        self.field = Entry(self.f, textvariable=self.emailId)
        self.field.place(x=xx, y=yy)
        self.field.insert(1, 'username')

    def createObscureField(self, xx, yy):
        self.field = Entry(self.f, textvariable=self.password, show='*')
        self.field.place(x=xx, y=yy)

    def createButton(self, btext):
        self.button = Button(self.f, command=self.print, text=btext, bg=self.secondaryColor, fg=self.primaryColor)
        self.button.place(x='125', y='210')
        
    def print(self):
        print('ok')
        print(f'E-mail - {self.emailId.get()}')
        print(f'Password - {self.password.get()}')
        if self.emailId.get() == 'prakhar@gmail.com' and self.password.get() == '12345678':
            messagebox.showinfo('Login Successful', 'You have been successfully logged in to prakhar@gmail.com')
        else:
            messagebox.showinfo('Login Failed', 'Invalid username or password')

    

if __name__ == '__main__':
    window = GUI()


    window.createFrame()
    window.createHeading('LOGIN', 'consolas 18 bold')
    window.createLabel('Username', 'arial 9 ', 70 ,110)
    window.createField(150, 110)
    window.createLabel('Password', 'arial 9 ', 70, 160)
    window.createObscureField(150, 160)
    window.createButton('Submit')

    window.mainloop()