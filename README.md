# quick-cheatsheets
Quick search the commands you need.

---
### Linux
Check Ubuntu version
```
lsb_release -a
```

Check global disk storage usage
```
df -h
```

Check currunt disk storage usage
```
df -h .
```

Check all folder sizes recursively in the current folder
```
du -h
```
```
du -h .
```

Check folder sizes only in the current directory
```
du -h --max-depth=1 | sort -hr
```

Check top 20 largest directories under the current folder
```
du -Sh | sort -rh | head -20
```

Grant read, write and execute permissions for everyone, convenient for logging
```
chmod 777 <foldername/filename>
```
Grant read, write and execute permissions for everyone recursively, convenient for logging
```
chmod -R 777 <foldername/filename>
```

Check Tensorflow version
```
pip list | grep tensorflow
```

Check Keras version
```
pip list | grep Keras
```
```
python -c 'import keras; print(keras.__version__)'
```

Check OpenCV version
```
python -c 'import cv2; print(cv2.__version__)'
```

Add a new user
```
sudo adduser <new_username>
```
Add a user to sudo group
```
usermod -aG sudo <username>
```
Switch to another user on one terminal
```
su - <another_user>
```

---

### Using Jupyter Notebook on Local/Remote Machines
Launch jupyter notebook kernel on a remote server
```
jupyter notebook --no-browser --port=<PORT_NUM>
```
Example ```<PORT_NUM>=8888```
```
jupyter notebook --no-browser --port=8888
```

Launch jupyter notebook kernel with a specific GPU on a remote server
```
CUDA_VISIBLE_DEVICES=<GPU_NUM> jupyter notebook --no-browser --port=<PORT_NUM>
```
Example ```<GPU_NUM>=0 <PORT_NUM>=8888```
```
CUDA_VISIBLE_DEVICES=0 jupyter notebook --no-browser --port=8888
```

ssh on a local machine
```	 
ssh -N -f -L 127.0.0.1:<PORT_NUM>:127.0.0.1:<PORT_NUM> <USER>@<URL>
```
Example ```<PORT_NUM>=8888 <USER>=admin <URL>=192.168.1.3```
```	 
ssh -N -f -L 127.0.0.1:8888:127.0.0.1:8888 admin@192.168.1.3
```
Then open a browser on the local machine with the URL provided on the Terminal, e.g. ```*localhost:8888*```.

---

### Training with GPUs
Train a model with a specific GPU
```
CUDA_VISIBLE_DEVICES=<GPU_NUM> python train.py
```
Example ```<GPU_NUM>=0```
```
CUDA_VISIBLE_DEVICES=0 python train.py
```

---

### Using TensorBoard Remotely
Run Tensorboard on a remote server
```
tensorboard --logdir=runs
```
Then check the <PORT_NUM> displayed on the Terminal.

ssh on a local machine:
```	 
ssh -N -f -L 127.0.0.1:<PORT_NUM>:127.0.0.1:<PORT_NUM> <USER>@<URL>
```
Example ```<PORT_NUM>=6006 <USER>=admin <URL>=192.168.1.3```
```	 
ssh -N -f -L 127.0.0.1:6006:127.0.0.1:6006 admin@192.168.1.3
```
Then open a browser on the local machine with the URL provided on the Terminal, e.g. ```*localhost:6006*```.
