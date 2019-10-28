"""
An examply of the strategy pattern is sort routines implemented for different purposes.
The strategy used to do the sorting is abstracted from the calling code, making it
modular and replaceable.
"""

from PIL import Image

class TiledStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new("RGB", desktop_size)
        num_tiles = [x // i + 1 for x, i in zip(out_img.size, in_img.size)]
        for i in range(num_tiles[0]):
            for j in range(num_tiles[1]):
                out_img.paste(in_img, (
                    in_img.size[0] * i,
                    in_img.size[1] * j,
                    in_img.size[0] * (i + 1),
                    in_img.size[1] * (j + 1),
                    ),
                )
        return out_img


class CenteredStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new("RGB", desktop_size)
        left = (out_img.size[0] - in_img[0]) // 2
        top = (out_img.size[1] - in_img[1]) // 2
        out_img.paste(in_img, (left, top, left + in_img.self[0], top + in_img.size[1]), )
        return out_img


class ScaledStrategy:
    pass


"""
Three strategies that take the same parameters. Once selected, the appropriate strategy
can be calledto create the correctly sized version of the desktop image.

Switching between these options without the strategy pattern would call for putting all
code inside one large method and using if statements to selected the expected one. Every
time we wanted to add a new strategy, we would have to make the method even largry and
difficult to weild.

The preceding example is rarely seen in Python. The classes each represent objects that
provide only a single function. Since there is no other data associated with the object,
we could have just created a set of top-level functions and passed them around as our
strategies instead.

Python's first-class functions allow us to implement the strategy in a more
straightforward way. Knowing the pattern exists can still help us choose the correct
design for our program, but implement it using a more readable syntax. The strategy
pattern, or a top-level function implementation, should be used when we need to allow
client code or the end user to select from multiple implementation of the same interface. 
"""
