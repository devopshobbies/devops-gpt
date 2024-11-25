
import argparse
import csv
import logging
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from content_parser import WebContentParser


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )


def setup_http_session():
    retry_strategy = Retry(
        total=5,
        backoff_factor=8,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    adapter.max_retries.respect_retry_after_header = False
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def process_urls(file_path, save_result):
    http = setup_http_session()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Check if the row is not empty
                main_url = row[0]
                try:
                    main_response = http.get(main_url, verify=False, timeout=30, headers=headers)
                    logging.info(f'Fetched URL: {main_url}')
                except requests.RequestException as e:
                    logging.error(f"Failed to fetch URL {main_url}: {e}")
                    continue

                main_soup = BeautifulSoup(main_response.content, 'html.parser')
                products = main_soup.find('div', {'class': 'marketing-content_root__DE3hU'}).find_all('div', {'class': 'card-grid-block_root__yDdm_'})
                logging.info(f'Found {len(products)} products on page: {main_url}')
                all_data = []
                for product in products:
                    # Get org title
                    title = product.find('h2').text
                    sub_content_link=[]
                    all_sub_title = product.find_all('li')
                    for res in all_sub_title:
                        sub_part_content = {}
                        sub_part_content['main_title'] = title
                        sub_title = res.find('span', {'class': 'card-title_text__F97Wj'}).get_text()
                        sub_part_content['sub_title'] = sub_title
                        sub_title_link = 'https://developer.hashicorp.com' + res.find('a').attrs['href']
                        sub_part_content['sub_title_link'] = sub_title_link

                        parser = WebContentParser(sub_title_link)
                        data = parser.get_data()
                        sub_part_content['all_data_info'] = data

                        logging.info(f'Parsed content for sub-title: {sub_title}')
                        sub_content_link.append(sub_part_content)
                    all_data.append(sub_content_link)
                if save_result:
                    # Logic to save sub_part_content goes here (e.g., writing to a file or database)
                    logging.info(f'Saving result for: {all_data}')
                else:
                    print(all_data)
                          

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description='Process URLs from a CSV file.')
    parser.add_argument('--csv_path', type=str, default='./urls.csv', help='Path to the CSV file containing URLs')
    parser.add_argument('--save_result', type=bool, default=False, help='Flag to indicate if the results should be saved')
    args = parser.parse_args()

    process_urls(args.csv_path, args.save_result)


if __name__ == '__main__':
    main()
