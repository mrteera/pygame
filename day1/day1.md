# Day 1

## Environment Preparation

After you have VirtualBox and Ubuntu 16.04 (x64) on Windows,
Launch Ubuntu and open Terminal program to update the system to the latest

```
sudo apt-get update
sudo apt-get -y upgrade
```

Check Python version
```
python3 -V
```

Install Python package management
```
sudo apt-get install -y python3-pip
```

Install Python dependencies
```
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
```

Install PyGame
```
sudo pip3 install pygame ipython
```

Open FireFox to Download PyCharm (Python IDE)
```
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux
```
Test PyGame library
```
ipython
```
```
import pygame
```
