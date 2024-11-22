import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class WebContentParser:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/50.0.2661.102 Safari/537.36'
            )
        }
        self.session = self._initialize_session()
        self.main_response = None
        self.all_page_data = []

    def _initialize_session(self):
        """Set up the session with retry strategy."""
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

    def fetch_content(self):
        """Fetch the main content from the URL."""
        try:
            self.main_response = self.session.get(
                self.url, verify=False, timeout=30, headers=self.headers
            )
            print(f'URL fetched: {self.url}')
            return self.main_response
        except requests.RequestException as e:
            print(f"Failed to fetch the URL: {e}")
            return None

    def parse_content(self):
        """Parse the fetched HTML content."""
        if not self.main_response:
            print("No response available to parse.")
            return []

        main_soup = BeautifulSoup(self.main_response.content, 'html.parser')
        datas = main_soup.find('main', {'id': 'main'})
        if not datas:
            print("No 'main' element found.")
            return []

        all_tag = datas.find_all(['h1', 'h2', 'h3', 'p', 'blockquote', 'ul'])
        each_title_data = {}

        for tag in all_tag:
            if tag.name in ['h1', 'h2']:
                if each_title_data:
                    self.all_page_data.append(each_title_data)
                    each_title_data = {}
                each_title_data['metadata'] = tag.text.strip()

            elif tag.name == 'h3':
                if tag.text.strip() == 'Resources':
                    each_title_data[tag.text.strip()] = ''
                else:
                    if each_title_data:
                        self.all_page_data.append(each_title_data)
                        each_title_data = {}
                    each_title_data['metadata'] = tag.text.strip()

            elif tag.name in ['p', 'blockquote']:
                num = len(each_title_data)
                key = f'content {num}'
                if tag.text.strip():
                    each_title_data[key] = tag.text.strip()

            elif tag.name == 'ul':
                text = ' '.join(
                    li.text.strip()
                    for li in tag.find_all('li', {'class': 'mdx-lists_listItem__nkqhg'})
                )
                if 'Resources' in each_title_data:
                    each_title_data['Resources'] = text
                else:
                    num = len(each_title_data)
                    key = f'content {num}'
                    if text:
                        each_title_data[key] = text

        if each_title_data:
            self.all_page_data.append(each_title_data)

        return self.all_page_data

    def get_data(self):
        """Main method to fetch and parse content."""
        self.fetch_content()
        return self.parse_content()

