#note063_web_button,checkbox,option.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

br = webdriver.Chrome()
br.maximize_window()


########## 1. RADIO BUTTON
#radio button allows user to select one option. Selecting another one will result in erasing previous selection.
#access to iframe
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
br.switch_to.frame('iframeResult')

#access to designated element
elem = br.find_element(By.XPATH, '//*[@id="html"]')

#select element
if elem.is_selected() == False:
    print("LOG: option is not selected, let me select for you")
    elem.click()
else:
    print("LOG: option is already selected, no action is required")
 
time.sleep(5)


########## 2. CHECKBOX
#checkbox allows user to select multiple options. Selecting another one will not result in erasing previous selection.
#access to iframe
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
br.switch_to.frame('iframeResult')

#access to designated element(s) 
elem = br.find_element(By.XPATH, '//*[@id="vehicle1"]')
elem2 = br.find_element(By.ID, 'vehicle3')

#select element(s)
if elem.is_selected() == False:
    print("LOG: option is not selected, let me select for you")
    elem.click()
else:
    print("LOG: option is already selected, no action is required")
 
if elem2.is_selected() == False:
    print("LOG: option is not selected, let me select for you")
    elem2.click()
else:
    print("LOG: option is already selected, no action is required")
    
time.sleep(5)


########## 3. SELECT - OPTION (DROP-DOWN)
#select-option(drop-down) allows user to select one option. Selecting another one will result in erasing previous selection.
#access to iframe
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')
br.switch_to.frame('iframeResult')

# access to designated element 
#   - inspecting on dropdown menu will show <select name="cars" id="cars" > == $0
#   - click arrow on the left and it will show <option value> </option> tags
#   - on the option you want to select, ex. Audi, right click copy Xpath

#1) select element with XPATH 
elem = br.find_element(By.XPATH, '//*[@id="cars"]/option[4]')
elem.click()

#2) select element with text  
elem = br.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Audi"]')
elem.click()

#3) select element with partial text match  
elem = br.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

## selecting element with text (fully or partially) can particularly helpful 
## because sometimes web may update its option list, add/remove so option[4] may not always be "Audi"

    
