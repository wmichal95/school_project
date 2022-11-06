from PIL import ImageChops, Image
import io
from http import HTTPStatus


def put(body):
    image_from_bytes = Image.open(io.BytesIO(body))
    inverted_img = ImageChops.invert(image_from_bytes)

    img_byte_arr = io.BytesIO()
    inverted_img.save(img_byte_arr, format="JPEG")

    return img_byte_arr.getvalue(), HTTPStatus.OK
