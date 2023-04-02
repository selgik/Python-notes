#note059_desktop_file&folder.py
import os
import shutil


########## 1. FILE MANAGEMENT
#1) create file
#if same name folder exists, error will be returned
open("new_file.txt", "a").close()           #create emtpy txt file named "new_file" in append mode

#2) rename file 
os.rename("new_file.txt", "new_file2.txt")  #os.rename(current_name, new_name)

#3) remove file
os.remove("new_file_renamed.txt")


########## 2. FOLDER MANAGEMENT
#1) create folder
os.mkdir("new_folder")                     #new folder will be created at current workspace
os.mkdir("c:/users/Sylvia Kim/test")       #new folder will be created at designated path

#2) create folder with its sub-folders
os.mkdir("new_folders/a_sub/aa_sub/aaa")    #this is WRONG
os.makedirs("new_folders/a_sub/aa_sub/aaa") #this will create new_folders and its sub folders a_sub>aa_sub>aaa

#3) rename folder
os.rename("new_folder", "new_f_name")

#4) remove folder
#rmdir only works when inside of folder is empty
os.rmdir("new_f_name")                      #result: new_f_name folder is removed
os.rmdir("new_folders")                     #result: error will be returned as there are files/folders inside

#so what's an alertnative?
import shutil
shutil.rmtree("new_folders")                #be aware of using it! no alert will show that there is some files/folders inside


########## 3. shutil
#1) copy file to path: shutil.copy
shutil.copy("abc.png", "test_folder")                   #shutil.copy(original path, new path)
shutil.copy("abc.png", "test_folder/abc_copy.png")      #copy to new path and rename it

#2) copy file to path: shutil.copyfile
#unlike shutil.copy, you must use full path (not just folder)
shutil.copyfile("abc.png", "test_folder/abc_copy2.png")  

#3) copy file to path: shutil.copy2
#like shutil.copy, either folder or path can be used in new path
shutil.copy2("abc.png", "test_folder/abc_copy3.png")

### difference betweeen shutil.copy, shutil.copyfile vs shutil.copy2
### unlike shutil.copy and shutil.copyfile, shutil.copy2 will preserve metadata of original file
### --> ex. file creation date of abc_copy3.png will show 2023-01-01 as per original file abc.png
###         but abc_copy.png and abc_copy2.png will show 2023-03-14 (date when file was copied/created)

#4) copy folder
#all subfolders and files will be copied/moved too
shutil.copytree("test_folder", "test_folder2")

#5) move folder (or rename folder)
shutil.move("test_folder", "test_folder2")  #test_folder will be moved under test_folder2 (becoming subfolder)
shutil.move("test_folder2", "test_folder")  #there is no test_folder to move, so test_folder2 name will be changed to test_folder

shutil.move("test_folder", "test_renamed_folder") #giving folder name change effct from test_folder to test_renamed_folder

#6) remove folder
shutil.rmtree("test_renamed_folder")        #be careful, no alert will be shown but remove folder and its sub-folders/files
  
  
