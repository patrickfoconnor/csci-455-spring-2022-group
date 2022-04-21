import tkinter as tk


class SmartApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().wm_geometry("800x480")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # dictionary for frames, contain the list of frames
        for Frame in (Frame1, Frame2):
            frame = Frame(container, controller=self)
            frame.grid(row=0, column=0, sticky="news")
            self.frames.update({Frame.__name__: frame})
        self.show_frame("Frame1")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # raise to the front


class Frame1(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label = tk.Label(self, text="Frame1")
        self.label.place(x=50, y=50)

        self.btn_1 = tk.Button(self, text="go to Frame2",
                               command=lambda: controller.show_frame("Frame2"))
        self.btn_1.place(x=500, y=200)

    def change_btn_bg(self):
        self.btn_1.configure(bg="green")


class Frame2(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        right_frame = tk.Frame(self, bg="#FF0000")
        right_frame.pack(side="right", expand=True, fill="both")

        left_frame = tk.Frame(self, bg="#00FF00")
        left_frame.pack(side="left", expand=True, fill="both")

        main_menu_btn = tk.Button(right_frame, text="back to Frame1",
                                  command=self.hide)
        main_menu_btn.place(x=240, y=300)

        btn_2 = tk.Button(right_frame, text="Change",
                          command=self.activate)
        btn_2.grid(row=0, rowspan=2, column=3)

    def activate(self):
        # Call Frame1's `change_btn_bg` method
        self.controller.frames["Frame1"].change_btn_bg()

    def hide(self):
        self.controller.show_frame("Frame1")


if __name__ == "__main__":
    app = SmartApp()
    app.mainloop()