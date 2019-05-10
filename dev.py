import os,cv2
import numpy as np




PATH = os.getcwd()
# Define data path
data_path = PATH + '/dhrcdata/Train'
data_dir_list = os.listdir(data_path)

print(data_dir_list)	

# Define the number of classes
num_classes = 46

img_data_list=[]


for dataset in data_dir_list:
	img_list=os.listdir(data_path+'/'+ dataset)
	print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
	for img in img_list:
		input_img=cv2.imread(data_path + '/'+ dataset + '/'+ img )
		input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
		input_img_resize=cv2.resize(input_img,(128,128))
		img_data_list.append(input_img_resize)

img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255
print (img_data.shape)

