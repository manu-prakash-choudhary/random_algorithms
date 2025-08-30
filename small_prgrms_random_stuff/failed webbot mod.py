from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webbot import Browser 

#options = Options()
#options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
#web = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Users\choud\chromedriver.exe')
web=Browser()
web.go_to('google.com') 
web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
web.press(web.Key.ENTER)
web.go_back()
web.click('Sign in')
web.type('mymail@gmail.com' , into='Email')
web.click('NEXT' , tag='span')
web.type('mypassword' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span')
 
