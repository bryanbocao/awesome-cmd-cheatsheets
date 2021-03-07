# quick-cheatsheets
Quick search the commands you need.

---
### Linux
Check Ubuntu version
```
lsb_release -a
```

Change computer hostname
```
sudo nano /etc/hostname
```
Then update the old name with a new name.
```
sudo nano /etc/hosts
```
Then update any occurrence of the old name with a new name.

[Reference](https://www.cyberciti.biz/faq/ubuntu-change-hostname-command/)

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

Switch to ```colemak``` keyboard layout
```
setxkbmap us -variant colemak
```
[Reference](https://superuser.com/questions/227727/ubuntu-switch-keyboard-layout-to-colemak)

Switch back to ```us-qwert``` keyboard layout
```
setxkbmap us
```

Swap ```Left Alt``` with ```Left Ctrl```
```
sudo apt-get install gnome-tweak-tool
gnome-tweaks
```
```Keyboard & Mouse -> Additional Layout Options -> Ctrl position -> Swap Left Alt with Left Ctrl```

[Reference](https://askubuntu.com/questions/93624/how-do-i-swap-left-ctrl-with-left-alt-on-my-keyboard)

Adjust mouse wheel scroll speed
```
sudo apt install imwheel
bash <(curl -s http://www.nicknorton.net/mousewheel.sh)
```
[Reference](https://dev.to/bbavouzet/ubuntu-20-04-mouse-scroll-wheel-speed-536o)

Stop laptop going to sleep when closing the lid
```
sudo nano /etc/systemd/logind.conf
```
Change
```
#HandleLidSwitch=suspend
```
to
```
HandleLidSwitch=ignore
```
then
```
sudo systemctl restart systemd-logind
```
[Reference](https://www.dell.com/community/Linux-General/Stop-laptop-going-to-sleep-when-closing-the-lid-UBUNTU-Server/td-p/6086201)

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

Install ```openssh``` server
```
sudo apt-get install openssh-server
```
Verify ```ssh``` service running
```
sudo systemctl status ssh
```
Enable ```ssh``` server
```
sudo systemctl enable ssh
```
Start ```ssh``` server
```
sudo systemctl start ssh
```
Rename images as preparation for video making
[rename4video.py](https://github.com/BryanBo-Cao/quick-cheatsheets/blob/master/utils/rename4video.py)

Create a video from images
```
ffmpeg -framerate <FRAME_RATE> -i <DATASET_DEST_IMG_PATH>/image-%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p <DATASET_DEST_IMG_PATH>/RGB_video.mp4
```
Example ```FRAME_RATE=30 DATASET_DEST_IMG_PATH=/home/username/Data/RGB_copy/```
```
ffmpeg -framerate 30 -i /home/username/Data/RGB_copy/image-%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p /home/username/Data/RGB_copy/RGB_video.mp4
```

Mount a new disk ```/dev/sdb1``` not shown by ```df -h``` but listed by ```ls /dev/sd*``` or ```sudo fdisk -l```
```
sudo vim /etc/fstab
```
add the below line to the end of the file:
```
/dev/sdb1 /ssd  ext4  defaults  0 0
```
```
sudo mount /ssd
```
[Reference](https://askubuntu.com/questions/125257/how-do-i-add-an-additional-hard-drive)

If the following problem occurs
```
mount: /ssd: wrong fs type, bad option, bad superblock on /dev/sdb1, missing codepage or helper program, or other error.
```
do
```
mkfs.ext4 /dev/sdb1
```
and ```sudo mount /ssd``` again, you will see the new disk by ```df -h```

[Reference](https://unix.stackexchange.com/questions/315063/mount-wrong-fs-type-bad-option-bad-superblock)

---

### Version Checking
Check CUDA version
```
nvcc --version
```
```
nvcc -V
```
Check CUDA version - Prerequisite
```
sudo apt install nvidia-cuda-toolkit
```

Check TensorFlow version
```
pip list | grep tensorflow
```
```
python -c 'import tensorflow as tf; print(tf.__version__)'
```

Check Keras version
```
pip list | grep Keras
```
```
python -c 'import keras; print(keras.__version__)'
```

Check PyTorch version
```
python -c 'import torch; print(torch.__version__)'
```

Check OpenCV version
```
python -c 'import cv2; print(cv2.__version__)'
```

---

### Git
Set global user email
```
git config --global user.email "<you@example.com>"
```
Set global username
```
git config --global user.name "<Your Name>"
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


### Atom
Replace delete-line shortcut ```ctrl-shift-k``` with ```ctrl-d```
```
Edit -> Preferences -> Keybindings
```
Search ```ctrl-shift-k``` in the "Search keybindings" box, find the command of delete-line
```
editor:delete-line
```
Search ```ctrl-d``` (which you want to use) in the "Search keybindings" box

Click ```your keymap file```, then it will navigate to ```.atom/keymap.cson```, enter the following text in this file
```
'atom-text-editor:not([mini])':
  'ctrl-d': 'editor:delete-line'
```
Save the file ```.atom/keymap.cson``` and restart Atom to take effect.

### remote-atom
local machine
```
sudo apm install remote-atom
```
Open Atom app: ```Packages -> Remote Atom -> Start Server```

remote server
```
curl -o /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate
sudo chmod +x /usr/local/bin/rmate
```
#### Usage
local machine
```
ssh -R 52698:localhost:52698 <user@example.com>
```
```
rmate <test.txt>
```
[Reference](https://atom.io/packages/remote-atom)
