# https://dribbble.com/shots/1237618--Gif-Spinner
from itertools import cycle
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import Image, ImageTk, ImageSequence


class AnimatedGif(ttk.Application):

    def __init__(self):
        super().__init__(size=(400, 300), theme='superhero')

        # open the GIF and create a cycle iterator
        with Image.open(r'C:\Users\us43060\Desktop\ttkbootstrap\src\ttkbootstrap\gallery\images\spinners.gif') as im:
            # create a sequence
            sequence = ImageSequence.Iterator(im)

            # use the cycle iterator to convert each frame to a tk photoimage
            self.image_cycle = cycle([ImageTk.PhotoImage(s) for s in sequence])

            # length of each frame
            self.framerate = im.info['duration']

        self.image_container = ttk.Label(self, image=next(self.image_cycle))
        self.image_container.pack(fill=BOTH, expand=YES)
        self.after(self.framerate, self.next_frame)

    def next_frame(self):
        """Update the image for each frame"""
        self.image_container.configure(image=next(self.image_cycle))
        self.after(self.framerate, self.next_frame)


if __name__ == '__main__':
    AnimatedGif().run()
