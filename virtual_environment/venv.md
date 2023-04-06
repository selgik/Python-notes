# Requirements:
- Visual Studio
- Venv Documentation

# Why Virtual Environment?
- We may need to use particular library version depending on the projects
- For example, Python 3.5 library A11 for project "Nice" and Python 3.9 library A13 for project "Super"
- It would be then easier to separate area (virtual enviroments) for each projects

# How to Set Up Virtual Environment?
1. search python venv at Google
2. refer official [document](https://docs.python.org/3/library/venv.html) for set up
3. open Terminal at Visual Studio and paste below (right click will do paste)
    ```terminal
    python -m venv /path/to/new/virtual/environment
    ```
    for example, we can create a folder named "selenium" then type below instead
    ```terminal
    python -m venv selenium
    ```
    new folder will be created within Visual Studio workplace
4. let's go to the virtual environment
   ```terminal
    C:\yourname\selenium\Scripts
    ``` 
    then C:\address will be updated. Type below furter:
    ```terminal
    C:\yourname\selenium\Scripts>activate
    ``` 
5. what happens next? 
    - (selenium) will appear before directory address such as (selenium) C:\ ...
6. what does it mean? 
    - that means you are inside the virtual environment. 
    - any installation of packages or running codes will happen in virtual environment not affecting main Python workplace
 
    
- THE END - 
