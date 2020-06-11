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

Check Tensorflow version
```
pip list | grep tensorflow
```

Check Keras version
```
pip list | grep Keras
```
