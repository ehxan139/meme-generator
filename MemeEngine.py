"""
MemeEngine generates a meme out of the input image and quote.

MemeEngine is responsible for reading the images, resizing image if required,
adding text to it and finally saving the newly generated meme. 
"""
from PIL import Image, ImageDraw, ImageFont
from os.path import join as path_join


class MemeEngine():
    """Main class that generates a MEME from an image and a quote.
    
    `make_meme` function takes path to an image and a quote to generate a meme.
    Meme is save in the output_dir provided during the initialisation of the 
    MemeEngine object.
    
    :param output_dir: Path to the output dir to save the generated meme.
    """

    def __init__(self, output_dir):
        """Initialise the MemeEngine object.

        :param output_dir: Path to the output dir to save the generated meme.
        """
        self.meme_path = output_dir

    def img_loader(self, img_path: str):
        """Load and return the input image.
        
        :param img_path: Path to the input image.
        """
        return Image.open(img_path)

    def img_to_meme(self, img, text, author, width=500):
        """Convert image to Meme and return it.

        :param img: Input image
        :param text: Body of the quote
        :param author: Author of the quote
        :param width: Output width of the input image
        """
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img_resize = img.resize((width, height), Image.NEAREST)
        if text is not None:
            draw = ImageDraw.Draw(img_resize)
            font = ImageFont.truetype('arial.ttf', size=20)
            draw.text((10, 30), f'"{text}", {author}', font=font, fill='white')
            # draw.text((10, 30), f'"{text}", {author}', fill='white')
        return img_resize

    def meme_save(self, meme, img_path: str):
        """Save the generated meme image.

        :param meme: newly generated meme
        :param img_path: path to the input image
        """
        img_path_split = img_path.rsplit("/", maxsplit=1)
        # meme_path = './_data/meme/' + img_path_split[-1]
        meme_path = path_join(self.meme_path, img_path_split[-1])
        meme.save(meme_path)
        return meme_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make meme from the input image and return path to saved meme.
        
        :param img: Input image
        :param text: Body of the quote
        :param author: Author of the quote
        :param width: Output width of the input image
        """
        try:
            img = self.img_loader(img_path)
        except:
            print(f"Invalid file {img_path}")
        else:
            meme = self.img_to_meme(img, text=text, author=author, width=width)
            meme_path = self.meme_save(meme, img_path=img_path)
            return meme_path
