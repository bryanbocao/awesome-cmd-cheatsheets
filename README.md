# quick-cheatsheets
Quick **search** ```Ctrl/Cmd + F``` the commands you need.

---
### Linux
Check Linux version
```
lsb_release -a
```
Check Linux Architecture
```
uname -m
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

Add a new path <new_bin_path>
```
export PATH=$PATH:<new_bin_path>
```
Example: ```<new_bin_path>=/home/user/.local/bin```
```
export PATH=$PATH:/home/user/.local/bin
```
Display ```$PATH``` to verify
```
echo $PATH
```

Check CPU information
```
lscpu
```

Check RAM speed and type
```
sudo dmidecode --type 17
```
[Reference](https://www.cyberciti.biz/faq/check-ram-speed-linux/)

Check hard drive speed
```
sudo hdparm -Tt <Filesystem>
```
Example ```<Filesystem>=/dev/sdb2```
```
sudo hdparm -Tt /dev/sdb2
```
[Reference](https://askubuntu.com/questions/87035/how-to-check-hard-disk-performance)

Grant read, write and execute permissions for everyone, convenient for logging
```
chmod 777 <foldername/filename>
```
Grant read, write and execute permissions for everyone recursively, convenient for logging
```
chmod -R 777 <foldername/filename>
```

Enable syntax highlighting in vim on Mac
```
echo "syntax on" >> ~/.vimrc
```
[Reference](https://apple.stackexchange.com/questions/320287/how-do-i-enable-syntax-highlighting-in-vim-on-mac)

Set default colorscheme in vim

Add ```colorscheme <colorscheme>``` in ```~/.vimrc```

Example ```<colorscheme>=industry```
```
vim ~/.vimrc
colorscheme industry
```

Switch to ```colemak``` keyboard layout (1)
```
setxkbmap us -variant colemak
```
[Reference](https://superuser.com/questions/227727/ubuntu-switch-keyboard-layout-to-colemak)

Switch to ```colemak``` keyboard layout (2)
```
cd ~/Downloads
wget https://colemak.com/pub/unix/colemak-1.0.tar.gz
tar -xf colemak-1.0.tar.gz
cd colemak-1.0
setxkbmap us; xmodmap xmodmap/xmodmap.colemak && xset r 66
```
[Reference](https://colemak.com/Unix)

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

Remap key
```
xev
```
Example: when pressing ```Left``` does not move left
```
KeyRelease event, serial 37, synthetic NO, window 0x5e00001,
    root 0x1e2, subw 0x0, time 96268495, (1670,972), root:(1904,1200),
    state 0x2010, keycode 113 (keysym 0xff7e, Mode_switch), same_screen YES,
    XLookupString gives 0 bytes: 
    XFilterEvent returns: False
