from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ---- Chrome Options ----
options = Options()
# options.add_argument("--headless")   # Uncomment to run headless
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")

# Adjust Chrome binary path if required
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# ---- Open WhatsApp Web ----
driver.get("https://web.whatsapp.com")
input("Scan the QR code on WhatsApp Web and press Enter to continue...")

# ---- Names list ----
names = ["Yashii", "Abhishek", "Pramendra"]
failed_names = []

# ---- Message to send ----
message = (
    """...\nHey!\nI'm excited to share the LinkedIn page for my company, Varcode EdTech! We're all about helping learners grow with practical coding skills and industry-ready courses.\n\nIt'd be great if you could check it out, give it a follow, and explore future opportunities with us!\n\nVisit us: https://varcode.in/\nFollow us on: https://www.linkedin.com/company/varcode-edtech/\n\nThanks for your support—it means a lot!"""
)

# ---- Send message loop ----
for name in names:
    try:
        # Step 1: Search the contact
        search_icon = driver.find_element(By.XPATH, '//span[@data-icon="search-refreshed-thin"]')
        search_icon.click()

        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.clear()
        search_box.send_keys(name)
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)  # Open chat

        # Step 2: Type + Send message
        time.sleep(1)
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@aria-label="Type a message"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        print(f"✅ Message sent to {name}")
        time.sleep(2)

    except Exception as e:
        failed_names.append(name)
        print(f"❌ Failed to send message to {name}: {e}")

# ---- Wrap up ----
if failed_names:
    print("Failed names:", failed_names)
else:
    print("✅ Message sent to all names successfully")

driver.quit()
