
from asyncio.windows_events import NULL
from tkinter import *
from turtle import onclick, width

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.title('Login page')
        self.emailId = StringVar()
        self.password = StringVar()


    def createFrame(self):
        self.f = Frame(self, height='100', width='150')
        self.f.pack()

    def createHeading(self, ltext, lfont):
        self.label = Label(self.f, text=ltext, font= lfont, padx= 15, pady= 25, justify=CENTER)
        self.label.pack()

    def createLabel(self, ltext, lfont, ljustify, lpadx, lpady):
        self.label = Label(self.f, text=ltext, font= lfont, padx= lpadx, pady= lpady, justify=ljustify)
        self.label.pack(anchor='sw', pady=(10,0))

    def createField(self):
        self.field = Entry(self.f, textvariable=self.emailId, justify=CENTER)
        self.field.pack()
        self.field.insert(1, 'username')

    def createObscureField(self):
        self.field = Entry(self.f, textvariable=self.password, justify=CENTER, show='*')
        self.field.pack()

    def createButton(self, btext):
        self.button = Button(self.f, command=self.print, text=btext)
        self.button.pack(padx='10', pady='10')
        
    def print(self):
        print('ok')
        print(f'E-mail - {self.emailId.get()}')
        print(f'Password - {self.password.get()}')

    

if __name__ == '__main__':
    window = GUI()


    window.createFrame()
    window.createHeading('LOGIN', 'consolas 18 bold')
    window.createLabel('Username', 'arial 9 ', LEFT, 2, 2,)
    window.createField()
    window.createLabel('Password', 'arial 9 ', LEFT, 2, 2)
    window.createObscureField()
    window.createButton('Submit')

    window.mainloop()