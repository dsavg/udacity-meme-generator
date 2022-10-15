"""Define a MemeGenerator module with the following responsibilities.

- Loading of a file from disk
- Transform image by resizing to a maximum width of 500px while maintaining
the input aspect ratio
- Add a caption to an image (string input) with a body and author to a random
location on the image.
"""
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps


class MemeEngine:
    """Load, Transform, and Add caption to an image.

    Class depends on the Pillow library.
    """

    def __init__(self,
                 tmp_path: str = './tmp',
                 img_path: str = None,
                 body: str = None,
                 author: str = None
                 ):
        """Construct a new `MemeEngine` from a temporary path.

        :param tmp_path: An str directory path to save the new meme to.
        """
        self.tmp_path = tmp_path
        self.img_path = img_path
        self.body = body
        self.author = author

        self.width = None
        self._height = None
        self._ratio = None

        self._img = None
        self._img_original = None
        self._original_width = None
        self._original_height = None
        self._message = None
        self._img_draw = None
        self._font = None
        self._file_name = None
        self.out_path = None

    def __repr__(self) -> str:
        """Return `str(self)`."""
        return f'MemeEngine(output_dir="{self.tmp_path}")'

    def make_meme(self,
                  img_path: str = None,
                  body: str = None,
                  author: str = None,
                  width: int = 500
                  ) -> str:
        """Method that loads, transforms and adds caption to image.

        Load of a file from disk.
        Transform image by resizing to a maximum width of 500px while
        maintaining the input aspect ratio.
        Add a caption to an image (string input) with a body and author
        to a random location on the image.

        :param img_path: An str file path to read original image from
        :param body: An str body of quote to add to image
        :param author: An str author of quote to add to image
        :param width: An int width of image
        :return: generate an image path
        """
        self.img_path = img_path
        self.body = body
        self.author = author
        self.width = width

        # check if required arguments are present
        if not isinstance(self.img_path, str):
            raise TypeError(f'"img_path" should be of type str, '
                            f'{type(self.img_path)} found')
        if not isinstance(self.body, str):
            raise TypeError(f'"body" should be of type str, '
                            f'{type(self.body)} found')
        if not isinstance(self.author, str):
            raise TypeError(f'"author" should be of type str, '
                            f'{type(self.author)} found')

        # load of a file from disk
        self._img_original = Image.open(self.img_path)
        # ensure that if image has an EXIF Orientation tag
        # return it's transposed
        self._img = ImageOps.exif_transpose(self._img_original)
        self._img_original.close()
        self._original_width = self._img.size[0]
        self._original_height = self._img.size[1]

        # transform image
        self._ratio = self.width / float(self._original_width)
        self._height = int(self._ratio * float(self._original_height))
        self._img = self._img.resize((self.width, self._height),
                                     Image.Resampling.NEAREST)

        # add caption
        self._message = f'"{body}" \n- {author}'
        self._img_draw = ImageDraw.Draw(self._img)
        self._font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                        size=20)
        self._img_draw.text((self.width/7, self._height/1.5), self._message,
                            font=self._font, fill='white')

        # save image to a file with a meme prefix
        self._file_name = img_path.split('/')[-1]
        self.out_path = f'{self.tmp_path}/meme_{random.randint(1, 100000)}_{self._file_name}'
        self._img.save(self.out_path)

        return self.out_path
