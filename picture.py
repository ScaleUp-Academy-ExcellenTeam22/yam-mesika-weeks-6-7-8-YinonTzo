from PIL import Image


def decipher(pixels: Image, image: Image) -> str:
    """
    https://stackoverflow.com/questions/56441769/iterate-over-all-pixels-to-check-which-pixels-are-white-and-which-are-black
    Go over the pixels and decipher code.
    :param pixels: the real pixels from the image.
    :param image: Image to go over.
    :return: String decrypted from image.
    """
    black = 1

    return "".join([chr(height)
                    for width in range(image.size[0])
                    for height in range(image.size[1])
                    if pixels[width, height] == black])


def open_image(path: str) -> Image:
    """
    Open image.
    :param path: Path to image.
    :return: Image(as an object).
    """
    return Image.open(path).convert()


def load_image(image: Image) -> Image:
    """
    Load the pixels from the image.
    :param image: Image to load from.
    :return: Loaded image.
    """
    return image.load()


def close_image(image: Image) -> None:
    """
    Close image.
    :param image: Image to close.
    """
    image.close()


def main() -> None:
    """
    Open and load the image, then decipher and print the deciphered sentence.
    """
    path_to_image = "code.png"
    image = open_image(path_to_image)
    pixels = load_image(image)

    print(decipher(pixels, image))
    close_image(image)


if __name__ == '__main__':
    main()
