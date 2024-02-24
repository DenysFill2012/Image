from PIL import Image
from PIL import ImageFilter


with Image.open("tttt.jpg") as original:
    print("rozmir zobrathenna: ", original.size)
    print("формат зображення: ",original.format)
    print("колірний тип: ", original.mode)

    bw= original.convert("L")
    bw.save("bw.jpg")

    bluir = original.filter(ImageFilter.BLUR)
    bluir.save("blur.jpg")
    
    rotateimg = original.transpose(Image.ROTATE_270)
    rotateimg.save("baaa.jpg")

    mirriw = original.transpose(Image.FLIP_LEFT_RIGHT)
    mirriw.save("wsewe.jpg")

    fffe = (11, 11, 52, 33)
    crop = original.crop(fffe)
    crop.save("was.jpg")

    crop.show()
    

