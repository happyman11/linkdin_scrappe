
    
from linkedin_scraper import Person, actions
from selenium import webdriver

path="/home/ravishekhartiwari/Desktop/LINKDIN_SCRAPP/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=path)


#email = "tiwari11.rst@gmail.com"
#password = "Ravishekhar@99"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person()    


actions.scrape(close_on_complete=True)