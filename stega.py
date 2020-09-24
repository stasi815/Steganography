
from PIL import Image, ImageDraw, ImageFont

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
    Encodes image with written text
    """
    # Open the image
    original_img = Image.open(path_to_png)

    # Separate the color channels
    red_channel = original_img.split()[0]
    green_channel = original_img.split()[1]
    blue_channel = original_img.split()[2]

    x_size = original_img.size[0]
    y_size = original_img.size[1]

    image_text = write_text(original_img.size, "But that's none of my business...")
    bw_encode = image_text.convert('1')

    # New PIL image with the same size as encoded
    encoded_img = Image.new('RGB', (x_size, y_size))
    pixels = original_img.load()
    for i in range(x_size):
        for j in range(y_size):
            red_channel_pix = bin(red_channel.getpixel((i,j)))
            old_pix = red_channel.getpixel((i,j))
            tencode_pix = bin(bw_encode.getpixel((i,j)))

            if tencode_pix[-1] == '1':
                red_channel_pix = red_channel_pix[:-1] + '1'
            else:
                red_channel_pix = red_channel_pix[:-1] + '0'
            pixels[i, j] = (int(red_channel_pix, 2), green_channel.getpixel((i,j)), blue_channel.getpixel((i,j)))
    encoded_img.save("decoded_img2.png")


def write_text(img_size, text_to_write):
    """
    Writes text to an image
    """
    # create an image
    img_txt = Image.new('RGB', img_size, (255, 255, 255))

    # get a drawing context
    draw = ImageDraw.Draw(img_txt)

    # write black text
    draw.multiline_text((10,10), text_to_write, fill=(0,0,0))
    return img_txt




path_to_png = "encoded_img2.png"
encode_image(path_to_png)