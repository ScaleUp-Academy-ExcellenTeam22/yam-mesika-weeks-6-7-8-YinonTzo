from PIL import Image

if __name__ == '__main__':
    with Image.open("code.png") as im:
        im.show()
