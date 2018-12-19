"""
a module model for designing GUI-based apps
"""

#importing libraries
from tkinter import *

#creating a root window for the program
root = Tk()

#modifying root window attributes

#title
root.title("Hello Gooey")

#size
root.geometry("300x200")

#creating a frame
app = Frame(root)

#fitting the frame to the root
app.pack()

#a class for gridding a label with text to a frame
class Lbl:

    #instantiation
    def __init__(self, frame, lbltext):

        #instantiate label with frame and text
        lbl = Label(frame, text=lbltext)

        #grid to frame
        lbl.pack()

#a class for gridding a button with text to a frame
class Btn:

    #instantiation
    def __init__(self, frame, btntext):

        #instantiate Button with frame and text
        btn = Button(frame, text=btntext)

        #grid to frame
        btn.pack()

#examples
hello_txt = """

Hello world!

Hellooooo nurse!
"""

lbl1 = Lbl(app, hello_txt)
btn1 = Btn(app, "I'm a button!")
btn2 = Btn(app, "I'm a button too!")

#running the root
root.mainloop()
