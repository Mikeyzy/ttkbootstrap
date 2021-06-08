"""
    Author: Israel Dryer
    Modified: 2021-06-08
    Adapted for ttkbootstrap from: https://magicutilities.net/magic-mouse/features
"""
from tkinter.messagebox import showinfo
import ttkbootstrap as ttk


class Application(ttk.Window):
    def __init__(self):
        super().__init__(title="Magic Mouse", theme="lumen")
        self.window = ttk.Frame(self)
        self.window.pack(fill="both", expand="yes")
        self.nb = ttk.Notebook(self.window)
        self.nb.pack(fill="both", expand="yes", padx=5, pady=5)
        mu = MouseUtilities(self.nb)
        self.nb.add(mu, text="Mouse 1")

        # add demo tabs
        self.nb.add(ttk.Frame(self.nb), text="Mouse 2")
        self.nb.add(ttk.Frame(self.nb), text="Mouse 3")


class MouseUtilities(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.images = {
            "reset": ttk.PhotoImage(
                name="reset", file="src/ttkbootstrap/gallery/assets/magic_mouse/icons8_reset_24px.png"
            ),
            "reset-small": ttk.PhotoImage(
                name="reset-small", file="src/ttkbootstrap/gallery/assets/magic_mouse/icons8_reset_16px.png"
            ),
            "submit": ttk.PhotoImage(
                name="submit",
                file="src/ttkbootstrap/gallery/assets/magic_mouse/icons8_submit_progress_24px.png",
            ),
            "question": ttk.PhotoImage(
                name="question",
                file="src/ttkbootstrap/gallery/assets/magic_mouse/icons8_question_mark_16px.png",
            ),
            "direction": ttk.PhotoImage(
                name="direction", file="src/ttkbootstrap/gallery/assets/magic_mouse/icons8_move_16px.png"
            ),
            "bluetooth": ttk.PhotoImage(
                name="bluetooth",
                file="src/ttkbootstrap/gallery/assets/magic_mouse/icons8_bluetooth_2_16px.png",
            ),
            "buy": ttk.PhotoImage(
                name="buy", file="src/ttkbootstrap/gallery/assets/magic_mouse/icons8_buy_26px_2.png"
            ),
            "mouse": ttk.PhotoImage(
                name="mouse", file="src/ttkbootstrap/gallery/assets/magic_mouse/magic_mouse.png"
            ),
        }

        for i in range(3):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

        # Column 1 =====================================================================================================
        col1 = ttk.Frame(self, padding=10)
        col1.grid(row=0, column=0, sticky="news")

        ## device info -------------------------------------------------------------------------------------------------
        dev_info = ttk.Labelframe(col1, text="Device Info", padding=10)
        dev_info.pack(side="top", fill="both", expand="yes")

        ### header
        dev_info_header = ttk.Frame(dev_info, padding=5)
        dev_info_header.pack(fill="x")
        ttk.Button(dev_info_header, image="reset", bootstyle='link', command=self.callback).pack(side="left")
        ttk.Label(dev_info_header, text="Model 2009, 2xAA Batteries").pack(side="left", fill="x", padx=15)
        ttk.Button(dev_info_header, image="submit", bootstyle='link', command=self.callback).pack(side="left")

        ### image
        ttk.Label(dev_info, image="mouse").pack(fill="x")

        ### progressbar
        pb = ttk.Progressbar(dev_info, value=66)  # also used as a container for the % complete label
        pb.pack(fill="x", pady=5, padx=5)
        ttk.Label(pb, text="66%", bootstyle='primary inverse').pack()

        ### progress message
        ttk.Label(dev_info, text='Battery is discharging', font="Helvetica 8", anchor="center").pack(fill="x")

        ## licence info ------------------------------------------------------------------------------------------------
        lic_info = ttk.Labelframe(col1, text="License Info", padding=20)
        lic_info.pack(side="top", fill="both", expand="yes", pady=(10, 0))
        lic_info.rowconfigure(0, weight=1)
        lic_info.columnconfigure(0, weight=2)
        lic_title = ttk.Label(lic_info, text="Trial Version, 28 days left", anchor="center")
        lic_title.pack(fill="x", pady=(0, 20))
        ttk.Label(lic_info, text="Mouse serial number:", anchor="center", font="Helvetica 8").pack(fill="x")
        lic_num = ttk.Label(lic_info, text="dtMM2-XYZGHIJKLMN3", anchor="center", bootstyle='info')
        lic_num.pack(fill="x", pady=(0, 20))
        buy_now = ttk.Button(lic_info, image="buy", text="Buy now", compound="bottom", command=self.callback)
        buy_now.pack(padx=10, fill="x")

        # Column 2 =====================================================================================================
        col2 = ttk.Frame(self, padding=10)
        col2.grid(row=0, column=1, sticky="news")

        ## scrolling ---------------------------------------------------------------------------------------------------
        scrolling = ttk.Labelframe(col2, text="Scrolling", padding=(15, 10))
        scrolling.pack(side="top", fill="both", expand="yes")

        op1 = ttk.Checkbutton(scrolling, text="Scrolling", default=True)
        op1.pack(fill="x", pady=5)

        ### no horizontal scrolling
        op2 = ttk.Checkbutton(scrolling, text="No horizontal scrolling")
        op2.pack(fill="x", padx=(20, 0), pady=5)
        ttk.Button(op2, image="question", bootstyle='link', command=self.callback).pack(side="right")

        ### inverse
        op3 = ttk.Checkbutton(scrolling, text="Inverse scroll direction vertically", default=True)
        op3.pack(fill="x", padx=(20, 0), pady=5)
        ttk.Button(op3, image="direction", bootstyle='link', command=self.callback).pack(side="right")

        ### Scroll only vertical or horizontal
        op4 = ttk.Checkbutton(scrolling, text="Scroll only vertical or horizontal", state="disabled")
        op4.pack(fill="x", padx=(20, 0), pady=5)

        ### smooth scrolling
        op5 = ttk.Checkbutton(scrolling, text="Smooth scrolling", default=True)
        op5.pack(fill="x", padx=(20, 0), pady=5)
        ttk.Button(op5, image="bluetooth", style="Link.TButton", command=self.callback).pack(side="right")

        ### scroll speed
        scroll_speed_frame = ttk.Frame(scrolling)
        scroll_speed_frame.pack(fill="x", padx=(20, 0), pady=5)
        ttk.Label(scroll_speed_frame, text="Speed:").pack(side="left")
        ttk.Scale(scroll_speed_frame, defaultvalue=35, from_=1, to=100).pack(side="left", fill="x", expand="yes", padx=5)
        scroll_speed_btn = ttk.Button(scroll_speed_frame, image="reset-small", bootstyle='link')
        scroll_speed_btn.configure(command=self.callback)
        scroll_speed_btn.pack(side="left")

        ### scroll sense
        scroll_sense_frame = ttk.Frame(scrolling)
        scroll_sense_frame.pack(fill="x", padx=(20, 0), pady=(5, 0))
        ttk.Label(scroll_sense_frame, text="Sense:").pack(side="left")
        ttk.Scale(scroll_sense_frame, defaultvalue=50, from_=1, to=100).pack(side="left", fill="x", expand="yes", padx=5)
        scroll_sense_btn = ttk.Button(scroll_sense_frame, image="reset-small", bootstyle='link')
        scroll_sense_btn.configure(command=self.callback)
        scroll_sense_btn.pack(side="left")

        ## 1 finger gestures -------------------------------------------------------------------------------------------
        finger_gest = ttk.Labelframe(col2, text="1 Finger Gestures", padding=(15, 10))
        finger_gest.pack(side="top", fill="both", expand="yes", pady=(10, 0))

        op6 = ttk.Checkbutton(finger_gest, text="Fast swipe left/right to navigate back/forward", default=True)
        op6.pack(fill="x", pady=5)
        ttk.Checkbutton(finger_gest, text="Swap swipe direction", default=True).pack(fill="x", padx=(20, 0), pady=5)

        ### gest sense
        gest_sense_frame = ttk.Frame(finger_gest)
        gest_sense_frame.pack(fill="x", padx=(20, 0), pady=(5, 0))

        ttk.Label(gest_sense_frame, text="Sense:").pack(side="left")

        ttk.Scale(gest_sense_frame, defaultvalue=50, from_=1, to=100).pack(side="left", fill="x", expand="yes", padx=5)

        gest_sense_btn = ttk.Button(gest_sense_frame, image="reset-small", bootstyle='link')
        gest_sense_btn.configure(command=self.callback)
        gest_sense_btn.pack(side="left")

        ## middle click ------------------------------------------------------------------------------------------------
        middle_click = ttk.Labelframe(col2, text="Middle Click", padding=(15, 10))
        middle_click.pack(side="top", fill="both", expand="yes", pady=(10, 0))

        cbo = ttk.Combobox(middle_click, values=["Any 2 finger click", "Other 1", "Other 2"], defaultindex=0)
        cbo.pack(fill="x")

        # Column 3 =====================================================================================================
        col3 = ttk.Frame(self, padding=10)
        col3.grid(row=0, column=2, sticky="news")

        ## two finger gestures -----------------------------------------------------------------------------------------
        two_finger_gest = ttk.Labelframe(col3, text="2 Finger Gestures", padding=10)
        two_finger_gest.pack(side="top", fill="both")

        op7 = ttk.Checkbutton(two_finger_gest, text="Fast swipe left/right to navigate back/forward")
        op7.pack(fill="x", pady=5)

        op8 = ttk.Checkbutton(two_finger_gest, text="Swap swipe direction")
        op8.pack(fill="x", padx=(20, 0), pady=5)

        ### gest sense
        gest_sense_frame = ttk.Frame(two_finger_gest)
        gest_sense_frame.pack(fill="x", padx=(20, 0), pady=(5, 0))

        ttk.Label(gest_sense_frame, text="Sense:").pack(side="left")

        ttk.Scale(gest_sense_frame, defaultvalue=50, from_=1, to=100).pack(side="left", fill="x", expand="yes", padx=5)

        gest_sense_btn = ttk.Button(gest_sense_frame, image="reset-small", bootstyle='link')
        gest_sense_btn.configure(command=self.callback)
        gest_sense_btn.pack(side="left")

        ### fast two finger swipe down
        ttk.Label(two_finger_gest, text="On fast 2 finger up/down swipe:").pack(fill="x", pady=(10, 5))

        op9 = ttk.Checkbutton(two_finger_gest, text="Swap swipe direction", default=True)
        op9.pack(fill="x", padx=(20, 0), pady=5)

        op10 = ttk.Checkbutton(two_finger_gest, text="Swap swipe direction", default=True)
        op10.pack(fill="x", padx=(20, 0), pady=5)

        two_finger_cbo = ttk.Combobox(two_finger_gest, values=["Cycle Task View | Normal | Desktop View"], defaultindex=3)
        two_finger_cbo.pack(fill="x", padx=(20, 0), pady=5)

        ### two finger sense
        two_finger_sense_frame = ttk.Frame(two_finger_gest)
        two_finger_sense_frame.pack(fill="x", padx=(20, 0), pady=(5, 0))

        ttk.Label(two_finger_sense_frame, text="Sense:").pack(side="left")

        ttk.Scale(two_finger_sense_frame, defaultvalue=50, from_=1, to=100).pack(side="left", fill="x", expand="yes", padx=5)

        two_finger_sense_btn = ttk.Button(two_finger_sense_frame, image="reset-small", bootstyle='link')
        two_finger_sense_btn.configure(command=self.callback)
        two_finger_sense_btn.pack(side="left")

        ## mouse options -----------------------------------------------------------------------------------------------
        mouse_options = ttk.Labelframe(col3, text="2 Finger Gestures", padding=(15, 10))
        mouse_options.pack(side="top", fill="both", expand="yes", pady=(10, 0))

        op11 = ttk.Checkbutton(mouse_options, text="Ignore input if mouse if lifted", default=True)
        op11.pack(fill="x", pady=5)

        op12 = ttk.Checkbutton(mouse_options, text="Ignore input if mouse if lifted", default=True)
        op12.pack(fill="x", pady=5)

        op13 = ttk.Checkbutton(mouse_options, text="Ignore input if mouse if lifted", default=True)
        op13.pack(fill="x", pady=5)

        ### base speed
        base_speed_sense_frame = ttk.Frame(mouse_options)
        base_speed_sense_frame.pack(fill="x", padx=(20, 0), pady=(5, 0))

        ttk.Label(base_speed_sense_frame, text="Base speed:").pack(side="left")

        ttk.Scale(base_speed_sense_frame, defaultvalue=50, from_=1, to=100).pack(side="left", fill="x", expand="yes", padx=5)

        base_speed_sense_btn = ttk.Button(base_speed_sense_frame, image="reset-small", bootstyle='link')
        base_speed_sense_btn.configure(command=self.callback)
        base_speed_sense_btn.pack(side="left")

    def callback(self):
        """Demo callback"""
        showinfo(title="Button callback", message="You pressed a button.")


if __name__ == "__main__":
    Application().mainloop()
