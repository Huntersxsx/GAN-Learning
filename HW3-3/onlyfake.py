import cv2
import os
import argparse

frame_dir = "./results/vangogh2photo_cyclegan/test_latest/images"
imdir = sorted(os.listdir(frame_dir))

img_name = []
img_array = []
for idx in range(len(imdir)):
    if "fake_A" in imdir[idx]:
        img_name.append(imdir[idx])

print(len(img_name))
img_name.sort(key=lambda x: int(x.split('.')[0][5:-7]))

for idx in range(len(img_name)):
    imgname = frame_dir + '/' + img_name[idx]
    img = cv2.imread(imgname)
    img_array.append(img)
print(len(img_array))
#imdir.sort(key=lambda x: int(x.split('.')[0][5:-7]))
#print(len(imdir))
save_dir = "./fakeimages"
count = 1
for image in img_array:
    path = save_dir + '/IMG_' + str(count) + ".jpg"
    print(path)
    cv2.imwrite(path, image)
    count += 1
