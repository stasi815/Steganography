
from PIL import Image, ImageDraw, ImageChops
# Shoutout to Anika for the code help!!

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
    decoded_image.save("decoded_text2.png")


def encode_image(encode_text, path_to_png="encoded_img2.png"):
    """
    Encodes image with written text
    """
    # get original image
    original_img = Image.open(path_to_png)

    # Separate the color channels
    red_channel = original_img.split()[0]
    green_channel = original_img.split()[1]
    blue_channel = original_img.split()[2]

    x_size = original_img.size[0]
    y_size = original_img.size[1]

    image_text = write_text(original_img.size, encode_text)

    # make blank image for text
    encoded_img = Image.new('RGB', (x_size, y_size))
    pixels = original_img.load()

    for x in range(x_size):
        for y in range(y_size):
            red_channel_pix = red_channel.getpixel((x,y))
            green_channel_pix = green_channel.getpixel((x,y))
            blue_channel_pix = blue_channel.getpixel((x,y))
            encoded_img.putpixel((x,y), (red_channel_pix, green_channel_pix, blue_channel_pix))
            if red_channel_pix % 2 == 1:
                red_channel_pix -= 1
                encoded_img.putpixel((x,y), (red_channel_pix, green_channel_pix, blue_channel_pix))
            new_img = ImageChops.add(encoded_img, image_text)

    new_img.save("decoded_img2.png")


def write_text(img_size, text_to_write):
    """
    Writes text to an image
    """
    # create an image
    img_txt = Image.new('RGB', img_size, (1,0,0))

    # get a drawing context
    draw = ImageDraw.Draw(img_txt)

    # write black text
    draw.multiline_text((10,10), text_to_write, fill=(0,0,0))
    return img_txt



encode_text = "But that's none of my business..."
path_to_png = "decoded_img2.png"
# encode_image(encode_text, path_to_png)
decode_image(path_to_png)