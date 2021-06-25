import os
import PIL.Image as  Image
from PIL import  ImageFont,ImageDraw
import random
import gc
IMAGES_PATH='E:\pycharm\photo_wall\\'
IMAGES_FORMAT=['.jpg']
IMAGE_HEIGHT=2732
IMAGE_WIDTH=2048
IMAGE_ROW=1
IMAGE_COL=1
ZOOM_RATIO=20
NUM_IMAGES=15
IMAGE_SAVE_PATH=r'E:\pycharm\photo_wall\result.jpg'
image_names=[]
for i in range(NUM_IMAGES):
    image_names.append(IMAGES_PATH+str(i+1)+'.jpg')



def image_compose():
    to_image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))
    for i in range(1,(IMAGE_ROW+1)*ZOOM_RATIO):
        for j in range(1,(IMAGE_COL+1)*ZOOM_RATIO):
            print(i,".......",j)
            from_image=Image.open(image_names[random.randrange(0,NUM_IMAGES)]).resize((int(IMAGE_WIDTH/ZOOM_RATIO),int(IMAGE_HEIGHT/ZOOM_RATIO)),Image.ANTIALIAS)
            to_image.paste(from_image,(int((j-1)*IMAGE_WIDTH/ZOOM_RATIO),int((i-1)*IMAGE_HEIGHT/ZOOM_RATIO)))
            gc.collect()
    return to_image.save(IMAGE_SAVE_PATH)


def number_image():
    text_image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))  # 新建一张空图
    text = "4192\n4191\n"  # 设置文字图层内容
    ft = ImageFont.truetype("C:\Windows\Fonts\方正粗黑宋简体.ttf", int(IMAGE_HEIGHT/3))  # 选择字体和字体大小
    draw = ImageDraw.Draw(text_image)
    draw.text((0, 0), text, font=ft, fill="red")  # 写入字
    text_image.save("number.jpg")
    gc.collect()

def convert():
    num_image=Image.open("number.jpg")
    back_image=Image.open("result.jpg")
    gc.collect()
    final_image = Image.new("RGB", (IMAGE_WIDTH,IMAGE_HEIGHT))
    gc.collect()
    for l in range(IMAGE_WIDTH):
        for h in range(IMAGE_HEIGHT):
            dot = (l, h)
            #print(dot)
            color_1 = num_image.getpixel(dot)
            color_2 = back_image.getpixel(dot)
            if color_1 == (254, 0, 0):
                color_2=color_2[:-1]+(1000,)
                final_image.putpixel(dot,(255,255,255))
            else:
                #print(color_2)
                final_image.putpixel(dot,color_2)
    final_image.save("final1.jpg")
#image_compose()
print("background image make succeed")
#number_image()
print("number make succeed")
convert()
print("convert succeed")