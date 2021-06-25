import os
import PIL.Image as Image
import random
IMAGES_PATH='E:\pycharm\photo_wall\\'
IMAGES_FORMAT=['.jpg']
IMAGE_HEIGHT=2732
IMAGE_WIDTH=2048
IMAGE_ROW=10
IMAGE_COL=10
ZOOM_RATIO=2
NUM_IMAGES=15
IMAGE_SAVE_PATH=r'E:\pycharm\photo_wall\result.jpg'
image_names=[]
for i in range(NUM_IMAGES):
    image_names.append(IMAGES_PATH+str(i+1)+'.jpg')
def image_compose():
    to_image=Image.new('RGB',(IMAGE_COL*IMAGE_WIDTH,IMAGE_ROW*IMAGE_HEIGHT))
    for i in range(1,(IMAGE_ROW+1)*ZOOM_RATIO):
        for j in range(1,(IMAGE_COL+1)*ZOOM_RATIO):
            print(i,".......",j)
            from_image=Image.open(image_names[random.randrange(0,11)]).resize((int(IMAGE_WIDTH/ZOOM_RATIO),int(IMAGE_HEIGHT/ZOOM_RATIO)),Image.ANTIALIAS)
            to_image.paste(from_image,(int((j-1)*IMAGE_WIDTH/ZOOM_RATIO),int((i-1)*IMAGE_HEIGHT/ZOOM_RATIO)))
    return to_image.save(IMAGE_SAVE_PATH)

#if '__name__'=='__main__':
image_compose()