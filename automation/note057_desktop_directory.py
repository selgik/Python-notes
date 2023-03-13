#note057_desktop_directory.py
import os


########## 1. GET/CHANGE DIRECTORY
#1) get current directory
print(os.getcwd())          #result: C:\Users\SylviaK\Desktop\Py_Workspace

#2) change current working directory to specific path
os.chdir("rpa_basic")       
print(os.getcwd())          #result: C:\Users\SylviaK\Desktop\Py_Workspace\rpa_basic

#3) change current working directory to upper folder 
os.chdir("..")              #to parent folder
print(os.getcwd())          #result: C:\Users\SylviaK\Desktop

os.chdir("../..")           #to grand parent folder
print(os.getcwd())          #result: C:\Users\SylviaK

#4) change current working directory to absolute path
os.chdir("c:/")       
print(os.getcwd())          #result: C:\


########## 2. COMBINE PATH/GET DIRECTORY NAME
#1) create file's path
file_path = os.path.join(os.getwcd(), "new_file.txt")   #concatenates os.getwcd() + / + new_file.txt
print(file_path)            #result: C:\Users\SylviaK\Desktop\Py_Workspace\new_file.txt

#2) access to folder where the file belongs to
folder_path = os.path.dirname(r"C:\Users\SylviaK\Desktop\Py_Workspace\new_file.txt")
print(folder_path)                 #result: C:\Users\SylviaK\Desktop\Py_Workspace
print(os.path.dirname(file_path))  #result: same as above

      
########## 3. GET FILE(PATH'S) INFORMATION
#1) get file's creation date
import time
import datetime
ctime = os.path.getctime("exfile.py")
print(ctime)                                  #result: unreadable sequence of number like 17863745.458737
print(datetime.datetime.fromtimestamp(ctime)) #result: more reable such as 2023-03-13 20:10:14.458737
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S")) #result: 20230313 20:10:14

#2) get file's edition date
mtime = os.path.getmtime("exfile.py")

#3) get file's last access date
atime = os.path.getatime("exfile.py")

#4) get file's size
xfile = "rpa_basic/2_desktop/11_file_system.py"
xsize = os.path.getsize(xfile)
print(xsize)


########## 4. GET THE LIST OF FILES
#1) Get list of file and directories in given path
print(os.listdir())               #result: gets all folder/files from current workspace
print(os.listdir("rpa_basic"))    #result: gets all folder/files from given folder ex: ['1_excel', '2_desktop']

#2) Get everything even in the subfolder
listall = os.walk("rpa_basic")    #all subfolders and file list under the folder rpa_basic (1_excel and 2_desktop) will be shown
print(listall)                    #result: unreadable like <generator object +walk at 0x000029384755>

for root, dirs, files in listall:
  print(root, dirs, files)        #result: folder and files list under rpa_basic will be shown
  
  
########## 4. FIND THE FILE
#1) let's say you are trying to see whether abc.py exist in workspace
name = "abc.py"
result = []

for root, dirs, files in os.walk(".")
  if name in files:
    result.append(os.path.join(root, name))
    
print(result)  #result: ['.\\rpa_basic\\2_desktop\\abc.py]
  
#2) same as above but using current directory as target search, will give full directory address
for root, dirs, files in os.walk(os.getcwd()):
  if name in files:
    result.append(os.path.join(root, name))
    
print(result)  #result: ['C:\\Users\\SylviaK\\Desktop\\Py_Workspace\\rpa_basic\\2_desktop\\abc.py]                  
      
      
########## 5. FIND THE FILE WITH PATTERN
# if you are not sure the name of file but only knows the pattern of it

import fnmatch
pattern = "file*.png"  #starts with file and finishes with .png
result = []

for root, dirs, files in os.walk("."):
  if name in files:  
    if fnmatch.fnmatch(name, pattern): #if it matches
      result.append(os.path.join(root, name))

print(result)

   
