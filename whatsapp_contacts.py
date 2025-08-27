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

# Updated list of names (without "+" but include country code)

# names = [
#     "Aarzoo", "Aryansh", "Bhavin", "Fiza", "Ghanshyam", "Prima"
# ]

#5A3
names = [
    "Yashii", "Abhishek", "Pramendra"
]
failed_names = []

message = """
\nHey, I'm excited to share the LinkedIn page for my company, Varcode EdTech! We're all about helping learners grow with practical coding skills and industry-ready courses.\n\nIt'd be great if you could check it out, give it a follow, and explore future opportunities with us!\n\nVisit us: https://varcode.in/\nFollow us on: https://www.linkedin.com/company/varcode-edtech/\n\nThanks for your support—it means a lot
"""

# Loop through each name
for name in names:
    try:
        # Locate the message input box using a more specific XPath
        search_box = driver.find_element(By.XPATH, '//span[@data-icon="search-refreshed-thin"]')
        search_box.click()
        # enter the name to the focused input box
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
        search_box.send_keys(name + Keys.ENTER)
        time.sleep(1)  # Small delay to avoid issues
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@aria-label="Type a message"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        
        time.sleep(3)  # Small delay to avoid issues

        print(f"Message sent to {name}")
    except Exception as e:
        failed_names.append(name)
        print(f"Failed to send message to {name}: {e}")

if len(failed_names):
    print("Failed names are ", failed_names)
else:
    print("Messsage sent on all names successfully")
driver.quit()  # Close the browser





# options.addArguments("start-maximized"); // open Browser in maximized mode
# options.addArguments("disable-infobars"); // disabling infobars
# options.addArguments("--disable-extensions"); // disabling extensions
# options.addArguments("--disable-gpu"); // applicable to windows os only
# options.addArguments("--disable-dev-shm-usage"); // overcome limited resource problems
# options.addArguments("--no-sandbox"); // Bypass OS security model
# WebDriver driver = new ChromeDriver(options);
# driver.get("https://google.com");