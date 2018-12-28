"""
a GUI wrapper for the matrices module
"""

# importing libraries
import matrices
import gui_tinker as gui


# creating the mainframe
mainframe = gui.App("Matrix Calculator", 500, 500).appframe

# creating some buttons
create_vect_btn = gui.Btn(mainframe, "Create a vector")
find_vect_length_btn = gui.Btn(mainframe, "Find the length of a vector")
find_dot_prod_btn = gui.Btn(mainframe, "Find the dot product between two vectors")
find_angle_btn = gui.Btn(mainframe, "Find the angle between two vectors")

# a class object for a user session with the ability to save
class UserSession:
    """
        attributes:
            vect_lib (dict)
            mtx_lib (dict)
        methods:
            add_to_vect_lib
            add_to_mtx_lib
            save_file
            load_file
    """

    def __init__(self):
        self.vect_lib = {}
        self.mtx_lib = {}
