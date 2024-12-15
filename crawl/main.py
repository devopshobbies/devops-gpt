import requests
from bs4 import BeautifulSoup
import os

# List of URLs to crawl
urls = [
   
]

# Directory to save the files
save_dir = "crawled_data"
os.makedirs(save_dir, exist_ok=True)

def fetch_and_save(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # For demonstration, we are fetching the page title and all paragraphs
        title = soup.title.string if soup.title else "no_title"
        paragraphs = soup.find_all('p')

        # Prepare the file name
        file_name = os.path.join(save_dir, f"{title}.txt")
        
        # Write the content to the file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n")
            for para in paragraphs:
                file.write(para.get_text() + "\n")

        print(f"Saved content from {url} to {file_name}")

    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

# Fetch and save data from each URL
for url in urls:
    fetch_and_save(url)
