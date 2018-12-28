"""
sandbox for designing, building, and testing blocks of code
"""

"""
a module model for designing GUI-based apps
"""

# importing libraries
from tkinter import *

# a function for creating root window with a frame
def create_frame(title, width, height):

    root = Tk()
    root.title(title)
    root.geometry(str(width) + 'x' + str(height))

    app = Frame(root)
    app.pack()

    return root, app

def do_the_thing(thing="The thing"):
    print(str(thing) + " has been done!")

# a class for creating a root window with a frame
class App:

    # instantiation
    def __init__(self, title="untitled", width=500, height=500):

        # creating a root window for the program
        # modifying attributes

        root, app = create_frame(title, width, height)
        
        # declaring attributes
        self.root = root
        self.appframe = app

    #running the app
    def run(self):
        self.root.mainloop()     

#a class for packing a label with text to a frame
class Lbl:

    #instantiation
    def __init__(self, frame, lbltext):

        #instantiate label with frame and text
        lbl = Label(frame, text=lbltext)

        #pack to frame
        lbl.pack()

#a class for packing a button with text to a frame
class Btn:

    #instantiation
    def __init__(self, frame, btntext):

        #instantiate Button with frame and text
        btn = Button(frame, text=btntext)

        #pack to frame
        btn.pack()

