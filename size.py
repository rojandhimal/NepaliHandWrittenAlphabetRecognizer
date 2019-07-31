import cv2
import numpy as np
import os


PATH = os.getcwd()

resize_all_image_path = PATH + '/nepali-barnamala-characters'
print(resize_all_image_path)

new_cat = []
for x in os.listdir(resize_all_image_path):
  new_cat.append(x)
  print(x)


IMG_SIZE = 32

def resize_all_image():
  for catagory in new_cat:
    path = os.path.join(resize_all_image_path, catagory)
    for img in os.listdir(path):
        
        try:
          img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
          new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
          x=str(img)
          img_loc='nepalibarnasnew/'+catagory+'/'+x
          cv2.imwrite(img_loc,new_array)
          #print("Resize and  Saved : {}".format(x))
    
        except Exception as e:
          pass
    print("Resized and shave character {}".format(catagory))

resize_all_image()
print("Resized and saving Completed!")
