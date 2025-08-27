from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from os import system
from selenium.webdriver.common.keys import Keys


options = Options()
# options.add_argument("--headless") # Run in headless mode
options.add_argument("--no-sandbox") # Bypass OS security model
options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
options.add_argument("--disable-gpu") # applicable to windows os only
options.add_argument("--disable-extensions") # disabling extensions
options.add_argument("start-maximized") # open Browser in maximized mode
options.add_argument("disable-infobars") # disabling infobars
# set chrome location
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# Initialize the WebDriver
driver = webdriver.Chrome(options=options)


# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
input("Scan the QR code on WhatsApp Web and press Enter to continue...")

# Updated list of numbers (without "+" but include country code)

numbers = [
    "916265452282", "916351044491", "91635166077", "916351394963", "917004255675", "917041690396", 
"917091362220", "917227081369", "917410135526", "917436028508", "917572877852", "917624010356", 
"917791814739", "917850995920", "917984812483", "918085769067", "918090767809", "918160948601", 
"918219698434", "918423139694", "918529043249", "918591266831", "918780364562", "918788030914", 
"918956083167", "918898146299", "919054151166", "919104706589", "919106005935", "919117654776", 
"919137791587", "919157129423", "919172018492", "919302733463", "919316755359", "919352868523", 
"919427244302", "919455929218", "919510290640", "919512576576", "919537089866", "919537428628", 
"919558577877", "919662742767", "919725953753", "919742492533", "919825970013", "919904222695", 
"919909391423", "919909638694", "919924922282", "919977276746", "919978603644", "919978848346", 
"919979154804", "919987345252", "919998358590", "9779807404804", "9779817454543"

]
failed_numbers = []

message = """Hey!\n I'm excited to share the LinkedIn page for my company, Varcode EdTech! We're all about helping learners grow with practical coding skills and industry-ready courses.\nIt'd be great if you could check it out, give it a *follow*, and explore future opportunities with us!\nHere's the link: https://www.linkedin.com/company/varcode-edtech/ \nThanks for your support—it means a lot!"""

# Loop through each number
for number in numbers:
    try:
        # Locate the message input box using a more specific XPath
        search_box = driver.find_element(By.XPATH, '//span[@data-icon="search"]')
        search_box.click()
        # enter the number to the focused input box
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
        search_box.send_keys("my stuff" + Keys.ENTER)
        time.sleep(1)  # Small delay to avoid issues
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@aria-label="Type a message"]')
        message_box.send_keys(number + Keys.ENTER)
        phone_number = driver.find_element(By.XPATH, f'//a[text()="{number}"]')
        phone_number.click()
        time.sleep(1)
        chat_with = driver.find_element(By.XPATH, '//div[@aria-label="Chat with "]')
        chat_with.click()
        time.sleep(2)
        # enter message in the focused input box
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@aria-label="Type a message"]')
        message_box.send_keys(message + Keys.ENTER)
        time.sleep(3)  # Small delay to avoid issues

        print(f"Message sent to {number}")
    except Exception as e:
        failed_numbers.append(number)
        print(f"Failed to send message to {number}: {e}")

if len(failed_numbers):
    print("Failed Numbers are ", failed_numbers)
else:
    print("Messsage sent on all numbers successfully")
driver.quit()  # Close the browser





# options.addArguments("start-maximized"); // open Browser in maximized mode
# options.addArguments("disable-infobars"); // disabling infobars
# options.addArguments("--disable-extensions"); // disabling extensions
# options.addArguments("--disable-gpu"); // applicable to windows os only
# options.addArguments("--disable-dev-shm-usage"); // overcome limited resource problems
# options.addArguments("--no-sandbox"); // Bypass OS security model
# WebDriver driver = new ChromeDriver(options);
# driver.get("https://google.com");