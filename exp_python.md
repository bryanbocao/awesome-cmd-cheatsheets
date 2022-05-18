Read image files
```
img_path_ls = glob.glob(img_dir + '/*.jpg') # or '/*.png'
for img_path in img_path_ls:
    img = cv2.imread(img_path)
```

Read frames from a video file
```
cap = cv2.VideoCapture(<video_file_path>)
ret, frame_rgb = cap.read()
while ret:
    cv2.imshow('frame_rgb', frame_rgb)
    cv2.waitKey(0)
    ret, frame_rgb = cap.read()
```
