import threading
import time
import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk
from moviepy.editor import *

from VideoFileFormats import file_formats

video_path = ''


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(False, False)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.video_path = ''
        self.canvas_width = 300
        self.canvas_height = 300
        canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height)
        canvas.pack()

        container = tk.Frame(canvas)
        canvas.create_window(self.canvas_width / 2, self.canvas_height / 2, window=container)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, VideoPage, AboutPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def open_file(self, page_name):
        global video_path
        path = askopenfilename(title="Select file", filetypes=file_formats)
        if not path:
            return
        if path is not None:
            video_path = path
            self.show_frame(page_name)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button1 = tk.Button(self, text="Open Video", pady=20, width=controller.canvas_width // 15,
                            command=lambda: controller.open_file("VideoPage"))
        button2 = tk.Button(self, text="About", pady=20, width=controller.canvas_width // 15,
                            command=lambda: controller.show_frame("AboutPage"))
        button1.pack(pady=controller.canvas_height // 30)
        button2.pack(pady=controller.canvas_height // 30)


class VideoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button2 = tk.Button(self, text="play video", command=lambda: self.playVideo())
        button2.pack()

    def playVideo(self):
        t = tk.Toplevel(self)
        t.wm_title("Window ")
        # t.geometry('100x100')
        my_label = tk.Label(t, text="This is window")
        my_label.pack(side="top", fill="both", expand=True)
        video = imageio.get_reader(video_path)
        thread = threading.Thread(target=self.stream, args=(my_label,))
        thread.daemon = 1
        thread.start()

    # def create_window(self):
    #     self.counter += 1
    #     t = tk.Toplevel(self)
    #     t.wm_title("Window #%s" % self.counter)
    #     l = tk.Label(t, text="This is window #%s" % self.counter)
    #     l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def stream(self, label):
        video = imageio.get_reader(video_path)
        while True:
            for image in video.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=frame_image)
                label.image = frame_image
            time.sleep(0.5)


class AboutPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
