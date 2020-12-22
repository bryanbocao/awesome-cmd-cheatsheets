import os
import pathlib
import shutil

# ------------------------------------------------
#  Assume that images are stored in the following
#    address in order:
#  /home/username/Data/RGB/*.png
# ------------------------------------------------
username = 'username'
dataset_root_path = '/home/' + username + '/Data'
img_type = 'RGB'
dataset_img_path = dataset_root_path + '/' + img_type

# ---------------------------------
#  Copy the Entire Folder to _copy
#    e.g. /home/username/Data/RGB_copy/*.png
# ---------------------------------
dataset_dest_img_path = dataset_img_path + '_copy'
dataset_dest_img_path = shutil.copytree(dataset_img_path, dataset_dest_img_path,\
    copy_function = shutil.copy)
print('dataset_img_path: ', dataset_img_path)
print('dataset_dest_img_path: ', dataset_dest_img_path)

# ------------------------------------------------------
#  Rename all *.png as Preparation for Creating a Video
# ------------------------------------------------------
# define the path
currentDirectory = pathlib.Path(dataset_dest_img_path)

# define the pattern
currentPattern = "*.png"

names_dict = {}
names_ls = []
img_cnt = 0
for currentFile in currentDirectory.glob(currentPattern):
    names_dict[currentFile.name] = currentFile
    names_ls.append(currentFile.name)
names_ls.sort()


def get_image_name(image_cnt):
    image_num = ""
    zeros_num = 5 - len(str(image_cnt))
    for i in range(zeros_num):
        image_num += '0'
    image_num += str(image_cnt)
    return "image-" + image_num + ".png"

image_cnt = 1
for file_name in names_ls:
    file_ = names_dict[file_name]
    new_file_name = dataset_dest_img_path + '/' + get_image_name(image_cnt)
    file_.rename(new_file_name)
    image_cnt += 1

print('DONE.')
'''
Execute the following command in Terminal:
    ffmpeg -framerate 30 -i <dataset_dest_img_path>/image-%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p <dataset_dest_img_path>/RGB_video.mp4

E.g.
    ffmpeg -framerate 30 -i /home/username/Data/RGB_copy/image-%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p /home/username/Data/RGB_copy/RGB_video.mp4
'''
