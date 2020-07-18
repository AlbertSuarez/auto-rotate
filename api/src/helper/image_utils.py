import os
import uuid
import base64
import requests
from PIL import Image

from src import DATA_FOLDER, IMAGE_FORMAT


def _write_image(image_content):
    """
    Write an image to a file in the Data folder given its content.
    :param image_content: Image content.
    :return: Output path of given image.
    """
    output_path = os.path.join(DATA_FOLDER, f'{uuid.uuid4()}.{IMAGE_FORMAT}')
    with open(output_path, 'wb') as f:
        f.write(image_content)
    return output_path


def download(image_url):
    """
    Downloads an image given an Internet accessible URL.
    :param image_url: Internet accessible URL.
    :return: Output path of the downloaded image.
    """
    output_path = None
    response = requests.get(image_url, timeout=15)
    if response.ok:
        output_path = _write_image(response.content)
    return output_path


def decode(image_base64):
    """
    Decodes an encoded image in base64.
    :param image_base64: Encoded image.
    :return: Output path of the decoded image.
    """
    image_data = base64.b64decode(image_base64)
    output_path = _write_image(image_data)
    with Image.open(output_path).convert('RGB') as img:
        img.save(output_path, format=IMAGE_FORMAT, quality=95)
    return output_path


def encode(output_image_path):
    """
    Encodes an image in base64 given its path.
    :param output_image_path: Image path.
    :return: Encoded image.
    """
    with open(output_image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string
