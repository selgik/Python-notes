#note062_web_iframe.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


########## 1. ACCESSING ELEMENT WITHIN IFRAME: THEORY
#some html document may contain iframe as below example:
<html>
    <body>
        <iframe id = "1">
            <html>
                <body>
                  <div...>
                </body>
             </html>
        </iframe>

        <iframe id = "2">
            <html>
                <body/>
            </html>
        </iframe>
   </body>
</html>

#for such case, accesing elements using xpath like: html > body > iframe > html > body... is impossible
#we need to tell that we are going to use iframe id=1 and then access xpath


########## 2. ACCESSING ELEMENT WITHIN IFRAME: HOW-TO
#1) website for practice (that contains iframe:)
#   https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio
#   click radio button next to HMTL and using Inspect button, review html. It's under iframe.

#2) switch to iframe and access to element
browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.switch_to.frame('iframeResult')   #input frame ID

elem = browser.find_element(By.XPATH, '//*[@id="html"]')
elem.click()

#3) after action is made, get out from iframe 
browser.switch_to.default_conent()
time.sleep()
browser.quit()

#why use browser.switch_to.default_conent()?
#if I remove that, the driver will still be focused inside the iframe, and subsequent commands may not work as intended.
#therefore, it is recommended to add that to ensure that the driver focus is back on the main document before quitting the browser.
  
  
