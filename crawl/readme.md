# Documentation for Web Content Scraper

## Overview
This script is designed to scrape data from a list of URLs provided in a CSV file. It fetches the content, extracts specific product information, and logs the operations performed. Optionally, the extracted content can also be saved. The script utilizes various libraries such as `requests`, `BeautifulSoup`, and `argparse` to ensure efficient and robust operation.

## Prerequisites
Make sure the following Python packages are installed:
- `requests`
- `beautifulsoup4`
- `urllib3`

To install the dependencies, run the following command:
```sh
pip install requests beautifulsoup4
```
## How to Use
Arguments
The script accepts command-line arguments that allow customization of behavior:
--csv_path: The path to the CSV file containing URLs to scrape. The default value is ./urls.csv.
--save_result: A boolean flag indicating whether to save the scraped results. The default value is False.
## Running the Script
You can run the script by using the following command:

```sh
Copy code
python main.py --csv_path <path_to_csv> --save_result <True/False>
```
For example:
```sh
Copy code
python main.py --csv_path ./urls.csv --save_result True
```
## CSV File Format
The CSV file should contain a list of URLs, with each URL on a new line. Here is an example:
```
https://example.com/page1
https://example.com/page2
```

