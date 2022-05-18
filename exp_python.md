Read image files
```
img_path_ls = glob.glob(img_dir + '/*.jpg') # or '/*.png'
for img_path in img_path_ls:
    img = cv2.imread(img_path)
```
