#note008_file.py

########## 1. OPEN, WRITE, READ FILE
#1) create file, write on it
score_file = open("score.txt", "w", encoding = "utf8")  #w: write / utf8: without it, some language characters may be broken.
print("Math: 0", file = score_file)
print("English: 40", file = score_file)
score_file.close()                                      #must always close the file
#result: score.txt file is created. Need to open the file to see results.
#two lines (Maht: 0, English: 40) exist

#2) another way to write 
score_file = open("score.txt", "a", encoding = "utf8")  #a: append(write further)
score_file.write("Physics: 60")
score_file.write("\nCoding: 100")                       #\n is needed. .write() will not affect on line change.
score_file.close()
#result: score.txt file is created. Need to open the file to see results.
#four lines (Maht: 0, English: 40, Physics: 60, Coding: 100) exist

#3) now let's read the file
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()
#result: in the result screen(PowerShell in Visual Studio), results are shown directly. 

#4) if you want to read one line by one line
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline())                            #read line, move cursor to the next line
print(score_file.readline())                            #2 lines will be read. Last two line will not be shown.
print(score_file.readline(), end="")                    #end="" will not make double spacking for the next line
print(score_file.readline())                            #only last 2 lines will have signel spacing.
score_file.close()

#4) if you do not know how many lines are in the file
score_file = open("score.txt", "r", encoding = "utf8")
while True:         #infinite loop
    line = score_file.readline()
    if not line:    #if nothing to read anymore?
        break       #break the loop
    print(line)     #else (if there's something to read in line, print them)
score_file.close()

# failure note: below version only read out 1st line, not all lines.
score_file = open("score.txt", "r", encoding = "utf8")
while True:         
    line = print(score_file.readline())
    if not line:    
        break            
score_file.close()

#5) another way to read
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines()    #here, we use readline*s*(), type(lines) is list.
for line in lines:
    print(line, end="")
score_file.close()
#readlines(): return all lines in the file, as a list where each line is an item in the list object:
#readline(): returns one line from the file.

# failure note: below version will show: ['Maht: 0\n', 'English: 40\n', 'Physics: 60\n', 'Coding: 100']
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readlines())
score_file.close()

########## 2. PICKLE
#Pickel stores data as file type. File can be shared, re-used. Benefit of pickle? it's faster. 
#ref: https://www.geeksforgeeks.org/understanding-python-pickling-example/
#     Pickling is a way to convert a python object (list, dict, etc.) into a character stream. 
#     The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.

#1) create pickle file
import pickle
profile_file = open("profile.pickle", "wb")   #w: write / b: binary / no need to add encoding
profile = {"name": "Lee", "Age": 30, "Hobby": ["soccer", "gold", "swimming"]}
print(profile)
pickle.dump(profile, profile_file)            #profile's data to be saved in the file
profile_file.close()
#result: profile.pickle file has been created

#2) open pickle file
import pickle
profile_file = open("profile.pickle", "rb")  #r: read 
profile = pickle.load(profile_file)          #data from the file to be loaded
print(profile)
profile_file.close()

########## 3. WITH
# codes can be shorter, clearer (ex. no need to use file.close() --> lead less bugs)
# ref: https://www.geeksforgeeks.org/with-statement-in-python/

#1) use pickle & use (convert 2-(2) example)
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

#2) without pickle, let's write and read new file
with open("study.txt", "w") as study_file:
  study_file.write("With is amazing!")
  
#3) load file
with open("study.txt", "w") as study_file:
  print(study_file.read())

########## 4. EXERCISE
# You are creating report everyweek from 1st - 50th week. File's name should be '[]week.txt'
# In every txt file, you will have below contents:
# - []th weekly report -
# Department:
# Name:
# Summary:

#1) First try:
for number in range(1, 51):
    with open("{}week.txt" .format(number), "w") as file:
        file.write("- {}th weekly report -\
        \nDepartment:\
        \nName:\
        \nSummary:" .format(number))
#result: 50 files created with incremental number. Contents have corresponding week number too.     

#2) Answer given by tutor:
for i in range(1, 51):
    with open(str(i) + "week.txt", "w") as file:
        file.write("- {}th weekly report -" .format(i))
        file.write("\nDepartment:")
        file.write("\nName:")
        file.write("\nSummary:")
# result: both my and tutor's answers worked perfectly.
