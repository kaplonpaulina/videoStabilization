from tkinter import *
from tkinter.filedialog import askopenfilename
from VideoFileFormats import file_formats


def open_file():
    path = askopenfilename( title="Select file", filetypes=file_formats)
    if not path:
        return
    if path is not None:
        print(path)


root = Tk()

canvas_width = 1000
canvas_height = 600

button_width = canvas_width/4
button_height = canvas_height/4


canvas = Canvas(root, width=canvas_width, height=canvas_height).pack()

# canvas.pack()
open_video_button = Button(root, text='Open Video', command=open_file).place(x = canvas_width/2-button_width/2, y = canvas_height/3-button_height/2, width=button_width, height=button_height)
about_button = Button(root, text='About').place(x = canvas_width/2-button_width/2, y = 2*canvas_height/3-button_height/2, width=button_width, height=button_height)

mainloop()
