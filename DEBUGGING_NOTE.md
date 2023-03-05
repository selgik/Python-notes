## CREATING NOTES TO TRACK ERRORS AND BUGS 
## Error Lists
1. Type Error: list object is not callable
2. [Errno 13] Permission denied
3. zsh: command not found 
4. see about_Execution_Policies
5. Chrome page closes immediately after it's opend via selenium
----   



### 1. Type Error: list object is not callable
- Library: matplotlib
- Reference: note038_scatterplot.py, [stake overflow case](https://stackoverflow.com/questions/35030659/unexpected-python-typeerror-list-object-is-not-callable)

- A. Situation: I was trying to create scatterplot using below code 
```python
plt.scatter(df['eng'], df['math'])
plt.xlabel('eng scores')
plt.ylabel('math scores')
```

- B. Mistake: At some point, I made mistakes in assigning label as below
```python
plt.scatter(df['eng'], df['math'])
plt.xlabel=['eng scores']
plt.ylabel=['math scores']
```

- C. 1st Fix: graph was still generated so I did not know that I made mistakes.  
At some point, I found erorrs so I changed B to A.
But even after that no labels were generated. Error message said "Type Error: list object is not callable" 
but I did not have any other list.

- D. 2nd Fix: restart & run.  
Somewhere in the system, plt.xlabel was treated like list. So even after changing B to A, system still showed an error. 
Only when I restarted & run all for jupyter, lables were showing up.
----

### 2. [Errno 13] Permission denied
- Library: openpyxl
- Reference: note041_excel_cell.py
- A. Situation: I was saving changes to excel as below
```python
ws["A1"] = 2
ws["A2"] = 3
ws["A3"] = 4
wb.save("sample.xlsx")
```  

- B. Error: 
```python
# PermissionError: [Errno 13] Permission denied: 'sample.xlsx'
```  

- C. Fix:
Excel file was open hence changes could not have been made.  
When I closed the file and re-run the code, 
all changes have been made.
----

### 3. zsh: command not found 
- Environment: terminal
- Reference: RPA-project/README.md>Part2, [stake overflow: zsh pip error](https://https://stackoverflow.com/questions/42870537/zsh-command-cannot-found-pip) , [stake overflow: zsh pyinstaller error](https://stackoverflow.com/questions/68684044/pyinstaller-command-could-not-be-found)
- A. Situation: using PyInstaller, I was trying to export python scripts to executable app (for MacOS). I typed below code in the terminal.
```terminal
pyinstaller --windowed test.py
``` 
- B. Error 1: I saw zsh error as below, but I do have pyinstaller package installed already. 
```terminal
zsh: command not found: pyinstaller
```  
- C. Error 2: So I tried to locate pyinstaller by typing *which pyinstaller* in the terminal, and I saw next error.
```terminal
pyinstaller not found
``` 
- D. Error 3: I typed *pip unistall pyinstaller* to uninstall and re-install. I saw another error message in my termianl. Now system is saying I do not have pip either.
```terminal
zsh: command not found: pip
```  
- E. Fix for Error 3: As per reference link, I typed *pip3* instead of *pip* in the terminal and confirmed command is correctly recognized.
```terminal
pip3 uninstall pyinstaller
``` 
- F. Fix for Error 1: For *which pyinstaller* command, terminal still gave me an error. After googling, I found out that I should be using below instead:
```terminal
pip3 show pyinstaller
``` 
- G. Fix for Error 2: When I checked package location via F, I noticed that pyinstaller, pip, python are all installed in different locations and from googling I concluded, that could be the root cause of problem. System was having problem finding out packages and applying them when I typed commands in the terminal. (See reference link) So I had to fix PATH.
- G-(1): first, find my PATH
```terminal
echo $PATH
``` 
- G-(2): add the location of the pyinstaller executable to my PATH (replace /path/to/pyinstaller to actual path)
```terminal
export PATH="$PATH:/path/to/pyinstaller"
``` 
----

### 4. see about_Execution_Policies
- Environment: powershell
- Reference: TBA
- A. Situation: to prepare web crawling, I created virtual environment with [venv](https://docs.python.org/3/library/venv.html). I then tried to activate via \Scripts\activate
- B. Error:
```terminal
cannot be loaded because running script is disabled on this system. For more information, see about_Execution_Policies
``` 
- C. Fix: Run PowerShell as an administrator and change as below
```terminal
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned
``` 
- By default, execution policy is set to "Restricted." This will prevent the execution of any script files for security purposes. By setting policy to RemoteSigned, virtual environment for selenium will be created by showing "(selenium)" in front of the path on the powershell.
----

### 5. Chrome page closes immediately after it's opend via selenium
- Library: selenium
- Reference: Note TBA, [StakeOverflow case](https://stackoverflow.com/questions/47508518/google-chrome-closes-immediately-after-being-launched-with-selenium)
- A. Situation: to prepare web crawling, I downloaded chromedriver and moved .exe file to the same path where .py script is. I then tested below codes to see if Chrome is opening without any issues.
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
```  
- B. Error: Chrome pages opens and it immediately closes after a second.
- C. Fix: add sleep module as below
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
time.sleep(10)
```  
- (Q) My Chrome is 64-bit but Chromedriver is 32-bit. Could it cause the issue? (A) No. Official site confirmed chromdriver win32 works for both 32 and 64-bits.

  
