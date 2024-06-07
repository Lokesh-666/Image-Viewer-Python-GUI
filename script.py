from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Chicken")
root.iconbitmap('.\images\\angry chicken.ico')


myImage0 = ImageTk.PhotoImage(Image.open('.\images\\cat0.jpeg'))
myImage1 = ImageTk.PhotoImage(Image.open('.\images\\cat1.jpeg'))
myImage2 = ImageTk.PhotoImage(Image.open('.\images\\cat2.jpeg'))
myImage3 = ImageTk.PhotoImage(Image.open('.\images\\cat3.jpeg'))

imageList = [myImage0, myImage1, myImage2, myImage3]
global number
number = 0

global MyLabel
MyLabel = Label(image=imageList[number])
MyLabel.grid(row=0,column=0,columnspan=3)


def action(action):
    match action:
        case 'back':
            GoBack()
        case 'front':
            GoForward()
            
def GoForward():
    global MyLabel
    global number

    MyLabel.grid_forget()
    MyLabel = Label(image=imageList[number+1])
    MyLabel.grid(row=0,column=0,columnspan=3)
    number+=1
    if number+1 ==len(imageList):
        buttonRight = Button(root, text='>>',state=DISABLED)
        buttonRight.grid(row=1,column=2)
    if number == 1:
        buttonLeft = Button(root, text='<<',command = lambda :  action('back'))
        buttonLeft.grid(row=1,column=0)

    
def GoBack():
    global MyLabel
    global number
    MyLabel.grid_forget()
    MyLabel = Label(image=imageList[number-1])
    MyLabel.grid(row=0,column=0,columnspan=3)
    number-=1
    if number == 0:
        buttonLeft = Button(root, text='<<',state=DISABLED)
        buttonLeft.grid(row=1,column=0)
    if number+2 == len(imageList):
        buttonRight = Button(root, text='>>', command=lambda:action('front'))
        buttonRight.grid(row=1,column=2)














buttonQuit = Button(root, text='quit',command=root.quit)

buttonLeft = Button(root, text='<<',command = lambda :  action('back'))
buttonRight = Button(root, text='>>',command = lambda :action('front'))

buttonQuit.grid(row=1,column=1)

buttonLeft.grid(row=1,column=0)
buttonRight.grid(row=1,column=2)


root.mainloop()