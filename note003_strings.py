#note003_strings.py 

#1. Write string/sentence
sen1 = 'Have a wonderful day'
sen2 = "What a fantastic day"
sen3 = """
If you want to write multiple lines like a paragraph
Add quotes x 3 in front and in the end
"""

#2. Slice strings
# Let's say ID is consists of 6digits + 6digits
# First 6digits represent the date of birth in YYMMDD format
# Second 6digits represent the personal ID and 1st digits from this part represents the gender. 1 for woman, 2 for man.

ID = "901208-122343"
print("Gender identification number is " + ID[7])   #result is 1. Because 7th place of ID is 1 as we count from 0.
print("Year identification number is " + ID[0:2])   #result is 90. ID[0:2] returns value from 0 - before 2nd place, which is 90.
print("Year identification number is " + ID[:2])    #same result as above. 0 can be omitted. 
print("Personal ID number is " + ID[7:14])          #result is 122343
print("Personal ID number is " + ID[7:])            #same ressult as above.
print("Personal ID number is " + ID[-6:])           #same ressult as above. ID[-6:] counts from backward. 

#3. Basic string functions
quote = "Life is beautiful"
print(quote.lower())                                #result is life is beatiful
print(quote.upper())                                #result is LIFE IS BEAUTIFUL
print(quote[0].isupper())                           #restul is True. 0th letter, which is L is in upper format.
print(quote.replace("Life", "My mom"))              #result is My mom is beautiful
print(quote.count("i"))                             #result is 3. i appears 3 times.
print(len(quote))                                   #result is 17. It calculates the number of strings.

#4. Index VS find
quote = "Life is beautiful"
search = quote.index("f")                           #print(search) result is 2. First f appears at 2nd place.
search = quote.index("f", search +1)                #print(search) result is 14. Second f appears at 14th place. 
                                                    #In order for line 36 to work, line 35 must be in place.
print(quote.find("f"))                              #result is 2. Same as index function.
print(quote.find("amazing"))                        #restul is -1. There is no such word "amazing"
print(quote.index("amazing"))                       #result won't show up and it will give error. This is difference between index and find.                                      
  
#5. Escape characters
#If you need to use new line, quote, backslace etc within print you may see errors. You can insert as below instead.

print("let's test to change line \nfrom here")      #\n --> from here will appear in the second line. 
print("He said \"All right, let's do this\"")       #\" --> reult is He said "All right, let's do this"
print("C:\\Users\\Adam Lay\\Desktop")               #\\ --> result is C:\Users\Adam Lay\Desktop
print("pingapple\rPine")                            #\r --> result is Pineapple
print("pineT\bapple")                               #\b --> result is pineapple
print("Fine\tApple")                                #\t --> result is Fine        Apple (like using a tab key)

#6. Using variables
#1) Version 1: all below can be replaced with %s
print("I'm %d years old" %20)                       #%d used for integer --> result is I'm 20 years old
print("I like %s very much" %"coding")              #%s used for strings --> result is I like coding very much
print("Apple starts with character %c" %"A")        #%c used for character --> result is Apple starts with character A
print("I like %s and %s" %("football", "tenis"))    #multiple variables can be used as well.

#2) Version 2
print("I am {} years old" .format(25))              #result is I am 25 years old
print("I like {} and {}" .format("candy", "milk"))  #result is I like candy and milk
print("I like {1} and {0}" .format("candy", "milk"))#result is I like milk and candy

#3) Version 3
print("My name is {name} and I am {age} years old" .format(name="Sylvia", age=20))
                                                    #result is My name is Sylvia and I am 20 years old

#4) Version 4: from Python ver 3.6+
age = 20
name = "Sylvia"
print(f"My name is {name} and I am {age} years old") #result is My name is Sylvia nad I am 20 years old                                                      
      
#7. Exercise
# Task   : Create a password from the website. Take first 3 digits of web name + length of web name + count of alphabet "e" + $ sign in the end
# Ex     : https://google.com --> goo + 5 + 1 + $ --> goo61$
# 1st Try: 

zer = "https://google.com"[7:13]  #extract google
fir = "https://google.com"[7:10]  #extract goo  
sec = len(zer)                    #length("google") is 6
thi = zer.count("e")              #e appears one time in word google
print(f"{fir}{sec}{thi}$")        #add all together.

# Failure note: It worked for for site:google but if the site name get changed, in ex. facebook, 
#               I would have to re-count the digit's place and adjust line 78-79, which is manual.
#               Also, variable names are ambiguous. Right answer should look like below.

# Right answer:

web = "https://google.com"        
web_c = web.replace("https://", "")  #First, remove the part that is not needed for PW creation.\
web_c = web_c[:web_c.index(".")]     #Using the same varialbe cut the part after . (.com or .net etc.)
password = web_c[:3] + str(len(web_c)) + str(web_c.count("e")) + "$"  #combine requirements. 
print(password)

# Benefit: above codes auto clear https:// part and after . part. I do not have to count digit place either.
#          variable names are more intuitive and clear. 
