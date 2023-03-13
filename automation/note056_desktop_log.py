## LOGGING HOT-TO DOC: https://docs.python.org/3/howto/logging.html
## REFERENCE VIDEO   : https://www.youtube.com/watch?v=-ARI4Cz-awo&ab_channel=CoreySchafer

#note056_desktop_log.py
import logging


########## 1. WHAT IS LOG? 
# Question: For beginner Python-developer like me, would wonder... what is log? and why should I use log? 
#           I can use print() to check whether certain codes or process has been completed.
# Answer  : With log, you can easily find when and where issue has been raised.
#           Combined with if statement and raise ValueError, we can track errors easily.
#           Also, logs can be stored and imported to file and used for other purposes like analysis, reporting etc.
# Ref     : (why logging than print) https://stackoverflow.com/questions/6918493/in-python-why-use-logging-instead-of-print


########## 2. BASIC CONFIGURATION
logging.basicConfig(level = logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
#level: all the logging for level above DEBUG will be shown
#%(asctime)s: log will contain time information
#[%(levelname)s]: log will show level name in bracket ex. [ERROR]
#%(message)s": log will show message information

#1) log level: debug < info < warning < error < critical
logging.debug("Debug point")                    #2023-02-19 21:20:44, 172 [DEBUG] Debug point
logging.info("Info point")                      #2023-02-19 21:20:44, 172 [INFO] Info point
logging.warning("Warning, review code")         #2023-02-19 21:20:44, 172 [WARNING] Warning, review code
logging.error("Error, must check the code")     #2023-02-19 21:20:44, 172 [ERROR] Error, must check the code
logging.critical("Critical, failed! failed!")   #2023-02-19 21:20:44, 172 [CRITICAL] Critical, failed! failed!

#2) log level change:
logging.basicConfig(level = logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")
#with above code, only last two codes will show message from #1 and rest messages will be ignored


########## 3. SAVE LOGS IN TERMINAL AND IN FILE
from datetime import datetime

#set the log format first
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

#leave log in the terminal(=stream)
streamHandler = logging.StremHandler()
streamHandler.setFormatter(logFormatter)

#leave log to file
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")  #file name will contain date time info
fileHandler = logging.FileHandler(filename, encoding = "utf-8")   #if you use Korean add encoding
fileHanlder.setFormatter(logFormatter)

#get logs
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)    #setting log level
logger.addHandler(steramHandler)
logger.addHandler(fileHandler)

logger.debug("this is a test")   #test

  
