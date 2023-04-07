# Requirements:
- Visual Studio
- Venv Documentation

# Why Virtual Environment?
- We may need to use particular library version depending on the projects
- For example, Python 3.5 library A11 for project "Nice" and Python 3.9 library A13 for project "Super"
- It would be then easier to isolate area (virtual enviroments) for each projects

# Why Virtual Environment for Selenium?
- Extracted by answers from ChatGPT:
> - You can still use Selenium in a regular Python environment without a virtual environment, but using a virtual environment like venv can help you avoid potential issues and maintain better project organization.  
> - Without a virtual environment, it can be easy to install packages globally or mix package versions, leading to conflicts or unexpected behavior. For example, if you install a newer version of a package required by Selenium globally, but an older version is required by another project, you may run into issues.  
> - Using a virtual environment like venv ensures that the packages you install are isolated from other projects and the global environment, reducing the risk of conflicts and making it easier to manage dependencies for your project. Additionally, if you need to share your project with others, it can be difficult to ensure that they have the same package versions installed, which can cause compatibility issues. A virtual environment can help you avoid this problem by allowing you to specify the exact package versions needed for your project.  
> - In summary, while you can still use Selenium without a virtual environment, using venv can help you avoid potential issues, maintain better organization, and make it easier to share your project with others.

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
 
    
THE END
