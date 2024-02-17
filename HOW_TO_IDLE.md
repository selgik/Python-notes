## HOW TO USE PYTHON3-IDLE ON MAC
----
- Date: Feb 2, 2023
- Reference: [honcho blog](https://www.honchosearch.com/blog/seo/install-python-modulespackage-using-idle-mac/)
----

### 1. How to use Idle on Mac
- Once Python3 is installed, IDLE will be inclued
- When IDLE is opened, IDLE shell (like a terminal) will be pop up. Go to File -> New File to edit codes
- File needs to be saved before running.

### 2. Ensure Idle is linked to right version of Python if multiple versions are installed
- Scenario: Installed package xyz but an error appeared when tried importing the package "error: ModuleNotFoundError: No module named xyz"
- Root cause: Idle was linked to Python 3.12 but Terminal was linekd to Python 3.11
- Troubleshoot: Associate Idle with Python 3.11
- How: (1) Locate Idle executable in Terminal
```python
which idle3.11
``` 
- (2) Let's say the path is "/Library/Frameworks/Python.framework/Versions/3.11/bin/idle3.11". Navigate to Python 3.11 in Terminal
```python
cd /Library/Frameworks/Python.framework/Versions/3.11/bin/
```
- (3) Launch Idle for Python 311 in Terminal
```python
./idle3.11
```
- Done!
  
### [Outdated] ~~3. How to install packages~~
~~- (1) on the IDLE shell enter below and copy the result path~~  
~~import sys; sys.executable~~

~~- (2) on the Terminal, enter below:~~  
~~path -m pip install package~~

-END-