```
```
xmodmap -e 'keycode 113 = Left'
```

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
---
ssh via public/private key

also a alterniative solution to ```Permission Denied (publickey)``` problem.

**Local Machine**
```
mkdir ~/.ssh
chmod 700 ~/.ssh
cd ~/.ssh
ssh-keygen -t rsa
```
Terminal
```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/<user>/.ssh/id_rsa): mykey
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in mykey.
Your public key has been saved in mykey.pub.
```
Enter key name (e.g. ```mykey``` on Terminal). Remember the ```passphrase``` yourself.

Executing the following command may still encounter the same issue of ```Permission denied (publickey).```
```
ssh-copy-id -i ~/.ssh/mykey <user>@<remote_host>
```

**Remote Machine**
```
cd ~/.ssh
scp <user>@<local_host>:/home/<user>/.ssh/mykey.pub ~/.ssh/authorized_keys
```

**Local Machine**
```
ssh -i ~/.ssh/mykey <user>@<remote_host>
```
via ```passphrase```

[Reference](https://www.ssh.com/academy/ssh/keygen)

---
Count Files
```
ls | wc -l
```
Count Files in ```<foldername>```
```
ls <foldername> | wc -l
```
Rename images as preparation for video making
[rename4video.py](https://github.com/BryanBo-Cao/quick-cheatsheets/blob/master/utils/rename4video.py)

Unzip all zipped files in a directory and store the content with the same folder name
```
find . -name '*.zip' -exec sh -c 'unzip -d "${1%.*}" "$1"' _ {} \;
```
[[Reference](https://stackoverflow.com/questions/2374772/unzip-all-files-in-a-directory)]


Create a video from images
```
ffmpeg -framerate <FRAME_RATE> -i <DATASET_DEST_IMG_PATH>/image-%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p <DATASET_DEST_IMG_PATH>/RGB_video.mp4
```
Example ```FRAME_RATE=30 DATASET_DEST_IMG_PATH=/home/username/Data/RGB_copy/```
```
ffmpeg -framerate 30 -i /home/username/Data/RGB_copy/image-%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p /home/username/Data/RGB_copy/RGB_video.mp4
```

List all disk devices
```
lsblk
```
e.g.
```
NAME   FSTYPE   LABEL  UUID                                 FSAVAIL FSUSE% MOUNTPOINT
loop0  squashfs                                                   0   100% /snap/bare/5
loop1  squashfs                                                   0   100% /snap/core18/1705
loop2  squashfs                                                   0   100% /snap/snap-store/433
loop3  squashfs                                                   0   100% /snap/snapd/7264
loop4  squashfs                                                   0   100% /snap/gnome-3-34-1804/24
loop5  squashfs                                                   0   100% /snap/gtk-common-themes/1506
loop6  squashfs                                                   0   100% /snap/gtk-common-themes/1535
loop7  squashfs                                                   0   100% /snap/core18/2745
loop8  squashfs                                                   0   100% /snap/gnome-3-34-1804/93
sda
├─sda1 vfat            55D0-8CD7                             504.9M     1% /boot/efi
└─sda2 ext4            53be03f3-b5bf-42a6-8f0c-0252d025f6b7  848.5G     2% /
sdb
├─sdb1 vfat            FACF-6821
├─sdb2
├─sdb3 ntfs            7C0A175A0A17112E
├─sdb4 ntfs            5CAC7AEAAC7ABDD8
├─sdb5 ntfs     新加卷 141A38A91A3889AE
└─sdb6 ntfs     新加卷 A2042BC1042B9777
```

Format Disk Partition ```/dev/sdb``` with ext4 File System
```
sudo mkfs -f ext4 /dev/sdb
```

Mount a new disk ```/dev/sdb1``` not shown by ```df -h``` but listed by ```lsblk```, ```ls /dev/sd*``` or ```sudo fdisk -l```
```
sudo mkdir /ssh
```
Otherwise, it may encounter the issue of ```mount: /ssh: mount point does not exist.```
Then
```
sudo vim /etc/fstab
```
add the below line to the end of the file
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
Rename the directory name listed under the ```Mounted on``` column after ```df -h```

Example: remove ```_``` from ```/_eDrive``` where ```/_eDrive``` is the current directory of the external drive to be renamed.
```
df -h
```
```
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/sdc        1.8T  1.5T  306G  83% /_eDrive
```
```
sudo umount /_eDrive
sudo mkdir /eDrive
sudo vi /etc/fstab
```
Append
```
/dev/sdc /eDrive        ext4    defaults        0       0
```
to the end of this file.
```
sudo mount /dev/sdc
```
Then run ```df -h``` and you should be able to see
```
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/sdc        1.8T  1.5T  306G  83% /eDrive
```
[Reference](https://www.thegeekdiary.com/how-to-change-or-rename-a-mount-point-in-linux/)

Kill all background jobs
```
kill $(jobs -p)
```
[Reference](https://unix.stackexchange.com/questions/43527/kill-all-background-jobs)

---

Download files from Google Drive
```
pip install gdown
```
```
gdown https://drive.google.com/uc?id=<file_id>
```
Example ```https://drive.google.com/file/d/1h_8Ts11rf0GQ4_n6FgmCeBuFcWrRjJfa/view```
```
gdown https://drive.google.com/uc?id=1h_8Ts11rf0GQ4_n6FgmCeBuFcWrRjJfa
```
[Reference](https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive)

