from PIL import Image


def decipher():
    """
    https://stackoverflow.com/questions/56441769/iterate-over-all-pixels-to-check-which-pixels-are-white-and-which-are-black
    Open file and decipher code.
    :return: String decrypted from image.
    """
    black = 1

    with Image.open("code.png").convert() as img:
        pixel = img.load()

        return "".join([chr(height)
                        for width in range(img.size[0])
                        for height in range(img.size[1])
                        if pixel[width, height] == black])


if __name__ == '__main__':
    print(decipher())
