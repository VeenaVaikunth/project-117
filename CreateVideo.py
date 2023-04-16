import os
import cv2

path = '/Users/veenavaikunth/Downloads/'
images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)

if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    file_name = path + '/' + file
    print(file_name)

images.append(file)
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0,8, size)

for i in range(0, count-1):
    cv2.imread(images)
    out.write(images)

print('DONE')