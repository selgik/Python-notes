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





