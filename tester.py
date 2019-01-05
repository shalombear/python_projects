# importing libraries
import gui_tinker as gui

program = gui.App("Incremental Counting Button", 500, 500)
app = program.appframe

click_count = 0

btntext = "Number of clicks: {}".format(click_count)

btn = gui.Btn(app, btntext)

def update_click_count():
    click_count = 'bob'
    btn["text"] = btntext

btn["command"] = update_click_count

program.run()
