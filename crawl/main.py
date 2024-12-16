from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

# Set up headless mode if you don't want to see the browser
chrome_options = Options()
# Uncomment the following line to run Chrome in headless mode
#chrome_options.add_argument("--headless")

# Provide the path to your ChromeDriver
service = Service('/usr/bin/google-chrome')  # Update this path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# # List of URLs to crawl
urls = [
    "https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs"
]

# Directory to save the files
save_dir = "crawled_data"
os.makedirs(save_dir, exist_ok=True)

def fetch_and_save(url):
    try:
        driver.get(url)
        
        # Optionally wait for some time for JavaScript to render (you might need to adjust this)
        time.sleep(5)

        # Fetch the title and all paragraphs
        title = driver.title
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')

        # Prepare the file name
        file_name = os.path.join(save_dir, f"{title}.txt")

        # Write the content to the file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n")
            for para in paragraphs:
                file.write(para.text + "\n")

        print(f"Saved content from {url} to {file_name}")

    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

# Fetch and save data from each URL
for url in urls:
    fetch_and_save(url)

# Close the driver
driver.quit()