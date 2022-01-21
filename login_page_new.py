
from asyncio.windows_events import NULL
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
        self.canvas1 = Canvas(self, height=400, width=400)
        # my_rectangle = round_rectangle(50, 50, 150, 100, radius=20, fill="blue")
        self.canvas1.place(x=180, y=100)
        # self.canvas1.round_rectangle(5,5, 365, 290, fill='yellow', outline='yellow', round=10)

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        
            points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]

            return self.canvas1.create_polygon(points, **kwargs, smooth=True, fill=self.primaryColor, outline=self.secondaryColor, width=2)

    def createFrame(self):
        self.f = Frame(self, height='300', width='400',bg=self.primaryColor)#highlightthickness=1, relief='raised', bd=2)
        #self.f.config(highlightbackground = self.secondaryColor, highlightcolor= self.secondaryColor)
        self.f.place(x='190', y='110', width='350', height='275')

    def createHeading(self, ltext, lfont):
        self.label = Label(self.f, text=ltext, font= lfont, padx= 15, pady= 25, bg=self.primaryColor, fg=self.secondaryColor)
        self.label.place(x='125', y='5')

    def createLabel(self, ltext, lfont, xx, yy):
        self.label = Label(self.f, text=ltext, font= lfont, padx= 2, pady= 2, bg=self.primaryColor, fg=self.secondaryColor)
        self.label.place(x=xx, y=yy)

    def createField(self, xx, yy, obscure):
        if(obscure):
            self.field = Entry(self.f, textvariable=self.password, show='*', highlightthickness=1)
        else:
            self.field = Entry(self.f, textvariable=self.emailId,highlightthickness=1 )
        self.field.config(highlightbackground = self.secondaryColor, highlightcolor= self.secondaryColor)
        self.field.place(x=xx, y=yy)
        # self.field.insert(1, 'username')

    # def createObscureField(self, xx, yy):
        
    #     self.field.place(x=xx, y=yy)

    def createButton(self, btext):
        self.button = Button(self.f, command=self.print, font='montserrat 10 bold', text=btext, bg=self.secondaryColor, fg=self.primaryColor)
        self.button.place(x='147', y='210')
        
    def print(self):
        print('ok')
        print(f'E-mail - {self.emailId.get()}')
        print(f'Password - {self.password.get()}')
        if self.emailId.get() == 'prakhar@gmail.com' and self.password.get() == '12345678':
            messagebox.showinfo('Login Successful', 'You have been successfully logged in to prakhar@gmail.com')

        else:
            resp = messagebox.showinfo('Login Failed', 'Invalid username or password')
            if(resp!=NULL):
                self.emailId==''
                self.password==''
                self.clearField()

    def clearField(self):
        self.field.delete(0,END)            
        

    

if __name__ == '__main__':
    window = GUI()

    window.round_rectangle(5,5, 365, 290, radius=30)
    window.createFrame()
    window.createHeading('LOGIN', 'consolas 18 bold')
    window.createLabel('Username', 'montserrat 10 bold', 70 ,100)
    window.createField(150, 100, False)
    window.createLabel('Password', 'montserrat 10 bold', 70, 150)
    window.createField(150, 150, True)
    window.createButton('Submit')

    window.mainloop()