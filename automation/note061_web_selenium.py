#note061_web_selenium.py
#refer to Python-practice/virtual_environment/ for setting up virtual environment with venv, selenium and webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


########## 1. TIP
#it is recommended to use terminal within Visual Studio when doing selenium project. Why?
#   1) working on Code Editor and running scripts after each codes will take time as it will open new web-page and do actions
#   2) it will be hard to spot and edit error. Working on terminal will instantly carry action and easier to spot error.


########## 2. OPEN WEB PAGE
#if webdriver exists in the same workspace
browser = webdriver.Chrome()

#otherwise, add directory of chromedriver like below example
browser = webdriver.Chrome('c:/Users/myname/Desktop/Python_Workspace/slnm/chromedriver.exe')

#go to the address
browser.get('http://google.com')


########## 3. LOCATE ELEMENTS AND GET ATTRIBUTE INFORMATION
elem = browser.find_element(By.LINK_TEXT, 'Images')
print(elem)  #result will show up in the terminal with some element information

#use Inspect option on the Chrome to check below attributes, same will show up
elem.get_attribute('href')  #result: destination link when clicked Images button
elem.get_attribute('class') #result: 'gb_q'


########## 4. APPLY ACTION: CLICK, TYPE, ENTER
elem.click()        #click
browser.back()      #go back to previous page 
browser.forward()   #go forward to where it was 
browser.refresh()   #refresh the page
browser.close()     #close current tab
browser.quit()      #quit browser closing all tabs
browser.save_screenshot('screenshot.png') 

#type keyword in the search box
elem = browser.find_element(By.ID, 'APjFqb')   #APjFqb found by using Inspect option on the Chrome (this is ID of search box)
elem.send_keys("python")     #result: python is typed in the search box
elem.clear()                 #result: typed text will be cleared (use when typo was added)
elem.send_keys(Keys.ENTER)   #result: keyboard "ENTER" is input, page will move to search results page

#another way to trigger search? clicking search icon (maginfier icon)
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
    
  
