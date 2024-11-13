
'''
here we extract all title and subtitle with their links

'''

import requests
from bs4 import BeautifulSoup
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

main_url ="https://developer.hashicorp.com/terraform/docs"

retry_strategy = Retry(
                        total=5,
                        backoff_factor=8,
                        )
adapter = HTTPAdapter(max_retries=retry_strategy)
adapter.max_retries.respect_retry_after_header = False
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
main_response = http.get(main_url, verify=False ,timeout=30,headers=headers)
print('main_url:',main_url)
print(main_response)


main_soup = BeautifulSoup(main_response.content,'html.parser')
products = main_soup.find('div',{'class':'marketing-content_root__DE3hU'}).find_all('div',{'class':'card-grid-block_root__yDdm_'})
print(len(products))

for product in products:

    # get org title
    title = product.find('h2').text
    print(title)
    
    # git org title's subtitles and links
    all_sub_title = product.find_all('li')
    for res in all_sub_title:
        sub_title = res.find('span',{'class':'card-title_text__F97Wj'}).get_text()
        sub_title_link = 'https://developer.hashicorp.com' + res.find('a').attrs['href']
        print(sub_title)
        print(sub_title_link)
    print('-----------')