Setup Razer Core X
```
pcie_ports=native pci=assign-busses,nocrs,realloc iommu=on
sudo update-grub
sudo add-apt-repository ppa:hertg/egpu-switcher
sudo apt install egpu-switcher
sudo egpu-switcher setup
```
Then Reboot the system.

[Reference](https://egpu.io/forums/thunderbolt-linux-setup/tutorial-ubuntu-18-04-rtx-2080-razer-core-v1/)

[Install Docker on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)

---

### Version Checking
Check CUDA version
```
nvcc --version
```
```
nvcc -V
```
```
ls -l /usr/local | grep cuda
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

### Conda
List env names
```
conda info --envs
```

Clone env ```<env_name>``` from machine ```source``` to ```destination```

In ```source``` machine
```
conda list --explicit > <env_name>.txt
```
Example ```<env_name>=cln_env```
```
conda list --explicit > cln_env.txt
```
Then ```cln_env.txt``` to ```destination``` machine

In ```destination``` machine
```
conda create --name <env_name> --file <path_to_><env_name>.txt
```
Example ```<env_name>=cln_env``` under the ```<path_to_>``` folder
```
conda create --name cln_env --file cln_env.txt
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
Then open a browser on the local machine with the URL provided on the Terminal, e.g. ```*localhost:8888*```

Kill port <PORT_NUM> in use
```
lsof -ti:<PORT_NUM>
```
Example ```<PORT_NUM>=8880```
```
lsof -ti:8880
```

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

### Check Running Containers
```
docker ps -a
```
```
(base) <user>@<machine>:~$ docker ps -a
CONTAINER ID   IMAGE          COMMAND          CREATED         STATUS                       PORTS     NAMES
<CONTAINER_ID>   <IMAGE_ID>   "/bin/bash"      6 minutes ago   Up 6 minutes                           funny_mcnulty
```
### Run a Container with Access to GPUs
```
docker run --ipc=host --shm-size=16384m -it -v /:/share --gpus all --network=bridge <IMAGE_ID> /bin/bash
```
```
nvidia-docker run --ipc=host --shm-size=16384m -it -v /:/share --network=bridge <IMAGE_ID> /bin/bash
```
### Bash into a Running Container
```
docker exec -it <CONTAINER_ID> /bin/bash
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

**Linux**:
```
'atom-text-editor:not([mini])':
  'ctrl-d': 'editor:delete-line'
```

**macOS**
```
'atom-text-editor:not([mini])':
  'cmd-d': 'editor:delete-line'
```

Save the file ```.atom/keymap.cson``` and restart Atom to take effect.

Select multiple lines
```
Cmd + Shift + L
```
Combine multiple lines in one row
```
Cmd + J
```

### remote-atom
local machine
```
sudo apm install remote-atom
```
Open Atom app: ```Packages -> Remote Atom -> Start Server```

remote server
```
sudo curl -o /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate
sudo chmod +x /usr/local/bin/rmate
```

#### Usage
local machine
```
ssh -R 52698:localhost:52698 <user@example.com>
```
remote machine
```
rmate <test.txt>
```
[Reference](https://atom.io/packages/remote-atom)

#### Miscellaneous
Write latex-like math equations in Markdown in Github *.md files
```
<img src="https://render.githubusercontent.com/render/math?math={<latex-like_equations>}">
```
Fill the placeholder ```<latex-like_equations>```. Example
```
<img src="https://render.githubusercontent.com/render/math?math={\kappa_{\Theta}=\frac{\lambda_{max}}{\lambda_{min}}}">
```
Display
<img src="https://render.githubusercontent.com/render/math?math={\kappa_{\Theta}=\frac{\lambda_{max}}{\lambda_{min}}}">

[Reference](https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b?permalink_comment_id=4051474#gistcomment-4051474)

Make hard disk compatible (read & write) in both Mac or Linux (Ubuntu) systems: choose partition format as ```ExFAT``` when erasing the whole disk on Mac.
