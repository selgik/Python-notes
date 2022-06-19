# note001_print

#1. String
print('hello world!')
print("nice to meet you")
print("hehe"*5)

#2. Numeric
print(5)
print(-100)
print(5*(8+5))

#3. Boolean
print(5>10)                     #result will be False
print(5<10)                     #restul will be True
print(True)                     #lower case print(true) will give an error
print(not False)                #result will be True
print(not(5>10))                #result will be True

#4. Variable
#(1) Instead of writing as below:
print("My mom's name is Jessy")
print("My mom is 40 years old")
print("Is mom an adult? True")

#(2) Variables can be assigned which can be updated/re-used:   
family  = "mom"
name    = "Jessy"
age     = 40
hobby   = "cooking"
is_ault = age >=20

print("My " + family + "'s name is " + name)
print("My " + family + " is " + str(age) + " years old")    #str() will change numeric/boolean value to string value.
print("Is " + family + " an adult? " + str(is_adult))       #same as print("Is",family,"an adult?",is_adult) , will auto add space inbetween.

#(3) Variables can be stated in the middle. 
family  = "mom"
name    = "Jessy"
age     = 40
hobby   = "cooking"
is_ault = age >=20

print("My " + family + "'s name is " + name)
age = 55                                                    #we have duplicate variables for age. This one will supersede.
print("My " + family + " is " + str(age) + " years old")    
print("Is " + family + " an adult? " + str(is_adult))   

#5. How to Add Comments?
#(1) Add # in the beginning
#(2) Select the code you want to change into the comments and Cntr+/ (in Windows). To deselect, repeat the task.
#(3) Add ''' in front and in the end of comments lines.

'''
If you need to add multiple lines of comments,
using 3rd option might be easier
''' 
