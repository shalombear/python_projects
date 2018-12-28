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

    # running the app
    def run(self):
        self.root.mainloop()     

# A Label subclass
class Lbl(Label):

    # instantiation
    def __init__(self, frame, lbltext):

        # instantiate parent class
        super().__init__(frame, text=lbltext)

        # pack to frame
        self.pack()

# a Button subclass
class Btn(Button):

    # instantiation
    def __init__(self, frame, btntext):

        # instantiate parent class
        super().__init__(frame, text=btntext)

        # pack to frame
        self.pack()
