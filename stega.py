
from PIL import Image

def decode_image(path_to_png):
    """
    Decodes the hidden message in a png image
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    print(red_channel)  # Start coding here!

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i,j)))[-1] == '0':
                pixels[i,j] = (255,255,255)
            else:
                pixels[i,j] = (0,0,0)

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


path_to_png = "encoded_sample.png"
decode_image(path_to_png)