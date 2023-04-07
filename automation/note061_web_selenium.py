#note061_web_selenium.py
#refer to Python-practice/virtual_environment/ for setting up virtual environment with venv, selenium and webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


########## 1. TIP
#1) use '' instead of "" inside the bracket as web XPATH may contain "" and having multiple "" in the bracket may cause error
#   - check the example under 4-(3)
#2) it is recommended to use terminal within Visual Studio when doing selenium project. Why?
#   - working on Code Editor and running scripts after each codes will take time as it will open new web-page and do actions
#   - it will be hard to spot and edit error. Working on terminal will instantly carry action and easier to spot error.


########## 2. OPEN WEB PAGE
browser = webdriver.Chrome()        #if webdriver exists in the same workspace use this, otherwise, specify directory as below 
browser = webdriver.Chrome('c:/Users/myname/Desktop/Python_Workspace/slnm/chromedriver.exe')
browser.get('http://google.com')    #go to the address


########## 3. LOCATE ELEMENTS, GET ATTRIBUTE INFORMATION
#1) locate element
elem = browser.find_element(By.LINK_TEXT, 'Images')
print(elem)  #result will show up in the terminal with some element information

#2) obtain attribute information: use Inspect option on the Chrome to confirm below
elem.get_attribute('href')  #result: destination link when clicked Images button
elem.get_attribute('class') #result: 'gb_q'


########## 4. APPLY ACTION: CLICK, TYPE, ENTER
#1) for basic handling 
elem.click()        #click
browser.back()      #go back to previous page 
browser.forward()   #go forward to where it was 
browser.refresh()   #refresh the page
browser.close()     #close current tab
browser.quit()      #quit browser closing all tabs
browser.save_screenshot('screenshot.png') 

#2) type keyword in the search box
elem = browser.find_element(By.ID, 'APjFqb')   #APjFqb found by using Inspect option on the Chrome (this is ID of search box)
elem.send_keys("python")     #result: python is typed in the search box
elem.clear()                 #result: typed text will be cleared (use when typo was added)
elem.send_keys(Keys.ENTER)   #result: keyboard "ENTER" is input, page will move to search results page

#3) trigger search by clicking search icon (maginfier icon)
browser.get('http://youtube.com')  
elem = browser.find_element(By.NAME, 'search_query') #search_query found by using Inspect option on the Chrome (this is name of search box)
elem.send_keys('python')
elem2 = browser.find_element(By.XPATH, '//*[@id="search-icon-legacy"]') #XPATH copied from Inspect option on the Chrome
elem2.click()


########## 5. IDEA FOR WEB RPA (SCRAPPING)    
#getting attribute information
elem = browser.find_element(By.TAG_NAME, 'a')
elem.get_attribute('href')    #result: this will show href info form first a tag. Depending on webpage, result may/may not contain URL

#from result page, get all URLs 
elems = browser.find_elements(By.TAG_NAME, 'a')
for e in elems:
    e.get_attribute('href')    #result: lists of href tag (URLs) will list up
    
  
